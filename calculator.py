"""
this is a program to calculate simple mathematical operations.
the operations are addition,subtraction,multiplication,and division.
"""
a=int(input("enter your first number:"))
b=int(input("enter your second number:"))
print("")
print("please follow the names for your operators. ")
print("for addition, please type add.")
print("for subtraction, please type subtract. ")
print("for multiplication, please type multiply.")
print("for division, please type divide")
print("to make sure the program works properly,please check the spelling carefully")
c=str(input("enter your operator:"))
#end of inputs.
#start of conditional statments and computing.
if c=="add":
    print("the sum is:", a+b )
elif c=="subtract":
    print("the difference is:", a-b)
elif c=="multiply":
    print("the product is:", a*b)    
elif c=="divide":
    print("the answer is:", a/b)    
else:
    print("invalid operator")
    print(" invalid operator")
