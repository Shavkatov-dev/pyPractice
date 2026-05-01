''' OBJECTS
    (1) What is object
    (2) Iterable objects & RANGE
    (3) DICTIONARY
    (4) Error handling system
'''

import array  # package/module
import math
from math import ceil, asin
print("======= What is object =======")
# An object has state and method properties.
# Everything is object in Python!

print(type('HJello World!'))
print(type(100))
print(type(True))
print(type(array))
print(type(math))


# Paradigm > Functional Programming & OOP

# OOP 4 concepts > Abstraction | Encapsulation | Inheritance | Polimorphism
result1 = math.ceil(97.7)  # CALL
print(f'result1: {result1}')
result2 = ceil(98.3)
print(f'result2: {result2}')


print("======= Error handling system =======")

car_dict = dict(name="Toyota", year=2026, electric=True)

try:
    print("passsed here")
    a = car_dict.speed
    result = car_dict["origin"]
    print("result:", result)
except Exception as err:
    print("General Error:", err)
# except KeyError as err:
#   print("No origin state found here:", err)
# except AttributeError as err:
#    print("No speed found here:", err)
else:  # umuman xatolik bumaganda ishga tushadi
    print("Executed successfully without errors")
finally:  # har qanday holatda eng oxirida ishga tushadi
    print("Final closing logic")
