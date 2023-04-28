#read a number from user and display it's factorial
n=int(input("enter a number"))
f=1;
for i in range(2,n+1):
    f=f*i

print("Factorial of ",n,"is",f);

