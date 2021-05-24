from random import randint

wheel = [200, 300, 500, 1000, 100, 50, 0, -1, 200, 300, 500, 1000, 100, 50, 0, -1,]


def spin_wheel():
    return wheel[randint(0, len(wheel) -1)]

print(spin_wheel())