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