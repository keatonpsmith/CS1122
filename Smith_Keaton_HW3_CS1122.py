import binascii
def dectobin(x):
    return bin(x)

def hextoascii(hexa):
    output = ""
    hexlist = hexa.split()
    for item in hexlist:
        temp = int(item, 16)
        output += chr(temp)
    return output

def bintohex(bina):
    output = ""
    binlist = bina.split()
    for item in binlist:
        temp = int(item, 2)
        digit = str(hex(temp))
        digit = digit[2]
        output += digit
    output = "0x" + output
    return output

def octtodec(octa):
    num = str(octa)
    reverse = num[::-1]
    output = 0
    for index in range(len(reverse)):
        output += (int(reverse[index]) * 8 ** index)
    return output

def main():
    print(dectobin(57))
    print(dectobin(123))
    print(dectobin(85))
    print(dectobin(38))
    print(hextoascii("0x41 0x53 0x43 0x49 0x49 0x20 0x77 0x68 0x61 0x74 0x20 0x79 0x6f 0x75 0x20 0x64 0x69 0x64 0x20 0x74 0x68 0x65 0x72 0x65"))
    print(hextoascii("0x39 0x41 0x4d 0x20 0x69 0x73 0x20 0x74 0x6f 0x6f 0x20 0x65 0x61 0x72 0x6c 0x20 0x66 0x6f 0x72 0x20 0x63 0x6c 0x61 0x73 0x73"))
    print(hextoascii("0x43 0x6f 0x6d 0x70 0x75 0x74 0x65 0x72 0x73 0x20 0x61 0x72 0x65 0x20 0x61 0x67 0x69 0x63"))
    print(hextoascii("0x57 0x68 0x61 0x74 0x20 0x74 0x68 0x65 0x20 0x68 0x65 0x78 0x3f"))
    print(bintohex("0000 1011 1010 1110 1101 1110 1010 1101"))
    print(bintohex("1100 1010 1111 1110 1111 1010 1100 1110"))
    print(bintohex("1011 1110 1110 1111 1101 0000 0000 1101"))
    print(bintohex("1111 1111 1111 1111 1001 0000 0110 0010"))
    print(octtodec(10))
    print(octtodec(42))
    print(octtodec(77))
    print(octtodec(113))
