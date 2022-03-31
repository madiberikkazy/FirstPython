my_family = ["Aksaule", "Ramazan", "Aktorgai"]
print(my_family)
my_family[0] = "Anne"
print(my_family)

x = [1, 2, 3]
y = [4, 5, 6]
z = x + y
print(z)

q = [1, 2, 3, 4, 5, 6]
w = q[0:3]
q[2:3] = ["r", "z"]
print(q)

e = q[1:4] = ["r", "z"]
print(e)

t = ["a", "b", "c"]
t.append("d")
print(t)

t1 = ["x", "y", "z"]
t.extend(t1)
print(t)

group = ["Alnur", "Jomart", "Aidyn"]
group.sort(reverse=False)
print(group)

a = int(input())
b = a[0]
c = a[1]
d = int(b) + int(c)
if d >= 9 and d < 100:
    print("This number is two - digit number")
else:
    print("This number is not two - digit number")

a = input("")
b = a[0]
c = a[1]
if b > c:
    print("First number is bigger ")
if b < c:
    print("Second number is bigger ")
else:
    print("Both numbers are equal")