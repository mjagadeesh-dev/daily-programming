#has-a relationship
#comosion
class  Clg:
    def __init__(self,name,rno):
        self.sName=name
        self.sRno=rno
    def study(self):
        print("students are studying")
class City:
    def __init__(self,name,rno):
        self.cName="Adoni"
        self.c=Clg(name,rno)
c1=City("jagadeesh",24)
print(c1.cName)
print(c1.c.sName)
c1.c.study()
del c1
print(c1.cName)

#aggregation
#composition
class Charger:
    def __init__(self,brand):
        self.cbrand=brand
    def getCharger(self):
        print("charger is plugged in")
class Mobile:
    def __init__(self,name):
        self.mname=name
        self.c=''
    def mobile(self,ch):
        self.c=ch
c1=Charger("vivo")
m1=Mobile("IQOO")
m1.mobile(c1)
m1.c.getCharger()
print(m1.c.cbrand)
del m1
print(c1.cbrand)

#composition and aggregation
class Heart:
    def __init__(self,s):
        self.status=s
    def heart(self):
        print("Heart is beating")
class Bike:
    def __init__(self):
        self.name="BMW"
    def drift(self):
        print("bike is drifting")
class Person:
    def __init__(self,status):
        self.pName="Jagadeesh"
        self.h=Heart(status)
        self.c=""
    def run(self,c):
        print("person is running")
        self.c=c
b1=Bike()
p1=Person("Beating")
p1.run(b1)
print(p1.h.status)
p1.h.heart()
print(p1.c.name)
p1.c.drift()