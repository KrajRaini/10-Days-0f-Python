#making a calculator using user input

print("Enter the two numbers")
num1=int(input())
num2=int(input())

print("""Enter the operation you wanted to do
1.Add
2.Sub
3.Mul
4.Div""")
a=int(input())
if a==1:
    print(num1+num2)
elif a==2: 
    print(num1-num2)
elif a==3: 
    print(num1*num2)
elif a==4: 
    print(num1/num2)
