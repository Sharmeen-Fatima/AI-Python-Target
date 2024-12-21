import random

print('welcome to the passowrd generator ')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ~!@#^*()0123456789'

number = input('Amount of Password to Generate: ')
number = int(number)

length = input('Input Your Password Length: ')
length = int(length)

print("Here are your passwords...!!")

for password in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)

    print(passwords)
