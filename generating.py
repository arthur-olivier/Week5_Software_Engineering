# Python 3 code to demonstrate
# SHA hash algorithms.

import hashlib
import string
import json


def listAlphabet():
    upper=list(string.ascii_lowercase)
    lower=list(string.ascii_uppercase)
    number=["1","2","3","4","5","6","7","8","9","0"]
    result=upper+lower+number
    return result

list=listAlphabet()
result = []
dict={}


for i in range(0,len(list)):
    str = list[i]
    result1=hashlib.sha1(str.encode())
    dict[result1.hexdigest()]=str
    result+= [result1.hexdigest()+" : "+list[i]]

print(dict)

with open('data.json', 'w') as mon_fichier:
	json.dump(dict, mon_fichier)




