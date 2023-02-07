#Welcoming The user to the program
def greeting():
    print("Hello User, Welcome to Ceaser Cipher\nHere you can encrypt or decrypt any Words you would like using the Ceaser Cipher Method")
#Taking the input from the user
def ask():
    a = (input("Do you want to Encrypt(e) or Decrypt(d)?\nPlease enter e/d depending on your need:"))
    while True:
        if a == "e":
            message = str(input("Enter the message you would like to Encrypt: "))
            shift_num = int(input("Enter the shift number: "))     
        elif a == "d":
            message = str(input("Enter the word you would like to Decrypt: "))
            shift_num = int(input("Enter the shift number: "))
        else:
            print("Invalid Response")
        return a,message,shift_num 
#Coding he encryption process 
def encrypt(a, shift_num):   
    textShift= ""
    for b in a:
        if b.isalpha():
            push= ord(b)+shift_num
            if push > ord('Z'):
                    push -= 26
            elif push < ord('A'):
                    push += 26
            textShift+=chr(push)  
        else:
            textShift+=b
    return textShift
#Coding the decryption process
def decrypt(a, shift_num):
    textShift = ""
    for b in a:
        if b.isalpha():
            push = ord(b)-shift_num
            if push > ord('Z'):
                    push -= 26
            elif push < ord('A'):
                    push += 26
            textShift += chr(push)  
        else:
            textShift += b
    return textShift
#Looping if the user wants to use the program again
def main():
    greeting()
    another = "y"     
    while another == "y":
        blarg = ask()
        if blarg[0] == "e":
            answer = encrypt(blarg[1],blarg[2]) 
            print("The Encrypted text: ",answer)
        elif blarg[0] == "d":
            answer = decrypt(blarg[1],blarg[2]) 
            print("The Decrypted text: ",answer)
        another = str(input("Do you want to Encrypt/Decrypt another message?(Y/N):"))
    print("Thankyou for using Ceaser Cipher program\nGoodbye!")
#Calling all functions
if __name__ == "__main__":
    main()


