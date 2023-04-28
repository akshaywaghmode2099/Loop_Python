#read a number from user and check whether it is prime or not


n=int(input("Enter a number"))

cnt=0;
for i in range(2,n//2+1):
    if n%i==0:
        break;
else:
    print(n,"is prime")

if i<n//2:
    print(n,"is not Prime")
    
