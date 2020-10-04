import sys
# ask user for cla
if len(sys.argv) != 2:
    sys.exit('Usage: python vigenere.py k')
# string key
key = sys.argv[1]
if key.isalpha() == False:
    sys.exit('Error, not alphabatic')

# list for the key
arr = []
for i in range(len(key)):
    if key[i].isupper():
        arr.append(ord(key[i]) - 65)
    else:
        arr.append(ord(key[i]) - 97)

# ask user for plaintext
p = input("plaintext: ")

# encipher
print('ciphertext: ', end='')
j = 0
for i in range(len(p)):
    if (p[i].isalpha() & p[i].isupper()):
        code = (ord(p[i]) + arr[j % len(key)])
        if code > 90:
            code -= 26
        print(chr(code), end='')
        j += 1
    elif (p[i].isalpha() & p[i].islower()):
        code = (ord(p[i]) + arr[j % len(key)])
        if code > 122:
            code -= 26
        print(chr(code), end='')
        j += 1
    else:
        code = p[i]
        print(code, end='')

print()
