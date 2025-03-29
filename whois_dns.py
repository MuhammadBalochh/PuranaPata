import whois
import dns.resolver

class WhoisDNS:
    @staticmethod
    def get_whois_info(domain):
        return whois.whois(domain)

    @staticmethod
    def get_dns_records(domain):
        try:
            dns_records = dns.resolver.resolve(domain, 'A')
            return [rdata.address for rdata in dns_records]
        except Exception as e:
            return str(e)
