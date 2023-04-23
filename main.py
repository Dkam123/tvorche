import random
import time

a = 'abcdefghijklmnopqrstuvwxyz'
b = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
c = '0123456789'
d = '[]{}()*&_-!@?'

all = a + b + c + d
length = 8
password = "".join(random.sample(all,length))
print("Password is being generated...")
time.sleep(3)
print("Your password is ready:")
print(password)
input()

