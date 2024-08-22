import sys
import os
from datetime import date, datetime
from task_4_1 import normalise_letter_case


class Publishing:
    def __init__(self):
        self.type = 'Publication'
        self.publication_content = None
        self.file = 'news_feed_data'
        self.records_num = 1

    def add_record(self):
        with open('news_feed', 'a') as f:
            f.write(self.publication_content)

    def read_records(self):
        with open(self.file) as f2:
            records = [x.split('\n') for x in normalise_letter_case(f2.read()).split('\n\n')]
            lst = []
            for i in records[:self.records_num]:
                dicts = {}
                dicts.setdefault('type', i[0])
                dicts.setdefault('text', i[1])
                dicts.setdefault('attribute', i[2])
                lst.append(dicts)
        os.remove(self.file)
        return lst


class AddNews(Publishing):
    def __init__(self, text, city):
        super().__init__()
        self.type = 'News'
        self.header = self.type.ljust(40, '-')
        self.text = text
        self.city = city
        self.publication_content = f"{self.header}\n{self.text}\n{self.city}, {date.today()}\n\n"


class AddAdvertising(Publishing):
    def __init__(self, text, date):
        super().__init__()
        self.type = 'Private Ad'
        self.header = self.type.ljust(40, '-')
        self.text = text
        self.end_date = datetime.strptime(date, '%Y-%m-%d')
        self.days_to_end = abs(datetime.today() - self.end_date)
        self.publication_content = f"{self.header}\n{self.text}\nActual until: {self.end_date}, {self.days_to_end.days} days left\n\n"


class AddAnnouncement(Publishing):
    def __init__(self, text, phone):
        super().__init__()
        self.type = 'Announcement'
        self.header = self.type.ljust(40, '-')
        self.text = text
        self.phone = phone
        self.publication_content = f"{self.header}\n{self.text}\nPhone: {self.phone}\n\n"


class ReadTxt(Publishing):
    def __init__(self, file, records_num):
        super().__init__()
        self.file = file
        self.records_num = records_num


def check_type(t):
    if t == 1:
        text = input('What happened?\n')
        city = input('Where it happened?\n')
        news = AddNews(text, city)
        news.add_record()
    elif t == 2:
        text = input('What do you promote?\n')
        date = input('When is the last day of the ad?\n')
        add = AddAdvertising(text, date)
        add.add_record()
    elif t == 3:
        text = input('What do you announce?\n')
        phone = input('What is your phone number?\n')
        anounce = AddAnnouncement(text, phone)
        anounce.add_record()
    elif t == 4:
        file = input('Enter file name\n')
        records_num = int(input('Enter the number of records\n'))
        readfile = ReadTxt(file, records_num)
        a = readfile.read_records()
        for x in a:
            if x['type'] == 'News':
                news = AddNews(x['text'], x['attribute'])
                news.add_record()
            elif x['type'] == 'Private ad':
                add = AddAdvertising(x['text'], x['attribute'])
                add.add_record()
            elif x['type'] == 'Announcement':
                anounce = AddAnnouncement(x['text'], x['attribute'])
                anounce.add_record()


while True:
    marker = int(input('Select type of record. 1 - News, 2 - Ad, 3 - Announcement, 4 - Upload from file, 5 - For Exit:\n'))
    if marker != 5:
        check_type(marker)
    else:
        sys.exit()
