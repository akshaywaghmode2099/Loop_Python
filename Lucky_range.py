#lucky Number

for n in range(1000,1000):
    cn=n;
    while n>9:
        sum=0;
        while n>0:
            sum=sum+n%10
            n=n//10;
        if sum>9:
            n=sum;

    ld=cn%10;
    if ld==sum:
        print(cn)
    
    
