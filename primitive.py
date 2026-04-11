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
