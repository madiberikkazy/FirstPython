'''
a = 3
b = a
a = 5
print(b)

x = 3
y = 4
x = y + 2
x = x + 1
print(x)
# x=x+1 равно x+=1

q = 4
if q > 0 :
    print(q)
while q > 0 :
    print(q)
'''


def cdown(n):
    while n > 0:
        print(n)
        n -= 1
    print("Ramo")


cdown(8)


def cdown(n):
    while n < 24:
        print(n)
        n += 1
    print("Ramo")
cdown(1)

for r in range(24):
    print(r)

for r in range(11):
    print(r)

for x in range(10, -1, -1):
    print(x)

for q in range(2, 33, 2):
    print(q)

for s in range(1, 33, 2):
    print(s)

w = 1
while w > 0:
    print(w)
    w += 1
    if w == 10:
        break

for d in range(20, 35, 2):
    print(d)

a = int(input("Enter number : "))
for x in range(10, a):
    print(a ** 2)

def n(x):
    b = 1
    for i in range(1,x+1):
        b = b*i
    print(b)
n(5)