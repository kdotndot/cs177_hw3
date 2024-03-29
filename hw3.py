import random
import string
from PIL import Image
import numpy as np
from requests import head


from rsa import decrypt
def xor(string1, string2):
    #Input: 2 strings
    #Output: List of xor'd characters in hex
    if len(string1) != len(string2):
        print("ERROR: INEQUAL LENGTH")
        return
    
    length = len(string1)
    ans = []
    for x in range(0, length):
        letter1 = ord(string1[x])
        letter2 = ord(string2[x])
        temp = hex(letter1 ^ letter2)[2:]
        if len(temp) < 2:
            temp = "0" + temp
        ans.append(temp)
    return ans

def xor_hex(string1, hex2):
    #Input: A string and a list of hex values, without the 0x part
    #Output: List of hex values xor'd
    if len(string1) != len(hex2):
        print("ERROR: INEQUAL LENGTH")
        return
    length = len(string1)
    ans = []
    for x in range(0, length):
        letter1 = ord(string1[x])
        letter2 = int(hex2[x], 16)
        temp = hex(letter1 ^ letter2)[2:]
        if len(temp) < 2:
            temp = "0" + temp
        ans.append(temp)
    return ans
    
    
""" def key_generator(length):
    
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits
    symbols = string.punctuation
    all = lower + upper + num + symbols
    password = ''.join(random.choice(all) for i in range(length)) 
    return password """
    
def convert_to_ascii(string):
    ans = []
    for x in string:
        ans.append(hex(ord(x))[2:])    
    return ans
    
string1 = "Darlin dont you go"
string2 = "and cut your hair!"




#LOGO2 = 76 * 112
LOGO1 = 'logo_1.bmp'
LOGO2 = 'logo_2.bmp'


#Parsing logo
data = ""
with open(LOGO2, "rb") as f:
    data = f.read()
bytes1 = []
for x in data:
    bytes1.append(x)
    
#Keeping header
header1 = bytes1[0:108]
for x in range(0, len(header1)):
    header1[x] = hex(header1[x])[2:]
    
logo1encrypted = []

with open("/dev/urandom", "rb") as rand:
    key1 = rand.read(len(bytes1))

print(key1)
""" for x in range(0,len(bytes1)):
    bytes1[x] = hex(bytes1[x])[2:]

logo1encrypted = xor_hex(key1, bytes1)

logo1encrypted[0:108] = header1
logo1encryptedbytes = bytearray()
for x in range(0,len(logo1encrypted)):
    if len(logo1encrypted[x]) == 1:
        logo1encrypted[x] = "0" + logo1encrypted[x]
    logo1encrypted[x] = bytes.fromhex(logo1encrypted[x])
    logo1encryptedbytes += logo1encrypted[x]



LOGO1ENCRYPT = open("logo2_encrypted.bmp", "wb")
LOGO1ENCRYPT.write(logo1encryptedbytes) """

