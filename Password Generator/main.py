import random
import string

print("Welcome to Password Generator")

chars = 'ABCDEFGHIKLMNOPQRSTVXYZabcdefghiklmnopqrstvxyz1234567890!@£$%^&*().,?'


user_input = input("How many characters would you like in your passworwd: ")
user_input = int(user_input)

length = int(input("How many characters would you like as password: "))
length = int(length)

print("Your password is/are: ")

for i in range(user_input):
    password = ""
    for j in range(length):
        password += random.choice(chars)
    print(password)



