#write python script to display pattern like below
'''
1
2 3
4 5 6

'''

n=int(input("Enter no of lines"))
k=1
for i in range(1,n+1):

    for x in range(1,i+1):
        print(k,end=" ")
        k=k+1
    print()
        
