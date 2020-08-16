from gitactions import functions


def test_speed_calculation():
    assert functions.speed(100, 1) == 100


def test_time_calculation():
    assert functions.time(10, 5) == 2


def test_distance_calculation():
    assert functions.distance(60, 4) == 240
