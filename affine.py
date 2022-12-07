def gcd(a, b):
    if(b == 0):
        return abs(a)
    return gcd(b, a % b)

def letterToNumber(s):
    num_list = []
    for c in s:
        num_list.append(str((ord(c) - 65)))
    return num_list

def aInverse(a):
    for i in range(26):
        flag = (a*i)%26
        if flag == 1:
            return i
            
def decrypt(a, b, cipherText):
    plaintext = ''
    for i in cipherText:
        plaintext += chr((a*(int(i)-b))%26 + 65)
    return plaintext

cipherInput = "NUTALDQIQTAYRQNJDHHNLDMTLDHYVNAEDPHDMYRDAHPQDYCDTAYDLQTYFRUNMRVPJDAYRQNJDHHNLDYRDAHPQDYCDTAYDLQTYFRUNJDHHNLDERYCYCDJDHHNLDNAMYCDJDHHNLDMTLDHYNQDADDMDM"
cipherText = letterToNumber(cipherInput)
for a in range(26):
    if gcd(a, 26) == 1:
        for b in range(26):
            aInv = aInverse(a)
            print(decrypt(a, b, cipherText)) #23, 13