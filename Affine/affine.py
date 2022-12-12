def gcd(a, b):
    if(b == 0): return abs(a)
    return gcd(b, a % b)

def letterToNumber(s):
    return [ord(c) - 65 for c in s]

def aInverse(a):
    for i in range(26):
        flag = (a*i)%26
        if flag == 1: return i
            
def decrypt(a, b, cipherText):
    plaintext = ''
    for i in cipherText:
        plaintext += chr((a*(int(i)-b))%26 + 65)
    return plaintext

f = open("Affine/affine.txt", mode='r', encoding='utf-8')
line = f.readline()
cipherInput = line
cipherText = letterToNumber(cipherInput)
for a in range(26):
    if gcd(a, 26) == 1:
        for b in range(26):
            aInv = aInverse(a)
            print(decrypt(a, b, cipherText))
print("Plaintext: " + decrypt(23, 13, cipherText)) #23, 13 is the required plaintext for the given example as it makes the most sense (readable)