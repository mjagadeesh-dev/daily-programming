#removing spaces from a string
s=input("Enter a string:")
res=""
for i in s:
    if i==" ":
        pass
    else:res=res+i
print(res)

#string words reverse
s=input("Enter a string:").split()
rev=""
for i in s:
    rev=i+' '+rev
print(rev)


#invoking a function through variable
def addition(a,b):
    c=a+b
    print(c)
a=addition
a(2,4)

#accessing and modifying the global variable inside a function
a=20
def fun1():
    global a
    a=10
    b=20
    print(a+b)
def fun2():
    global a
    a=30
    b=3
    print(a+b)
print("a value outside the function:",a)
fun1()
print("a value inside fun1:",a)
fun2()
print("a value inside fun2:",a)

#nested function
def fun1():
    a=2
    b=4
    print(a+b)
    def fun2():
        print("fun1 executed")
    fun2()
fun1()

#higher order function
def fun1():
    print("Inside fun1")
def fun2(fun):
    print("inside fun2")
    fun()
    print("fun1 executed")
fun2(fun1)

#accessing and modifying the nonlocal local variable
def fun1():
    a=10
    b=29
    print(a)
    def fun2():
        nonlocal a
        a=50
        print(a)
    print(a)
    fun2()
    print(a)
fun1()

#closure in python
def outer():
    print("outer function")
    def inner():
        print("inner function")
    return inner
res=outer()
res()

#Decorator
def main():
    s=input("Enter a string:")
    return s
def outter(ptr):
    print("outer function")
    def inner():
        res=ptr()
        ans=res.upper()
        print(ans)
    return inner
r=outter(main)
r() 