from decimal import Decimal

from pony.orm import *


db = Database()


class RoomType(db.Entity):
    max_person = Required(int)
    description = Required(str, unique=True)
    rooms = Optional("Rooms")


class Cities(db.Entity):
    name = Required(str, unique=True)
    hotels = Set("Hotels")


class Hotels(db.Entity):
    name = Required(str, unique=True)
    star_rating = Required(int)
    city = Optional(Cities)
    rooms = Optional("Rooms")


class Rooms(db.Entity):
    hotel = Required("Hotels")
    type = Required("RoomType")
    price = Required(Decimal)
    is_booked = Required(bool)
