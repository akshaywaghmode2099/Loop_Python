#read a number from user and display addition of it's digits

#input
#1234
#output
#10

n=int(input("Enter a number"))
sum=0;
while n>0:
    sum=sum+n%10;
    n=n//10;

print("Addition of digits is ",sum);

