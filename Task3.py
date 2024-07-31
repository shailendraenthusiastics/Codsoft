import random
import string
print("Welcome to our Random Password Generator")
def my_fun():
    length = int(input("Enter the length of the password you want: "))
    lowerD=string.ascii_lowercase
    upperD=string.ascii_uppercase
    digitD=string.digits
    symbolsD=string.punctuation
    combine=lowerD+upperD+digitD+symbolsD
    x=random.sample(combine ,length)
    password="".join(x)
    print("password=",password)
    my_fun()
my_fun()