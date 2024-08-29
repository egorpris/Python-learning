import sys
import os
import csv
import string
import xml.etree.ElementTree as ET
from datetime import date, datetime
from task_4_1 import normalise_letter_case


class Publishing:
    def __init__(self):
        self.type = 'Publication'
        self.publication_content = None

    def add_record(self):
        with open('news_feed', 'a') as f:
            f.write(self.publication_content)
        statistics = CSV('news_feed')
        statistics.count_words()
        statistics.count_letters()


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


class ReadFile:
    def __init__(self, file, records_num):
        super().__init__()
        self.file = file
        self.records_num = records_num

    def read_txt(self):
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

    def read_json(self):
        with open(self.file) as f2:
            a = eval(f2.read())
        os.remove(self.file)
        return a

    def read_xml(self):
        xml = ET.parse(self.file)
        root = xml.getroot()
        lst = []
        for x in root.iter('type'):
            lst.append({'type': x.text})
        for i, x in enumerate(root.iter('text')):
            lst[i].setdefault('text', x.text)
        for i, x in enumerate(root.iter('attribute')):
            lst[i].setdefault('attribute', x.text)
        # os.remove(self.file)
        return lst


def get_word(text):
    for i in '0123456789!@#$%^&*():;".,?/_-+=':
        if i in text:
            text = text.replace(i, '')

    return text


def total_count_letters(text):
    letter_frequency = {}
    for m in text.lower():
        if m in string.ascii_letters:
            if m in letter_frequency:
                letter_frequency[m] += 1
            else:
                letter_frequency[m] = 1

    return letter_frequency


def count_characters(text, condition):
    letter_frequency = {}
    for m in text:
        if m in condition and m in letter_frequency:
            letter_frequency[m.lower()] += 1
        elif m in condition and m not in letter_frequency:
            letter_frequency[m.lower()] = 1
        else:
            letter_frequency[m.lower()] = 0

    return letter_frequency


class CSV:
    def __init__(self, file):
        super().__init__()
        self.file = file

    def count_words(self):
        with open(self.file) as f:
            lst = [x.lower().strip().split(" ") for x in f.readlines()]
            lst = [[get_word(i) for i in x]for x in lst]
            word_frequency = {}
            for i in lst:
                for m in i:
                    if m in word_frequency and m != '':
                        word_frequency[m] += 1
                    elif m not in word_frequency and m != '':
                        word_frequency[m] = 1

        os.remove('cnt_words')
        with open('cnt_words', 'w', newline='') as words_csv:
            headers = ['word', 'count']
            writer = csv.DictWriter(words_csv, fieldnames=headers)
            writer.writeheader()
            for x, y in word_frequency.items():
                writer.writerow({'word': x, 'count': y})

    def count_letters(self):
        with open(self.file) as f:
            a = f.read()
            b = total_count_letters(a)
            c = count_characters(a, string.ascii_uppercase)
            letter_percentage = {}
            for x, y in b.items():
                letter_percentage[x] = round(y / len(a) * 100, 2)

        os.remove('cnt_letters')
        with open('cnt_letters', 'w', newline='') as words_csv:
            headers = ['letter', 'count', 'upper_count', 'percentage']
            writer = csv.DictWriter(words_csv, fieldnames=headers)
            writer.writeheader()
            for x, y in b.items():
                writer.writerow({'letter': x, 'count': y, 'upper_count': c[x],
                                 'percentage': letter_percentage[x]})


def add_record_from_file(input):
    for x in input:
        if x['type'] == 'News':
            news = AddNews(x['text'], x['attribute'])
            news.add_record()
        elif x['type'] == 'Private ad':
            add = AddAdvertising(x['text'], x['attribute'])
            add.add_record()
        elif x['type'] == 'Announcement':
            anounce = AddAnnouncement(x['text'], x['attribute'])
            anounce.add_record()


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
        file_type = input('Enter file format\n')
        file = input('Enter file name\n')
        records_num = int(input('Enter the number of records\n'))
        readfile = ReadFile(file, records_num)
        if file_type == 'json':
            a = readfile.read_json()
        elif file_type == 'xml':
            a = readfile.read_xml()
        else:
            a = readfile.read_txt()
        add_record_from_file(a)


while True:
    marker = int(input('Select type of record. 1 - News, 2 - Ad, 3 - Announcement, 4 - Upload from file, 5 - For Exit:\n'))
    if marker != 5:
        check_type(marker)
    else:
        sys.exit()
