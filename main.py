import argparse
import os
import importlib.util
import sys
from scraper import Scraper
from keyword_scanner import KeywordScanner
from exporters import Exporters
from whois_dns import WhoisDNS
from shodan_scan import ShodanScan
from reddit_scan import RedditScan
from pastesite_check import PastebinCheck

def load_plugin(plugin_name):
    """
    Dynamically loads and returns the plugin module.
    """
    plugin_path = os.path.join("plugins", f"{plugin_name}.py")
    
    if not os.path.exists(plugin_path):
        print(f"Plugin '{plugin_name}' not found!")
        return None
    
    spec = importlib.util.spec_from_file_location(plugin_name, plugin_path)
    plugin_module = importlib.util.module_from_spec(spec)
    sys.modules[plugin_name] = plugin_module
    spec.loader.exec_module(plugin_module)
    
    # Assuming the plugin has a `Plugin` class with an `execute` method
    if hasattr(plugin_module, "Plugin"):
        plugin_class = getattr(plugin_module, "Plugin")
        return plugin_class
    else:
        print(f"Plugin '{plugin_name}' does not implement the required 'Plugin' class.")
        return None

def main():
    parser = argparse.ArgumentParser(description="PuranaPata OSINT Tool")
    parser.add_argument("url", help="Target URL")
    parser.add_argument("--limit", type=int, default=5, help="Number of snapshots to fetch")
    parser.add_argument("--export", choices=["pdf", "json", "xlsx"], help="Export format")
    parser.add_argument("--keywords", help="Comma-separated list of keywords to scan")
    parser.add_argument("--whois", action="store_true", help="Fetch WHOIS data")
    parser.add_argument("--dns", action="store_true", help="Fetch DNS records")
    parser.add_argument("--shodan", help="Query Shodan with an IP address")
    parser.add_argument("--reddit", help="Analyze Reddit user history")
    parser.add_argument("--pastebin", help="Check Pastebin for keyword leaks")
    parser.add_argument("--plugin", help="Run a custom plugin")
    
    args = parser.parse_args()

    # Fetch snapshots
    snapshots = Scraper.fetch_snapshots(args.url, args.limit)

    # Save snapshots locally and scan for keywords
    if args.keywords:
        keywords = [k.strip() for k in args.keywords.split(",")]
        for timestamp, _ in snapshots:
            content = Scraper.download_snapshot(args.url, timestamp)
            if content:
                save_snapshot(args.url, timestamp, content)
                matches = KeywordScanner.scan_content(content, keywords)
                if matches:
                    print(f"Matches found in {timestamp}: {matches}")

    # Export based on user choice
    if args.export == "pdf":
        Exporters.export_to_pdf(args.url, snapshots)
    elif args.export == "json":
        Exporters.export_to_json(args.url, snapshots)
    elif args.export == "xlsx":
        Exporters.export_to_excel(args.url, snapshots)

    # WHOIS & DNS
    if args.whois:
        whois_info = WhoisDNS.get_whois_info(args.url)
        print(whois_info)
    if args.dns:
        dns_records = WhoisDNS.get_dns_records(args.url)
        print(dns_records)

    # Shodan Scan
    if args.shodan:
        shodan_api_key = "your_shodan_api_key"
        shodan_tool = ShodanScan(shodan_api_key)
        shodan_info = shodan_tool.scan_ip(args.shodan)
        print(shodan_info)

    # Reddit Scan
    if args.reddit:
        reddit_client_id = "your_reddit_client_id"
        reddit_client_secret = "your_reddit_client_secret"
        reddit_user_agent = "your_reddit_user_agent"
        reddit_tool = RedditScan(reddit_client_id, reddit_client_secret, reddit_user_agent)
        reddit_posts = reddit_tool.scan_user_posts(args.reddit)
        print(reddit_posts)

    # Pastebin Check
    if args.pastebin:
        pastebin_api_key = "your_pastebin_api_key"
        pastebin_tool = PastebinCheck(pastebin_api_key)
        pastebin_leaks = pastebin_tool.search_pastes(args.pastebin)
        print(pastebin_leaks)

    # Plugin Integration
    if args.plugin:
        plugin_class = load_plugin(args.plugin)
        if plugin_class:
            plugin_instance = plugin_class(args)
            plugin_instance.execute()

if __name__ == "__main__":
    main()
