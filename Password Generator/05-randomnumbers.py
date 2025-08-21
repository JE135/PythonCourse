import random
import string

digits = string.digits

print("Random digits: ", end="")
for _ in range(5):
    print(random.choice(digits), end="")