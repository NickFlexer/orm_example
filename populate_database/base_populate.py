from pony.orm import *

from models.hotel_data import RoomType, Cities


@db_session
def set_rooms_types():
    RoomType(max_person=1, description="Single")
    RoomType(max_person=2, description="Double")
    RoomType(max_person=3, description="Triple")
    RoomType(max_person=4, description="Quad")


@db_session
def set_cities():
    Cities(name="Будва")
    Cities(name="Бечичи")
    Cities(name="Рафаиловичи")
