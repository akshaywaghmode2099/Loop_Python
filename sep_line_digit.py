#read a number from user and its digits in reverse order on separate line
#input
# 543
#output
#3
#4
#5


n=int(input("Enter a number"))
while n>0:
    print(n%10);
    n=n//10;

    



