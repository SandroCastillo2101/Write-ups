import os

with open('output.txt') as f:
    lines = f.readlines()

for line in lines:
    c12 = line[0:2]
    c34 = line[2:4]
    c56 = line[4:6]
    decimal1 = int(c12, 16)
    decimal2 = int(c34, 16)
    decimal3 = int(c56, 16)
    if (decimal1 == decimal2 ^ 11):
        key = decimal1^67
        if(chr(decimal3^key)=="T"):
            print("Cipher text: ", line)
            print("Key: ", hex(key))    
