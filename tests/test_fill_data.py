import pytest
from pony.orm import *

from models.hotel_data import RoomType
from populate_database.base_populate import set_rooms_types, set_cities


def setup_module(module):
    print("Module SetUp: populate database")
    set_rooms_types()
    set_cities()


@db_session
def test_room_type(global_setup):
    assert RoomType.get(description="Triple").max_person, 3


@db_session
def test_total_room_types(global_setup):
    total_room_type = select(c for c in RoomType)
    assert total_room_type, 4
