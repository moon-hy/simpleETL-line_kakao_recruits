import requests

line_url = 'https://careers.linecorp.com/ko/jobs'


class BaseExtractor:
    def __init__(self, url):
        self.url = url
        self.headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'}
        self.raw_data = None

    def extract(self):
        response = requests.get(self.url, headers=self.headers)
        response.encoding = response.apparent_encoding

        self.raw_data = response.text
        return self.raw_data


class LineExtractor(BaseExtractor):
    def __init__(self):
        super(LineExtractor, self).__init__('https://careers.linecorp.com/ko/jobs')
