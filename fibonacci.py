#Fibonacci by 

a=0
b=1
i=0
c=0
for i in range(1,2000): #Change the second number to calculate to that set number
    c=b
    b+=a
    a=c
    print(i,b)
