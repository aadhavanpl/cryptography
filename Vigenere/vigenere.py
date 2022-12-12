def letterToNumber(s):
    return [ord(c) - 65 for c in s]

f = open("Vigenere/vigenere.txt", mode='r', encoding='utf-8')
line = f.readline()
cipherInput = line
cipherText = letterToNumber(cipherInput)

givenKey = "INTEGRITY"
key = letterToNumber(givenKey)

plainText = ''
j = 0

for i in range(len(cipherText)):
    plainText+=chr((int(cipherText[i]) - int(key[j]))%26 + 65)
    j+=1
    if j == len(key): j = 0
print(plainText)