import random
import string

letters = string.ascii_letters

print("Random letters: ", end="")
for _ in range(5):
    print(random.choice(letters), end="")