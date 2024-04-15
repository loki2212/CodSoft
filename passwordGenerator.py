import random
import string

def generatePassword(length):
    ascii= string.ascii_letters
    digits=string.digits
    punc=string.punctuation
    chars=ascii+digits+punc
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def passw():
    try:
         password_length = int(input("Enter the length of the password: "))
         if password_length <= 0:
             print("Please enter a valid positive length.")
         else:
             password = generatePassword(password_length)
             print("Generated Password is: ",password)
    except ValueError:
        print("Invalid input. Please enter a valid integer for the password length.")

passw()
