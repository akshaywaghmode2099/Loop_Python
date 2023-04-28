#read a number from user and check whether it is armstrong  or not

n=int(input("Enter a number"));

cnt=0;
cn=n;
while n>0:
    cnt+=1 #cnt=cnt+1
    n=n//10

n=cn
sum=0;
while n>0:
    rm=n%10;
    sum=sum+rm**cnt
    n=n//10;

if sum==cn:
    print(cn,"is an armstrong number");
else:
    print(cn,"is not an armstrong number");

