#read a number from user and display its factorial using while loop

n=int(input("Enter a number"))

i=1;
f=1;
while i<=n:
    f=f*i;
    i=i+1;

print("Fatorial of ",n,"is",f);
