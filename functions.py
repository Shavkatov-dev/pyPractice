''' FUNCTIONS
(1) DEFINE vs CALL
(2) Parameters vs Arguments
(3) Keyword and Default Arguments
(4) Scope
'''

print('======= DEFINE(parameters) vs CALL (arguments) ==========')

# built-in functions > type() input() print() len() str() int() bool()
# functions - reusable blocks of code that perform a specific task
# Instead of bloack {} in Java, we use indentation in Python to define a function!


# DEFINE - build
def greet(a):
    # pass - hech bulmaganda, bizga xatolik bermasligi uchun ishlatiladi
    print(f"Hello, {a}! Welcome to Python!")


def greeting(b):
    print(f"greeeting is executed")
    return f"Hello, {b}! Welcome to Python!"


# CALL - execute
result1 = greet("Alice")
# None, chunki biz hech narsa return qilmaganmiz, shuning uchun default qiymat None boladi
print("the result 1: ", result1)

result2 = greeting("Bob")
print("the result 2: ", result2)
