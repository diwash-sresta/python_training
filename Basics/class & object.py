# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     def greet(self):
#         return(f"Hello , my name is {self.name} and I'm {self.age} years old")

# # creating instances(objects) oft he person class
# person1 = Person("Alice", 30)
# person2 = Person("Bob",25)

# # Accessing instances variable and creating methods
# print(person1.name)
# print(person2.age)

# message = person1.greet()
# print(message)

# class Car:
#     wheels = 4  # class attribute

#     def __init__(self,make,model):
#         self.make = make
#         self.model = model

#     def info(self):
#         return(f"This car is manufactured by {self.make}. It is {self.model} model and has {self.wheels} wheels ")
    
# car1 = Car("Toyota", "Camry")
# car2 = Car("Ford","Ecosport")
# car3 = Car("Honda","Accord")

# message = car3.info()
# print(message)

# /////////////// Inheritance  ///////////////////////////
# single inheritance

# class Animal:
#     def speak(self):
#         return "Animal speaks"

# class Dog(Animal):
#     def bark(self):
#         return "Dog barks"
    
# my_dog = Dog()
# print(my_dog.speak())
# print(my_dog.bark())

# multiple inheritance

# class A :
#     def method_A(self):
#         return "Method A"
    
# class B :
#     def method_B(self):
#         return "Method B"

# class C(A, B):
#     def method_C(self):
#         return "Method C"
    
# obj_C = C()
# print(obj_C.method_A())
# print(obj_C.method_B())
# print(obj_C.method_C())

# multilevel inheritance

# class A :
#     def method_A(self):
#         return "Method A"
    
# class B(A) :
#     def method_B(self):
#         return "Method B"

# class C(B):
#     def method_C(self):
#         return "Method C"
    
# obj_C = C()
# print(obj_C.method_A())
# print(obj_C.method_B())
# print(obj_C.method_C())

# super()

# class Rectangle:
#     def area(self):
#         return self.length * self.width

# class Square(Rectangle):
#     def __init__(self, side_length):
#         self.length = side_length
#         self.width = side_length
#         super().__init__()

# square = Square(2)
# print(square.area())

class Area:
    pi = 3.14

    def sq_area(self):
        return self.length *self.width
    def rect_area(self):
        return self.length *self.width
    def cir_area(self):
        return self.pi *self.length**2
    def tri_area(self):
        return 0.5*self.base *self.height

class Square(Area):
    def __init__(self,side_length):
        self.length = side_length
        self.width = side_length
        super().__init__()

class Rectangle(Area):
    def __init__(self,length,width):
        self.length = length
        self.width = width
        super().__init__()
class Circle(Area):
    def __init__(self,radius):
        self.length = radius
        super().__init__()
class Triangle(Area):
    def __init__(self,base,height):
        self.base = base
        self.height = height
        super().__init__()
square = Square(4)
rectangle = Rectangle(4,4)
circle = Circle(5)
triangle = Triangle(4,5)

print(square.sq_area())
print(rectangle.rect_area())
print(circle.cir_area())
print(triangle.tri_area())