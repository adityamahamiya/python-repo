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
# Set operations
s1 = {1, "a", True, 2, "b", False}
print(s1)
# to add one single element
s1.add("Hello")
print(s1)
# to add multiple elements
s1.update([10, 20, 30])
print(s1)
print()
# to remove elements
s1.remove(False)
print(s1)
print()
# for union of two sets
t1 = {1, 2, 3}
t2 = {4, 5, 6}
print(t1.union(t2))
j1 = {1, 2, 3, 4, 5}
j2 = {5, 6, 7, 1, 3}
print(j1.intersection(j2))
print()
# If statement
a = 10
b = 20
if a > b:
    print("a is greater than b")
else:
    print("b is greater than a")
print()
# elif
a = 10
b = 20
c = 30
if (a > b) & (a > c):
    print("a is the greatest")
if (b > a) & (b > c):
    print("b is the greatest")
if (c > a) & (c > b):
    print("c is the greatest")
print()
#  tuple with if
tup1 = (1, 2, 3, 4, 5)
if "a" in tup1:
    print("a is present in tup1")
else:
    print("a is not present in tup1")
print()
# if with lists
l1 = ["a", "b", "c"]
if l1[0] == "a":
    l1[0] = "z"
print(l1)
print()
# if with dictionary
d1 = {"k1": 10, "k2": 20, "k3": 30}
if d1["k1"] == 10:
    d1["k1"] = d1["k1"] + 100
print(d1)
# looping statements (simple for loop)
fruits = ["apple", "mango", "banana"]
for i in fruits:
    print(i)
print()
# nested for loop
color = ["blue", "black", "green", "yellow"]
item = ["book", "pencil", "ball", "chair"]
for i in color:
    for j in item:
        print(i, j)
print()
# Printing 1-10 while using loop
i = 1
while i <= 10:
    print(i)
    i = i + 1
print()
# printing 2-table with while loop
i = 1
n = 2
while i <= 10:
    print(n, " * ", i, " = ", n * i)
    i = i + 1
print()


# class
class Phone:
    def make_call(self):
        print("Making phone call")

    def play_game(self):
        print("Playing game")


p1 = Phone()
p1.make_call()
print()
p1.play_game()
print()


# adding parameters to the class
class Phone:
    def set_color(self, color):
        self.color = color

    def set_cost(self, cost):
        self.cost = cost

    def show_color(self):
        return self.color

    def show_cost(self):
        return self.cost

    def make_call(self):
        print("Making phone call")

    def play_game(self):
        print("Playing game")


p1 = Phone()

p1.set_color("blue")
p1.set_cost(999)
print(p1.show_color())
print(p1.show_cost())
print()


# class with a constructor
class Employee:
    def __init__(self, name, age, salary, gender):
        self.name = name
        self.age = age
        self.salary = salary
        self.gender = gender

    def employee_details(self):
        print("Name of the employee is ", self.name)
        print("Age of the employee is ", self.age)
        print("Salary of the employee is ", self.salary)
        print("Gender of the employee is ", self.gender)


# constructor example
e1 = Employee('Sam', 32, 85000, 'Male')
print(e1.employee_details())


# Inheritance (PARENT CLASS)
class Vehicle:
    def __init__(self, mileage, cost):
        self.mileage = mileage
        self.cost = cost

    def show_details(self):
        print("I am a Vehicle ")
        print("Mileage of the Vehicle is ", self.mileage)
        print("Cost of the Vehicle is ", self.cost)


v1 = Vehicle(500, 500)
print(v1.show_details())


# Inheritance (CHILD CLASS
class Car(Vehicle):
    def show_car(self):
        print("I am a car")


c1 = Car(200, 1200)
print(c1.show_details())
print(c1.show_car())


# Inheritance (SUPER Class)
class Car(Vehicle):
    def __init__(self, mileage, cost, tyres, hp):
        super().__init__(mileage, cost)
        self.tyres = tyres
        self.hp = hp

    def show_car_details(self):
        print("I am a Car ")
        print("Number of tyres are ", self.tyres)
        print("Value of horse power is ", self.hp)


