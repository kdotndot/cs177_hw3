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
    
    
def key_generator(length):
    
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits
    symbols = string.punctuation
    all = lower + upper + num + symbols
    password = ''.join(random.choice(all) for i in range(length)) 
    return password
    
def convert_to_ascii(string):
    ans = []
    for x in string:
        ans.append(hex(ord(x))[2:])    
    return ans
    
string1 = "Darlin dont you go"
string2 = "and cut your hair!"
key = key_generator(len(string1))