# Password Generator
import string
import random


def generate_password(len):
    all_char = string.ascii_letters + string.digits + string.punctuation
    password = ''
    for char in range(len):
        rand = random.choice(all_char)
        password = password + rand
    return password


length = int(input('How many characters in your password?'))
print('Your new password: ', generate_password(length))



# or u can try this



# #Random Password Generator
# import random
# lower =  "abcdefghijklmnopqrstuvwxyz"
# upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# numbers = "0123456789"
# symbols = "[]{}()*;/,._-"
# all = lower + upper + numbers + symbols
# length = int(input("Enter the length of your password"))
# password = "".join(random.sample(all, length))
# print(password)