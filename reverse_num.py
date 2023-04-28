
#read a number from user and display it in reverse order using loop
# input 234
#output 432

n=int(input("Enter a number"))
rev=0;
while n>0:
    rem=n%10;
    rev=rev*10+rem
    n=n//10;

print("Revese number is ",rev);

