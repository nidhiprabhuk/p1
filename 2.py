def table1(num1,num2):
    for j in range(num1,num2+1,1):  
        for i in range(1,11,1):
            print(j,i,i*j)
        print()
start=int(input("Enter the starting number: "))
end=int(input("Enter the ending number: "))
table1(start,end)
