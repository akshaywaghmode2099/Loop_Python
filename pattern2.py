#write python script to display pattern like below
'''
1
2 2
3 3 3
4 4 4 4
'''

n=int(input("Enter no of lines "))
for i in range(4):
    for j in range(i+1):
        print(i,end=" ")
    print()
