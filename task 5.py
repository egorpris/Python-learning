class Publishing:
    file = open('news_feed', 'a')
    from datetime import date, datetime


class AddNews(Publishing):
    def __init__(self, text, city):
        self.text = text
        self.city = city

    def add_record(self, text, city):
        type = 'News'
        self.file.write(f"{type.ljust(40, '-')}\n{text}\n{city}, {AddNews.date.today()}\n\n")
        self.file.close()


class AddAdvertising(Publishing):
    def __init__(self, text, date):
        self.text = text
        self.date = date

    def add_adv(self, text, date):
        end_date = self.datetime.strptime(date, '%Y-%m-%d')
        days_to_end = abs(self.datetime.today() - end_date)
        type = 'Private Ad'
        self.file.write(f"{type.ljust(40, '-')}\n{text}\nActual until: {end_date}, {days_to_end.days} days left\n\n")
        self.file.close()


class AddAnnouncement(Publishing):
    def __init__(self, text, phone):
        self.text = text
        self.phone = phone

    def add_announcement(self, text, phone):
        type = 'Announcement'
        self.file.write(f"{type.ljust(40, '-')}\n{text}\nPhone: {phone}\n\n")
        self.file.close()


class CheckType(AddNews, AddAdvertising, AddAnnouncement):
    def __init__(self, text, city, date, phone, t=1):
        AddNews.__init__(self, text, city)
        AddAdvertising.__init__(self, text, date)
        AddAnnouncement.__init__(self, text, phone)
        self.t = t
        self.text = text
        self.city = city
        self.date = date
        self.phone = phone

    def check_type(self, t):
        if t == 1:
            self.text = input('What happened?\n')
            self.city = input('Where it happened?\n')
            AddNews.add_record(self, self.text, self.city)
        elif t == 2:
            self.text = input('What do you promote?\n')
            self.date = input('When is the last day of the ad?\n')
            AddAdvertising.add_adv(self, self.text, self.date)
        elif t == 3:
            self.text = input('What do you announce?\n')
            self.phone = input('What is your phone number?\n')
            AddAnnouncement.add_announcement(self, self.text, self.phone)


a = CheckType('text', 'city', 'date', 'phone', 1)
a.check_type(int(input('Select type of record. 1 - News, 2 - Ad, 3 - Announcement:\n')))
