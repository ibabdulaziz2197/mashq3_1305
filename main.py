# 1
class Student:
    def __init__(self, fullname, grade):
        self.fullname = fullname
        self.__grade = grade

    def get_grade(self):
        return self.__grade

    def set_grade(self, new_grade):
        self.__grade = new_grade


s1 = Student('Ali Valiyev', 4)

print(s1.fullname)

grade = s1.get_grade()
print(grade)

s1.set_grade(5)
print(s1.get_grade())

# 2
class Car:
    def __init__(self, name, price):
        self.name = name
        self.__price = price


    def get_price(self):
        return self.__price


    def set_price(self, new_price):
        self.__price = new_price



c1 = Car('BMW', 45000)


print(c1.name)
print(c1.get_price())


c1.set_price(50000)


print(c1.get_price())


# 2
class Phone:
    def __init__(self, model, battery):
        self.model = model
        self.__battery = battery


    def get_battery(self):
        return self.__battery


    def set_battery(self, new_battery):
        self.__battery = new_battery



p1 = Phone('iPhone 15', 90)


print(p1.model)
print(p1.get_battery())


p1.set_battery(100)


print(p1.get_battery())

3
class Phone:
    def __init__(self, model, battery):
        self.model = model
        self.__battery = battery


    def get_battery(self):
        return self.__battery


    def set_battery(self, new_battery):
        self.__battery = new_battery



p1 = Phone('iPhone 15', 90)


print(p1.model)
print(p1.get_battery())


p1.set_battery(100)


print(p1.get_battery())
