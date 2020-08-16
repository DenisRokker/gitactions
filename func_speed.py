from mimesis import Person

person = Person("ru")


def name():
    n = person.full_name()
    return n


def speed(s, t):
    v = s/t
    return v


def distance(v, t):
    s = v * t
    return s


def time(s, v):
    t = s / v
    return t
