import sqlite3
import math
import sys


class DbUpdate:
    def __init__(self, cities, row):
        with sqlite3.connect("coordinates.db") as self.conn:
            self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS 'Cities' (City varchar(255), Latitude float, Longitude float)")
        self.row = row
        self.cities = cities

    def select(self):
        self.cur.execute(f"SELECT City, Latitude, Longitude FROM Cities WHERE City = '{self.cities[0]}' OR City = '{self.cities[1]}'")
        return self.cur.fetchall()

    def insert(self):
        self.cur.execute(f"INSERT INTO Cities (City, Latitude, Longitude) VALUES ({self.row})")
        self.conn.commit()


def degrees_to_radians(degrees):
    return degrees * math.pi / 180


def calculate_distance(lat1, lon1, lat2, lon2):
    earth_radius = 6371

    dlat = degrees_to_radians(lat2 - lat1)
    dlon = degrees_to_radians(lon2 - lon1)

    lat1 = degrees_to_radians(lat1)
    lat2 = degrees_to_radians(lat2)

    a = math.sin(dlat / 2) * math.sin(dlat / 2) + math.sin(dlon / 2) * math.sin(dlon / 2) * math.cos(lat1) * math.cos(lat2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return earth_radius * c


def get_coords_and_calculate(cities):
    a = DbUpdate(cities=cities, row=None)
    check_db = a.select()
    if len(check_db) == 2:
        return calculate_distance(check_db[0][1], check_db[0][2], check_db[1][1], check_db[1][2])
    elif len(check_db) == 1:
        if cities[0] == check_db[0][0]:
            coords = input(f"Enter {cities[1]} coordinates separated by comma\n").split(',')
            row = f"'{cities[1]}', '{coords[0]}', '{coords[1]}'"
        else:
            coords = input(f"Enter {cities[0]} coordinates separated by comma\n").split(',')
            row = f"'{cities[0]}', '{coords[0]}', '{coords[1]}'"
        b = DbUpdate(cities=None, row=row)
        b.insert()
        return calculate_distance(float(check_db[0][1]), float(check_db[0][2]), float(coords[0]), float(coords[1]))
    else:
        coords = input("Enter cities coordinates separated by comma\n").split(',')
        row1 = f"'{cities[0]}', '{coords[0]}', '{coords[1]}'"
        row2 = f"'{cities[1]}', '{coords[2]}', '{coords[3]}'"
        b = DbUpdate(cities=None, row=row1)
        c = DbUpdate(cities=None, row=row2)
        b.insert()
        c.insert()
        return calculate_distance(float(coords[0]), float(coords[1]), float(coords[2]), float(coords[3]))


while True:
    cities = input("Enter two cities separated by comma. To end the program, type 'exit'\n").split(',')
    if len(cities) == 2:
        res = get_coords_and_calculate(cities)
        print(res)
    elif len(cities) != 2:
        raise "Enter two cities"
    elif cities == 'exit':
        sys.exit()
