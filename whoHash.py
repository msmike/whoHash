###############################################################################
# whoHash  - Hashing Algorithm
# Developed by Mike Dominguez, Frank Quijada, Hatan Hantol, and Scott Johnson
# The purpose of this hash function is to create a unique 80-bit message. 
# Please write your message in a file and place it in the same directory as the program
# If you can break it, please let us know so that we can further improve on it 
###############################################################################

import random
import os
from typing import List

def main():
	
    inputFile = input("What file would you like to hash? ") 
    f = open(inputFile, "r")
    append_write = 'w'  
    mBlock = ""
    bitFile = ""
    count = 0 
    with open(inputFile, "rb") as inputFile:
        k = 0
        for bit in getBits(inputFile):
            bitFile += str(bit)
    f.close()  
    bFileLength = len(bitFile)  
    bLength = 160
    bitFile = pad(bitFile, bFileLength, bLength)
    bFileLength = len(bitFile)
    front = 0
    rear = 1  
    loopUntil = bFileLength / bLength
    i = 1
    Hk = bytearray(b'01000101100011100000010000101000110111110110010100001011001111000010101100000010')
    while(i <= loopUntil):
        rear = i * bLength
        mBlock = bitFile[(front): rear]
        Hk = compress(mBlock, Hk)
        front = rear
        i = i + 1

    finalHash = convertBinHex(Hk)
    print(finalHash)


def getBits(inputFile):
	
    while True:
        b = inputFile.read(1)
        if not b:
            break
        b = ord(b)
        for i in range(8):
            yield b & 1
            b >>= 1

def pad(mBlock, length, bLength):
	
    p = "0100010110001110000001000010100011011111011001010000101100111100001010110000001001000101100011100000010000101000110111110110010100001011001111000010101100000010000100100010111101"
    d = "0001110000001000010100011011111011001010000101100111100001010110000001000010010001011110101000101100011100000010000101000110111110110010100001011001111000010101100000010010001011"
    s = True
    count = length%bLength
    x = 0    
    while (count != 0):  
        if s == True:
            mBlock = mBlock + p[x]
            s == False
        elif s == False:
            mBlock = mBlock + p[x]
            s == True
        count = len(mBlock)%bLength
        x = x + 1

    return mBlock

def totalBlocks(outputFile):
	
    count = 0
    f = open(outputFile, "r")
    fl = f.readlines()
    for i in range(len(fl)):
        count += 1
    count = count / 160
    
    return count

def compress(mBlock, Hk):
	
    i = 0
    messageBlock = ''.join(str(i) for i in mBlock)
    Mb = bytearray()
    Mb.extend(messageBlock.encode())
    M1 = Mb[0:80]
    M2 = Mb[80:160]
    
    Hp = permute(Hk)
    bLength = len(messageBlock)
    length = int(len(messageBlock)/2)
    HashValue = bytearray(length)
    V1 = bytearray(len(M1))
    V2 = bytearray(len(M2))
    V1 = sxor(M1, Hk)
    V2 = sxor(M2, Hp)
    HashValue = sxor(V1, V2)

    return HashValue
	
def permute(Hk):
	
    Hk = str(Hk)
    Hk = Hk[12:92]
	
    permTable = [5, 36, 7, 10, 1, 35, 12, 31, 2, 23, 37, 3, 33, 32, 18, 15, 17, 25, 26, 11,
			    20, 16, 34, 9, 14, 19, 39, 21, 30, 13, 8, 40, 27, 28, 4, 29, 6, 22, 24, 38,
			    46, 74, 60, 66, 68, 51, 57, 54, 79, 62, 77, 58, 69, 48, 49, 80, 65, 73, 67, 59, 
			    64, 76, 47, 70, 71, 72, 42, 43, 56, 61, 63, 50, 78, 41, 45, 75, 55, 52, 44, 53]
	
    p = ""
	
    for i in permTable:
        p += Hk[int(i)-1]

    Hp = bytearray()
    Hp.extend(p.encode())

    return Hp

def sxor(r, l): 
	
	b = bytearray(len(r))
	
	for i in range(len(r)):
		b[i] = r[i] ^ l[i]
	
	a = bytes(b).hex()
	b = ""
	
	for i in range (len(a)):
		if i % 2 == 1:
			b += a[i]
	
	x = bytearray()
	x.extend(b.encode())

	return x

def convertBinHex(Hk):
	
	hexString = hex(int(Hk, 2))
	
	return hexString



if __name__ == "__main__":
	
    main()
