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
e1.employee_details()
print()


# Inheritance (PARENT CLASS)
class Vehicle:
    def __init__(self, mileage, cost):
        self.mileage = mileage
        self.cost = cost

    def show_details(self):
        print("I am a Vehicle ")
        print("Mileage of the Vehicle is ", self.mileage)
        print("Cost of the Vehicle is ", self.cost)


print()

v1 = Vehicle(500, 500)
v1.show_details()
print()
# Inheritance (CHILD CLASS
class Car(Vehicle):
    def show_car(self):
        print("I am a car")


c1 = Car(200, 1200)
(c1.show_details())
(c1.show_car())
print()


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
c1.show_details()
c1.show_car_details()
print()


# inheritance (MULTIPLE)
class Parent1:
    def assign_string_one(self, str1):
        self.str1 = str1

    def show_string_one(self):
        return self.str1


class Parent2:
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
class Parent:
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
