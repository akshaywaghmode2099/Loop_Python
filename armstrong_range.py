
# Display all armstrong numbers in the range from 1 to 100000

print("Armstrong numbers in the range 1 to 100000 are:")
for n in range(1,100001):
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
        print(cn);
 

