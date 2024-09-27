# Random Password Generator Application:
import string
import random
print("Generate your Passord\n")
st_1 = string.ascii_lowercase
st_2 = string.ascii_uppercase
st_3 = string.punctuation
st_4 = string.digits
s = []
s.extend((st_1))
s.extend((st_2))
s.extend((st_3))
s.extend((st_4))
random.shuffle(s)
len = int(input("Enter Password length :\t"))
print("Your Password is:")
x = ("".join(s))
print(x[0:len])
    


 
 

