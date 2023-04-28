#read a number from user and display addition of factors.


n=int(input("Enter a Number"))
sum=0
print("Factors of ",n," are:")
for i in range(1,n+1):
    if n%i==0:
        print(i)
        sum=sum+i;

print("Addition of factors is ",sum);
