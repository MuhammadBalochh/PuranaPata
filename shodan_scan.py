import shodan

class ShodanScan:
    def __init__(self, api_key):
        self.api_key = api_key
        self.api = shodan.Shodan(self.api_key)

    def scan_ip(self, ip):
        try:
            return self.api.host(ip)
        except shodan.APIError as e:
            return f"Error: {e}"
