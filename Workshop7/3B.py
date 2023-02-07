print("Calculator")
a= float(input("Enter a number"))
b= float(input("Enter another number"))
choice= int(input("What operation do you want? 1. Addition 2. Subtraction 3. Multiplication 4. Division 5. Truncated division 6. Modulus 7. Exponentiation"))
def add(a,b):
    """This funtion does addition"""
    print(format(a+b,'.2f'))
def sub(a,b):
    """This funtion does subtraction"""
    print(format(a-b,'.2f'))
def mul(a,b):
    """This funtion does multiplication"""
    print(format(a*b,'.2f'))
def div(a,b):
    """This funtion does division"""
    print(format(a/b,'.2f'))
def tdiv(a,b):
    """This funtion does truncated division"""
    print(a/b)
def mod(a,b):
    """This funtion finds modulus"""
    print(format(a%b,'.2f'))
def exp(a,b):
    """This funtion finds exponent"""
    print(format(a**b,'.2f'))
if choice==1:
    add(a,b)
elif choice==2:
    sub(a,b)
elif choice==3:
    mul(a,b)
elif choice==4:
    div(a,b)
elif choice==5:
    tdiv(a,b)
elif choice==6:
    mod(a,b)
elif choice==7:
    exp(a,b)
else:
    print("Enter a valid option")
print(add.__doc__)
