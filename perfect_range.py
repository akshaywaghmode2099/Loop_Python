#write a python script to print all the perfect numbers
#between 5 to 100

for n in range(5,10000):
    sum=0
    for i in range(1,n//2+1):
        if n%i==0:
            sum=sum+i;

    if sum==n:
        print(n);


    
            
