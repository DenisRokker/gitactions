from .func_speed import time, speed, distance, name
import psycopg2


def test_speed_calculation():
    assert speed(100, 1) == 100


def test_time_calculation():
    assert time(10, 5) == 2


def test_distance_calculation():
    assert distance(60, 4) == 240


def test_name():
    assert type(name()) == str


def test_create_table():
    connect = psycopg2.connect(dbname="postgres",
                               user="postgres",
                               password="postgres",
                               host='postgres')
    cursor = connect.cursor()

    cursor.execute('create table People('
                   'ID INT NOT NULL,'
                   'NAME TEXT,'
                   'AGE INT NOT NULL,'
                   'PRIMARY KEY (id));')

    cursor.execute("insert into People (id, name, age) values(1, 'Denis', 21);")
    cursor.execute("insert into People (id, name, age) values(2, 'not Denis', 16);")
    cursor.execute("insert into People (id, name, age) values(3, 'Denis', 66);")
    cursor.execute("insert into People (id, name, age) values(4, 'Denis', 38);")
    cursor.execute("insert into People (id, name, age) values(5, 'not Denis', 2);")

    cursor.execute("select * from People where name = 'Denis';")

    assert cursor.fetchall()
    cursor.execute('drop table People;')

    connect.commit()
    cursor.close()
    connect.close()
