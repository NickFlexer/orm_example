from pony.orm import *

from models.hotel_data import RoomType, Cities, Hotels, Rooms
from populate_database.base_populate import set_rooms_types, set_cities


def setup_module(module):
    print("Module SetUp: populate database")
    set_rooms_types()
    set_cities()


@db_session
def teardown_module(module):
    print("Module Teardown: delete all data")
    Rooms.select().delete(bulk=True)
    RoomType.select().delete(bulk=True)
    Cities.select().delete(bulk=True)


@db_session
def test_room_type(global_setup):
    assert RoomType.get(description="Triple").max_person, 3


@db_session
def test_total_room_types(global_setup):
    total_room_type = select(c for c in RoomType)
    assert total_room_type, 4


@db_session
def test_add_hotel(global_setup):
    bechichi_city = Cities.get(name="Бечичи")
    Hotels(name="Звездочка", star_rating=3, city=bechichi_city)

    hotel = select(h for h in Hotels if h.city.name == "Бечичи")

    assert hotel.first().name, "Звездочка"


@db_session
def test_add_rooms(global_setup):
    Hotels(name="Пандора", star_rating=4, city=Cities.get(name="Рафаиловичи"))

    Rooms(hotel=Hotels.get(name="Пандора"), type=RoomType.get(max_person=3), price=55.10, is_booked=False)

    hotel_rooms = select(r for r in Rooms if r.hotel.name == "Пандора")

    assert len(hotel_rooms), 1