c1 = Car(20, 12000, 4, 300)
print(c1.show_details())
print(c1.show_car_details())
print()


# inheritance (MULTIPLE)
class Parent1():
    def assign_string_one(self, str1):
        self.str1 = str1

    def show_string_one(self):
        return self.str1


class Parent2():
    def assign_string_two(self, str2):
        self.str2 = str2

    def show_string_two(self):
        return self.str2


class Derived(Parent1, Parent2):
    def assign_string_three(self, str3):
        self.str3 = str3

    def show_string_three(self):
        return self.str3


d1 = Derived()
d1.assign_string_one("one")
d1.assign_string_two("Two")
d1.assign_string_three("Three")
print(d1.show_string_one())
print(d1.show_string_two())
print(d1.show_string_three())
print()


# inheritance (MULTI lvl)
class Parent():
    def assign_name(self, name):
        self.name = name

    def show_name(self):
        return self.name


class Child(Parent):
    def assign_age(self, age):
        self.age = age

    def show_age(self):
        return self.age


class GrandChild(Child):
    def assign_gender(self, gender):
        self.gender = gender

    def show_gender(self):
        return self.name


gc = GrandChild()
gc.assign_name("Bob")
gc.assign_age("52")
gc.assign_gender("Male")
print(gc.show_name())
print(gc.show_age())
print(gc.show_gender())
print()
# NumPy (SINGLE DIMENSIONAL ARRAY)
import numpy as np

n1 = np.array([10, 20, 30, 40])
print(n1)
print()
print(type(n1))
print()
import numpy as np

n2 = np.array([[10, 20, 30, 40], [40, 30, 20, 10]])
print(n2)
print()
# numpy with zeros
import numpy as np

n1 = np.zeros((1, 2))
print(n1)
print()
import numpy as np

n1 = np.zeros((5, 5))
print(n1)
print()
# NumPy with same number
import numpy as np

n1 = np.full((2, 2), 10)
print(n1)
print()
# NumPy with arrange
import numpy as np

n1 = np.arange(10, 20)
print(n1)
print()
import numpy as np

n1 = np.arange(10, 50, 5)
print(n1)
print()
# NumPy with random numbers
import numpy as np

n1 = np.random.randint(1, 100, 5)
print(n1)
print()
# NumPy with shapes
import numpy as np

n1 = np.array([[1, 2, 3], [4, 5, 6]])
print(n1.shape)
print()
n1.shape = (3, 2)
print(n1)
print()
# Joining NumPy
import numpy as np

n1 = np.array([10, 20, 30])
n2 = np.array([40, 50, 60])
print(np.vstack((n1, n2)))
print()
print(np.hstack((n1, n2)))
print()
print(np.column_stack((n1, n2)))
print()
import numpy as np

n1 = np.array([10, 20, 30, 40, 50])
n2 = np.array([40, 50, 60, 70, 80])
print(np.intersect1d(n1, n2))
print()
print(np.setdiff1d(n1, n2))
print()
print(np.setdiff1d(n2, n1))
print()
# addition in NumPy (BASIC)
import numpy as np

n1 = np.array([10, 20, 30])
n1 = n1 + 1
print(n1)
print()
import numpy as np

n1 = np.array([10, 20, 30])
n1 = n1 - 1
print(n1)
print()
import numpy as np

n1 = np.array([10, 20, 30])
n1 = n1 * 2
print(n1)
print()
import numpy as np

n1 = np.array([10, 20, 30])
n1 = n1 / 2
print(n1)
print()
# MEAN
import numpy as np

n1 = np.array([10, 20, 30, 40, 50, 60])
print(np.mean(n1))
print()
# median
import numpy as np

n1 = np.array([11, 44, 5, 96, 67, 85])
print(np.median(n1))
print()
# standard deviation
import numpy as np

n1 = np.array([1, 5, 3, 100, 4, 48])
print(np.std(n1))
print()
# NumPy Matrix
import numpy as np

n1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(n1)
print()
print(n1[0])
print()
print(n1[1])
print()
print(n1[:,1])
print()
print(n1[:,2])
