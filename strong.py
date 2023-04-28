#write a python script to read a number from user and
#check whether it is a strong number or not

n=int(input("Enter a Number"))
nc=n
sum=0;
while n>0:
    rm=n%10;
    i=1;
    f=1;
    while i<=rm:
        f=f*i;
        i=i+1;

    sum=sum+f;
    n=n//10

if nc==sum:
    print(nc,"is a strong number")
else:
    print(nc,"is not a strong number");
    

    
