choice=1
while choice==1:
    char= str(input("Enter a character: "))
    count=ord(char)+1
    charUp= chr(count)
    print(charUp)
    choice=int(input("Enter 1 if you want to continue: "))
