# class name:
#     name = "mihir"

# class marks(name):
#     def __init__(self, math, phy, cham):
#         self.math = math
#         self.phy = phy
#         self.cham = cham
#         self.percentage = str((self.math + self.phy + self.cham) / 3) + " %"

    
# s1 = marks(90,98,80)
# print(s1.name)
# print(s1.percentage)


# class methods

# class Student:
#     name = "mihir"

#     @classmethod
#     def changeName(cls,name):
#         cls.name = name

# s1 = Student()
# s1.changeName("sita raam")
# print(s1.name)
# print(Student.name)


# complex numbers
# class Complex:
#     def __init__(self, real, img):
#         self.real = real
#         self.img = img
        
#     def showNumbers(self):
#         print(self.real, "i +", self.img, "j")

#     def __add__(self, num2):
#         newReal = self.real + num2.real
#         newImg = self.img + num2.img
#         return Complex(newReal, newImg)
    
#     def __sub__(self,num2):
#         newreal = self.real - num2.real
#         newimg = self.img - num2.img
#         return Complex(newreal, newimg)


# num1 = Complex(12,4)
# num1.showNumbers()

# num2 = Complex(2,5)
# num2.showNumbers()

# # num3 = num1 + num2
# # num3.showNumbers()

# num4 = num1 - num2
# num4.showNumbers()


# circle class
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return (22/7) * self.radius ** 2
    
#     def perimeter(self):
#         return 2 * (22/7) * self.radius
    
# c1 = Circle(20)

# print(c1.area())
# print(c1.perimeter())

# class Employee():
#     def __init__(self, role,department, salary):
#         self.role = role
#         self.depaetment = department
#         self.salary = salary

#     def showEmployee(self):
#         return print(self.role, self.depaetment, self.salary)
    
# class Engineer(Employee):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         super().__init__("dj", "finance", "80,000")

# enn1 = Engineer("raghu", 34)
# enn1.showEmployee()



class Order:
    def __init__(self , items , price):
        self.items = items
        self.price = price

    def __gt__(self, ord2):
        return self.price > ord2.price

odr1 = Order("wefer", 40)
odr2 = Order("coffee", 20)

print(odr1 > odr2)