import string
print(string.ascii_lowercase)
print(list(string.ascii_lowercase[:10]))
print(list(string.ascii_lowercase[0:5]+string.ascii_lowercase[6:10]))
print(list(i*x for i in string.ascii_lowercase[0:5] +string.ascii_lowercase[6:10] for x in [1,2,3]))
print(map(list(i*x for i in string.ascii_lowercase[0:5] 
           +string.ascii_lowercase[6:10] for x in [1,2,3]))