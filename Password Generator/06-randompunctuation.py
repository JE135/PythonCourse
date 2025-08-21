import random
import string

special = string.punctuation

print("Random punctuation: ", end="")
for _ in range(5):
    print(random.choice(special), end="")