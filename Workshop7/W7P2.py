def types ():
    a= input ("Enter a number:")
    print(int(a))
    print(float(a))
types ()
def squared ():
    a= int (input ("Enter a number: "))
    print(a*a)
squared ()
def int_to_string():
    a= int (input ("Enter a number:"))
    print(str(a))
int_to_string()
name= str(input ("Enter your name: "))
def hello_world (name):
    print("Hello World, my name is",name)
hello_world(name)
n= int (input ("Enter how many times the string should be printed: "))
sym= str(input ("Enter the string: "))
def print_ast (n, sym="*"):
    for i in range(n):
        print (sym)
print_ast(n, sym)
import statistics as st
list=[]
for i in range (0,5):
    data=int (input ("Enter a number:"))
    list.append (data)
def improved_average(*n):
    print("Mode: ", st.mode(n))
    print("Median:", st.median (n))
    print("Mean: ", st.mean (n))
improved_average(list[0],list [1],list[2],list[3],list[4])
n= int(input ("Enter a number: "))
def either_side(n):
    print ("You typed",n,", one less than", n,"is",n-1, "one more than",n,"is",n+1)
either_side(n)
