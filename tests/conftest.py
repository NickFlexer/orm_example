import pytest

from models import db


@pytest.yield_fixture(scope="session")
def global_setup():
    print("Global SetUp: Bind database and generate mapping")
    db_name = "test_db.db"
    db.bind(provider="sqlite", filename=db_name, create_db=True)
    db.generate_mapping(create_tables=True)

    yield

    print("Global TearDown: drop tables")
    db.drop_all_tables(with_all_data=True)
    db.disconnect()
