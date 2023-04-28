#read a number from user and display its factors
n=int(input("Enter a Number"))

print("Factors of ",n," are:")
for i in range(1,n+1):
    if n%i==0:
        print(i)


        
    
