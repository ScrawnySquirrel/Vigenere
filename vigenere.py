def caesar_encrypt(ptstring, key):
    ptlist = list(ptstring.upper())
    ctlist = []
    for ptchar in ptlist:
        if ptchar.isalpha():
            ctlist.append(chr((ord(ptchar) + key-65) % 26 + 65))
    return "".join(ctlist)

def caesar_decrypt(ctstring, key):
    ctlist= list(ctstring.upper())
    ptlist = []
    for ctchar in ctlist:
        if ctchar.isalpha():
            ptlist.append(chr((ord(ctchar) - key-65) % 26 + 65))
    return "".join(ptlist)

def generate_vigenere_table(init_shift):
    eng_alpha = "abcdefghijklmnopqrstuvwxyz"
    vigenere_table = []
    for idx in range(0+init_shift,26+init_shift):
        vigenere_table.append(list(caesar_encrypt(eng_alpha, idx)))
    return vigenere_table

vt = generate_vigenere_table(0)
for ln in vt:
    print(ln)
print(len(vt))

# Caesar cipher function test
# tst = caesar_encrypt("hello",5)
# print(tst)
# print(caesar_decrypt("".join(tst),5))
