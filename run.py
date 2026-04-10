# Dunder __builtins__, __init__
message = "hello mate!!"
print(message)

result = type(message)
print(result)

''' In Python, there are buit-in tools:
(1) TYPES > int float str list dict
(2) FUNCTION > print() len() input() type() str() int()
(3) CONSTANTS > True False None

'''

print(dir(__builtins__))
