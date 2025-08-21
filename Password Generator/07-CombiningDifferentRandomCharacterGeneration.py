import random
import string

letters = string.ascii_letters
digits = string.digits
special = string.punctuation

print("Random letters: ", end="")
for _ in range(5):
    print(random.choice(letters), end="")
print()

print("Random digits: ", end="")
for _ in range(5):
    print(random.choice(digits), end="")
print()

print("Random punctuation: ", end="")
for _ in range(5):
    print(random.choice(special), end="")
print()
