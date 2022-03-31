x = 33.0
print(type(x))

m = 33
print(type(int(m)))

import math

a = math.cos(math.degrees(60))
print(a)


def Ramo():
    print("Ramo Producer")


Ramo()


def x1():
    x2()
    print(1)


def x2():
    print(2)


def x3():
    print(3)
    x1()


x3()


def Enemy(enemy):
    print("Enemy name is", enemy)


Enemy("Lazy")


def SNF(snf):
    print("My SNF is ", snf)


SNF("Koshekbai Ramazan Abayuly")


def MI(mi):
    print("My mother name is ", mi)


MI("Aksaule")