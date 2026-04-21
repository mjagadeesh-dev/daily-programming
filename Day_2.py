#oops
#Inheritance
class A:
    def __init__(self, x):
        self.x=x
class B(A):
    def __init__(self, x, y):
        A.__init__(self, x)
        self.y=y
class c(B):
    def __init__(self, x, y, z):
        B.__init__(self, x, y)
        self.z=z
    def calculate(self):
        return self.x+self.y+self.z
c1=c(30,2,10)
res=c1.calculate()
print(res)

#super method
class A:
    def __init__(self, x):
        self.x=x
class B(A):
    def __init__(self, x, y):
        super().__init__(x)
        self.y=y
class c(B):
    def __init__(self, x, y , z):
        super().__init__(x, y)
        self.z=z
    def calculate(self):
        return self.x+self.y+self.z
c1=c(1,2,3)
res=c1.calculate()
print(res)

class A:
    def hunnt(self):
        print("hunting")
class B(A):
    pass
class c(A):
    pass
b1=B()
b2=c()
b1.hunnt()
b2.hunnt()
#single level inheritance
class A:
    def display_A(self):
        print("This is class A")
class B(A):
    def display_B(self):
        print("This is class B")
c1=B()
c1.display_A()
c1.display_B()

#multilevel inheritance
class A:
    def display_A(self):
        print("This is class A")
class B(A):
    def display_B(self):
        print("This is class B")
class c(B):
    def display_c(self):
        print("This is class c")
c1=c()
c1.display_A()
c1.display_B()
c1.display_c()

#Hierarchical inheritance
class A:
    def disp_a(self):
        print("class A")
class B(A):
    def disp_b(self):
        print("class B")
class C(A):
    def disp_c(self):
        print("class C")
c1=B()
c2=C()
c1.disp_a()
c1.disp_b()
c2.disp_c()
c2.disp_a()

#Multiple inheritance
class Bike:
    def drift(self):
        print("Bike is drifting")
class Car:
    def race(self):
        print("Car is in race")
class B(Bike,Car):
    def disp(self):
        print("combine bike and car")
c1=B()
c1.disp()
c1.race()
c1.drift()
#Hybrid inheritance
class A:
    def dis_a(self):
        print("inside a")
class B(A):
    def dis_b(self):
        print("inside b")
class C(A):
    def dis_c(self):
        print("inside c")
class D(B,C):
    def dis_d(self):
        print("inside d")
c1=D()
c1.dis_a()
c1.dis_b()
c1.dis_c()
c1.dis_d()

#Encapsulation
class Bank:
    def __init__(self, balance):
        self.__balance=balance
    def deposit(self,amount):
        self.__balance+=amount
    def withdraw(self,amount):
        if self.__balance>=amount:
            self.__balance-=amount
            print("Withdrawal successful....")
        else:
            print("Insufficient balance!...")
            
    def get_balance(self):
        print("Current balance: ",self.__balance)
b1=Bank(1000)
b1.get_balance()
b1.deposit(600)
b1.get_balance()
b1.withdraw(500)
b1.get_balance()
#example 2 using setter and getter
class Book:
    def __init__(self,number):
        self.__pages=number
    def setter(self,val):
        if val>0:
            self.__pages=val
        else:print("invalid value")
    def getter(self):
        return self.__pages
b1=Book(100)
res=b1.getter()
print(res)
b1.setter(-2)
res=b1.getter()
print(res)
b1.setter(200)
res=b1.getter()
print(res)

#Encapsulation using property function
class Person:
    def __init__(self):
        self.__uName=""
    def setter(self,name):
        self.__uName=name
    def getter(self):
        return self.__uName
    getset=property(getter,setter)
p1=Person()
p1.getset="Jagadeesh"
res=p1.getset
print(res)

#encapsulation using property decorator
class Person:
    def __init__(self):
        self.__uName=""
    @property
    def data(self):
        return self.__uName
    @data.setter
    def data(self,name):
        self.__uName=name
p1=Person()
p1.data="Jagadeesh"
res=p1.data
print(res)

#converting a public method to private method
class A:
    def __init__(self):
        self.__data=0
    def public_method(self):
        print("This is a public method")
        self.__private_method()
    def __private_method(self):
        print("This is a private method")
a1=A()
a1.public_method()
a1._A__private_method()
class Bike:
    def __init__(self):
        self.__brand="BMW"
    def get_brand(self):
        print(self.__brand)
    def __move(self):
        print("Bike is moving")
b1=Bike()
b1.get_brand()


