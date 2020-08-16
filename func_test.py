from .func_speed import time, speed, distance


def test_speed_calculation():
    assert speed(100, 1) == 100


def test_time_calculation():
    assert time(10, 5) == 2


def test_distance_calculation():
    assert distance(60, 4) == 240
