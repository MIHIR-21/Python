# Random password generator 
import random
import string

pass_len = 12

values= string.ascii_letters + string.digits + string.punctuation

password = ""
for i in range(pass_len):
    password += random.choice(values)

print("your password is:", password)
