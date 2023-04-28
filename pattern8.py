n=int(input("Enter no of lines "))

'''k=1
for i in range(n,0,-1):
    for j in range(k,n+1):
        print(j,end=" ")

    print()
    k=k+1
'''

for i in range(1,n+1):
    for j in range(i,n+1):
        print(j,end=" ")

    print()
