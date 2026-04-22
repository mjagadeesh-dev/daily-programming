#Recursion
#program for find factorial of a number
def fact(n):
    if n==0 or n==1:
        return 1
    return n*fact(n-1)
fact(5)

#program for sum of natural numbers
def sum_nat(n):
    if n==1:
        return 1
    return n+sum_nat(n-1)
sum_nat(3)

#program for check a string is palindrome or not
def palindrome(s,rev='',i=0):
    if i>=len(s):
        return ""
    return s[i]+palindrome(s,rev,i+1)
s="madam"
result=palindrome(s)
if s==result:
    print("palindrome")
else:print("not palindrome")

#revers a string usinng two pointer
def rev(s,i,j):
    if i>=j:
        return s
    s[i],s[j]=s[j],s[i]
    return rev(s,i+1,j-1)
s=input("Enter a strinng:")
result=rev(list(s),0,len(s)-1)
print(" ".join(result))
