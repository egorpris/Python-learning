import sys
from datetime import date, datetime


class Publishing:
    def __init__(self):
        self.type = 'Publication'
        self.publication_content = None

    def add_record(self):
        with open('news_feed', 'a') as f:
            f.write(self.publication_content)


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


while True:
    marker = int(input('Select type of record. 1 - News, 2 - Ad, 3 - Announcement, 4 - For Exit:\n'))
    if marker != 4:
        check_type(marker)
    else:
        sys.exit()
