import random

min_val = int(input("Enter the lower bound: "))
max_val = int(input("Enter the higher bound: "))

random_number = random.randint(min_val, max_val)
print(random_number)