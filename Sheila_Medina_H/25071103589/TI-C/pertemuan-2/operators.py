x = 15
y = 4

# Arithmetic Operators
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)

# Assignment Operators
z = 10
z += 5
z -= 3
z *= 2
z /= 4
z %= 3
z **= 2
z //= 2

numbers = [1, 2, 3, 4, 5]

if (count := len(numbers)) > 3:
    print(f"List has {count} elements")

# Comparison Operators
x = 5
y = 3

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

# Logical Operators
x = 5
print(x > 0 and x < 10)

x = 5
print(x < 5 or x > 10)

x = 5
print(not(x > 3 and x < 10))

# Identity Operators
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
print(x is y)
print(x == y)

x = ["apple", "banana"]
y = ["apple", "banana"]

print(x is not y)

x = [1, 2, 3]
y = [1, 2, 3]

print(x == y)
print(x is y)

# Membership Operators
text = "Hello World"

print("H" in text)
print("hello" in text)
print("z" not in text)

# Bitwise Operators
print(6 & 3)

#Operator precedence
print((6 + 3) - (6 + 3))