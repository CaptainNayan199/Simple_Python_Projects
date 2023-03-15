# importing packages.
import string
import random


def password():
    a = string.ascii_uppercase
    b = string.ascii_lowercase
    c = string.digits
    d = string.punctuation
    passlength = int(input("Enter the password length : \n"))
    e = []
    e.extend(list(a))
    e.extend(list(b))
    e.extend(list(c))
    e.extend(list(d))
    random.shuffle(e)
    passs = (''.join(e[0:passlength]))
    print(passs)


password()
