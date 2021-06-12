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
n = 1
while n <= 12:
    print("Table of ", n)
    i = 1
    while i <= 10:
        print(n, " * ", i, " =  ", n * i)
        i = i + 1
    n = n + 1
