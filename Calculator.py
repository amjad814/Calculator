print("Simple Calculator")
print("Selection operation: +  -  *  /")

num1 = float(input("enter 1st number:"))
operator =("+", "-", "*", "/")
op = input("enter operator:")
num2 = float(input("enter 2nd number:"))
if (op == "+"):
    print("result:", num1 + num2)

elif(op =="-" ):
    print("result:", num1 - num2)

elif(op =="*" ):
    print("result:", num1 * num2)

elif(op =="/" ):
    if num2 != 0 :
        print("result:", num1 / num2)
    
else:
    print("error")