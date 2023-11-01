def table1(num1,num2):
    for j in range(num1,num2+1,1):  
        for i in range(1,11,1):
            print(j,i,i*j)
        print()
table1(500,502)
