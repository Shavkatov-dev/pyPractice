print("======= number ==========")

# in JAVA, variable is a name of storage location
# in Python, variable is a named reference!

count = 100
count_type = type(count)
print("count", count)
print(f'the count: {count} and type: {count_type}')

result1 = count.bit_count()  # method
result2 = count.numerator  # state
print(result1, result2)


print("======= string ==========")

# Methods: upper() lower() title() capitalize() swapcase() isupper() islower() istitle() - not mutable, returns new string


course = "AI Python FullStack"
result3 = type(course)
print(f"the result 1: {result3}")

result = course.title()  # har bir suz 1nchi harfini katta harf qilb beradi!!!
print(f"the result 2: {result}")

result = course.upper()
print(f"the result 3: {result}")

result = course.replace("FullStack", "MasterClass")
print(f"the result 4: {result}")


print("======= boolean ==========")

# functions > type() input() print() len() str() int() bool()

y = input("Give your value for y:")
print("y:", y)

result = y.isnumeric()  # stringning faqat raqamlardan tashkil topganligini tekshiradi
print(f"the input value is numeric: {result}")

# FALSY > 0, 0.0, "", [], {}, set(), None, False
# TRUTHY > 1, -1, 0.1, " ", [0], {0:0}, set(0), True
test_falsy = "" or False or None or 0
print("The Falsy: ", bool(test_falsy))

test_truhty = "MIT" and True and 1
print("The Truthy: ", bool(test_truhty))
