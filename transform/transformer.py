import datetime
import re
from datetime import date


class RecruitListFormat:
    def __init__(self):
        self.url = None
        self.title = None
        self.region = None
        self.company = None
        self.employee_type = None
        self.start_date = None
        self.end_date = None
        self.category = None
        self.created_date = str(date.today())

    def __str__(self):
        return f'{self.url} | {self.title} | {self.company}'

    def get_tuple(self):
        return (self.url, self.title, self.region, self.company, self.employee_type,
                self.start_date, self.end_date, self.category, self.created_date)


class LineTransformer:
    def __init__(self):
        self.data = []
        self.dummies = []

    def transform(self, raw_data):
        file = raw_data
        file = re.search('<ul class="job_list">.*?</ul>', file).group()

        job_list = re.finditer('<li><a.*?ko/jobs.*?/a></li>', file, re.DOTALL)

        for job in job_list:
            try:
                text = job.group()
                data = RecruitListFormat()
                data.url = re.search('<a.*?href="(.*?)">', text).group(1)
                data.title = re.search('<h3.*?>(.*?)<.*?h3>', text).group(1)
                data.region, data.company, data.category, data.employee_type = re.search(
                    '<div class="text_filter"><span>(.*?)</span>.*?<span>(.*?)</span>.*?<span>'
                    '(.*?)</span>.*?<span>(.*?)</span>.*?</div>',
                    text).groups()
                date = re.search('<span class="date">(.*?)</span>', text).group(1)
                data.start_date, data.end_date = date.split('~')

                self.data.append(data)

            except Exception as e:
                print("Error: LineTransformer: ", e)
                self.dummies.append(job.group())

        self.__dump_dummies()
        return self.data

    def __dump_dummies(self):
        if len(self.dummies) > 0:
            with open(f'data/dummies/line_{datetime.date.today()}', 'w', -1, 'utf-8') as f:
                for dummy in self.dummies:
                    f.write(dummy + '\n')


class KakaoTransformer:
    def __init__(self):
        self.data = []
        self.dummies = []

    def transform(self, raw_data):
        file = raw_data
        file = re.sub('\s{2,}', ' ', file)
        file = re.search('<ul class="list_jobs">.*?</ul>', file).group()

        job_list = re.finditer('<li.*?/li>', file, re.DOTALL)

        for job in job_list:
            try:
                text = job.group()
                data = RecruitListFormat()

                data.url = re.search('<a href="(.*?)" class.*?">', text).group(1)
                data.title = re.search('<h4.*?>(.*?)</h4>', text).group(1)
                data.end_date, data.region, data.company, data.employee_type = re.findall('<dd>(.*?)</dd>', text)
                data.category = "Tech"
                data.hashtags = re.findall('<span class="txt_hash">.*?</span>(.*?)</a>', text)

                self.data.append(data)

            except Exception as e:
                print("Error: KakaoTransformer: ", e)
                self.dummies.append(job.group())

        self.__dump_dummies()

        return self.data

    def __dump_dummies(self):
        if len(self.dummies) > 0:
            with open(f'data/dummies/kakao_{datetime.date.today()}', 'w', -1, 'utf-8') as f:
                for dummy in self.dummies:
                    f.write(dummy + '\n')
