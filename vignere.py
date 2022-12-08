def letterToNumber(s):
    num_list = []
    for c in s:
        num_list.append(str((ord(c) - 65)))
    return num_list

cipherInput ="IYEGXPXMMOETTNZKAYAUYYTTBBMVFFYYKKKCIGXELZFXBAVSIJZOXQBBNXUWIOYZVTFRVABXMZXWYROXAZRTXOEOLSKUTJAEKMGWABWHVAMYKPHQVCQLFMQNWOEOBRMETXOFVTQMGHJIIGIRWTKEVYQVFIFAJAEKMGWALYYVAVMUCKIYJQHLNHGGZZWGQBUTXGIMFYLRYVUDAVPIGVL"
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