#display sum of n natural numbers using for loop

n=int(input("Enter a number"))
sum=0
for x in range(1,n+1):
      sum=sum+x
print("sum of first",n,"natural numbers is",sum)
