fruit = "banana"
letter = fruit[1]
print(letter)

# index - 0123456789
# len - 123456789

bad_bro = "Dias"
x = len(bad_bro)
print(x)

r = input()
print(r[-1])
print(r[0])
print(len(r))

word = input()
index = 0
while index < len(word):
    letter = word[index]
    print(letter)
    index = index + 1

word = "Ramo"
for letter in word:
    print(letter)

w = "Ramo Producer"
print(w[2:5])
print(w[:7])
print(w[4:])
print(w[-7:-1])