import math

number = float(input("Enter a number:"))
answer = math.sqrt(number)

print(answer)

#using multiples modules

import math
import random

def multiply_pi():
    return random.randint(1,10) * math.pi

for i in range(5):
    print(multiply_pi())

# In boss.py

def good_boss(name):
    print(name + " is a good boss!")

def bad_boss(name):
    print(name + " is a bad boss!")

def not_a_boss(name):
    print(name + " is not even a boss")
# In app.py
import boss

boss.bad_boss("Bill Steves")
