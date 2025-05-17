from mydb import MyDb

# conn = None
# cur = None

# def setup_module(module):
#     global conn
#     global cur
#     db = MyDb()
#     conn = db.connect("server")
#     cur = conn.cursor()
# def teardown_module(module):
#     cur.close()
#     conn.close()
# #basic idea
# def test_johns_id():
#     id = cur.execute( "select id from employee_db where name=John")
#     assert id == 123

# def test_toms_id():
#     id = cur.execute( "select id from employee_db where name=Tom")
#     assert id == 789

#using fixtures

import pytest

@pytest.fixture(scope="module")

def cur():
    print("setting up")
    db = MyDb()
    conn = db.connect("server")
    cur = conn.cursor()
    yield cur
    cur.close()
    conn.close()
    print("closing database")

def test_johns_id(cur):
    id = cur.execute( "select id from employee_db where name=John")
    assert id == 123

def test_toms_id(cur):
    id = cur.execute( "select id from employee_db where name=Tom")
    assert id == 789

# pytest --capture=no or  pytest -v --capture=no

