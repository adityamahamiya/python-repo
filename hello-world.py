# Arithmetic Operators
num1 = 10
num2 = 20
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)

# RELATIONAL OPERATIONS
print(num1 < num2)
print(num1 > num2)
print(num1 == num2)
print(num1 != num2)

# LOGIACL OPERATIONS
log1 = True
log2 = False

# &
print(log1 & log2)
print(log2 & log1)
print(log2 & log2)
print(log1 & log1)

# |
print(log1 | log2)
print(log2 | log1)
print(log2 | log2)
print(log1 | log1)

# stings
my_string = "My name is Jhon"
print(my_string[0])
my_string = "My name is Jhon"
print(my_string[-1])

print(len(my_string))
print(my_string.lower())
print(my_string.upper())
print(my_string.replace('Jhon', 'Tom'))
print(my_string.count('is'))

# stings
fruit = "I like apples, mangoes, bananas"
print(fruit)
print(fruit.split(' '))

# lists
l1 = [1, "a", True]
print(l1)
print(type(l1))

# lists
l1 = [1, 'a', 2, 'b', 3, 'c']
print(l1)
print(type(l1))
print(l1[2:5])

# lists
l1 = [1, 'a', 2, 'b', 3, 'c']
print(l1)
l1[0] = 100
print(l1)
l1.append("Sparta")
print(l1)
l1.pop()
print(l1)
l1.reverse()
print(l1)
l1.insert(1,"Sparta")
print(l1)
l1.sort()
print(l1)

