# Arithmetic Operators
num1 = 10
num2 = 20
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)
print("END")
print()

# RELATIONAL OPERATIONS
print(num1 < num2)
print(num1 > num2)
print(num1 == num2)
print(num1 != num2)
print("END")
print()

# LOGICAL OPERATIONS
log1 = True
log2 = False
print("END")
print()

# &
print(log1 & log2)
print(log2 & log1)
print(log2 & log2)
print(log1 & log1)
print("END")
print()

# |
print(log1 | log2)
print(log2 | log1)
print(log2 | log2)
print(log1 | log1)
print("END")
print()

# stings
my_string = "My name is Jhon"
print(my_string[0])
my_string = "My name is Jhon"
print(my_string[-1])
print("END")
print()

print(len(my_string))
print(my_string.lower())
print(my_string.upper())
print(my_string.replace('Jhon', 'Tom'))
print(my_string.count('is'))
print("END")
print()

# stings
fruit = "I like apples, mangoes, bananas"
print(fruit)
print(fruit.split(' '))
print("END")
print()

# lists
l1 = [1, "a", True]
print(l1)
print(type(l1))
print("END")
print()

# lists
l1 = [1, 'a', 2, 'b', 3, 'c']
print(l1)
print(type(l1))
print(l1[2:5])
print("END")
print()

# lists
l1 = ["apples", "mangoes", "bananas"]
print(l1)
l1[0] = "Fruit"
print(l1)
l1.append("Sparta")
print(l1)
l1.pop()
print(l1)
l1.reverse()
print(l1)
l1.insert(1, "Sparta")
print(l1)
l1.sort()
print(l1)
print("END")
print()

# lists
l1 = [1, 2, 3]
l2 = ["a", "b", "c"]
print(l1 + l2)
print("END")
print()
l1 = [1, "a", True]
print(l1 * 3)
print("END")
print()

# Tuple
tup1 = (1, "Sparta", True)
print(tup1)
print(type(tup1))

tup2 = (1, "a", True, 2, "b", False)
print(tup2)
# to find the length of the tuple
print(len(tup2))
# to add or multiply or do both at the same time
print(tup1 + tup2)
print()
print(tup1 * 3)
print()
print(tup1 * 3 + tup2)
print()
# to find out the maximum and minimum values of a tuple
tup1 = (1, 2, 3, 4, 5, 6)
print(min(tup1))
print(max(tup1))
print("END")
print()

# Dictionary
Fruits = {"Mango": 10, "Apple": 20, "Litchi": 30, "Blueberry": 40}
print(Fruits)
print(type(Fruits))

# separating keys and values
print(Fruits.keys())
print(Fruits.values())
print()

# adding or changing an existing element
Fruits["Banana"] = 50
print(Fruits)
Fruits["Apple"] = 60
print(Fruits)
print()

# adding two dictionaries
fruit1 = {"Mango": 100, "Apple": 200}
fruit2 = {"Litchi": 300, "Blueberry": 400}
fruit1.update(fruit2)
print(fruit1)

# removing an element from a dictionary
fruit1.pop("Blueberry")
print(fruit1)
print()
