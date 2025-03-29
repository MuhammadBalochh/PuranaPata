import requests

WAYBACK_API = "http://web.archive.org/cdx/search/cdx?url={url}&output=json&limit={limit}"
WAYBACK_CONTENT = "http://web.archive.org/web/{timestamp}/{url}"

class Scraper:
    @staticmethod
    def fetch_snapshots(url, limit):
        response = requests.get(WAYBACK_API.format(url=url, limit=limit))
        snapshots = response.json()[1:]
        return snapshots

    @staticmethod
    def download_snapshot(url, timestamp):
        response = requests.get(WAYBACK_CONTENT.format(timestamp=timestamp, url=url))
        if response.status_code == 200:
            return response.text
        return None
