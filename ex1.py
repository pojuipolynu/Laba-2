import json
import datetime
import random


class Ticket:
    def __init__(self, price, discount):
        self.price = price
        self.discount = discount
        self.number = random.randint(1000, 9999)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if not isinstance(value, int or float):
            raise Exception('Your price value is invalid')
        self.__price = value

    @property
    def discount(self):
        return self.__discount

    @discount.setter
    def discount(self, value):
        if not isinstance(value, int or float):
            raise Exception('Your discount value is invalid')
        self.__discount = value

    def discount_price(self):
        l = self.price - self.price * self.discount/100
        return l

    def construct_ticket(self):
        with open('ticketsfile.json', 'r') as openfile:
            jobject = json.load(openfile)
        for i in jobject['tickets']:
            if i['number'] == self.number:
                print(i)

    def __str__(self):
        return f'Your ticket: {self.number}\nPrice without discount: {self.price}\nPrice with discount:' \
               f'{self.discount_price()}'


class Regular(Ticket):
    title = 'Regular ticket'

    def __init__(self, price, discount=0):
        super().__init__(price, discount)


class Advance(Ticket):
    title = 'Advance ticket'

    def __init__(self, price, discount=40):
        super().__init__(price, discount)


class Student(Ticket):
    title = 'Student ticket'

    def __init__(self, price, discount=50):
        super().__init__(price, discount)


class Late(Ticket):
    title = 'Late ticket'

    def __init__(self, price, discount=-10):
        super().__init__(price, discount)


class Event:
    def __init__(self, name, day, month, year):
        self.name = name
        self.day = day
        self.month = month
        self.year = year
        self.date = datetime.date(year, month, day)

    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, d):
        if not isinstance(d, int) or not 1 <= d <= 31:
            raise Exception('Your day is invalid')
        self.__day = d

    @property
    def month(self):
        return self.__month

    @month.setter
    def month(self, m):
        if not isinstance(m, int) or not 1 <= m <= 12:
            raise Exception('Your month is invalid')
        self.__month = m

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, y):
        if not isinstance(y, int):
            raise Exception('Your year is invalid')
        self.__year = y

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise Exception('Your event name is invalid')
        self.__name = value

    def ticket_maker(self, type):
        k = datetime.date.today()
        n = (self.date - k).days
        if not isinstance(type, str) or (type != 'r' and type != 's'):
            raise Exception('Your data is invalid')
        if type == 's':
            return Student
        elif type == 'r' and n <= 10:
            return Late
        elif type == 'r' and n >= 60:
            return Advance
        elif type == 'r' and 10 < n < 60:
            return Regular

    def __str__(self):
        return f'Event: {self.name}\nDate: {self.date}\n'


def write_json(tlist):
    if not isinstance(tlist, list):
        raise TypeError
    tdict = []
    for i in tlist:
        tdict.append(i.__dict__)
    dictionary = {'tickets': tdict}
    with open("ticketsfile.json", "w") as outfile:
        json.dump(dictionary, outfile)


event1 = Event('Concert', 13, 9, 2023)
ticket1 = event1.ticket_maker('r')(500)
event2 = Event('Book club', 23, 12, 2022)
ticket2 = event2.ticket_maker('r')(400)
ticket3 = event2.ticket_maker('s')(400)
print(f'{event1}{ticket1}')
print(f'\n{event2}{ticket2}\n\n{ticket3}')
tickets = [ticket1, ticket2, ticket3]
write_json(tickets)
ticket1.construct_ticket()
