n=int(input("Enter no of lines "))
e=2
o=1
for i in range(1,n+1):
    for j in range(1,i+1):
        if i%2==0:
            print(e,end=" ")
            e=e+2
        else:
            print(o,end=" ")
            o=o+2

    print()
