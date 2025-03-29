import requests

class PastebinCheck:
    def __init__(self, api_key):
        self.api_key = api_key

    def search_pastes(self, keyword):
        url = f"https://pastebin.com/api/api_post.php"
        data = {
            'api_dev_key': self.api_key,
            'api_option': 'search',
            'api_paste_data': keyword
        }
        response = requests.post(url, data=data)
        return response.json()
