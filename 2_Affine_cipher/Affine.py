"""
Affine with mod26 Cipher function to encrypt and decrypt 
"""
__author__ = "Vaasudevan (github.com/VaasuDevanS)"
__date__   = "Dec 20, 2018"


def affine_cipher(typ, sentence, a, b):

    crypted = []

    # Loop each character in sentence
    for s in sentence:
        if s.isalpha(): # [A-Za-Z]
            x = 65 if s.isupper() else 97
            if typ.lower().startswith("e"):
                crp_s = (a*(ord(s)-x) + b) % 26
            else:
                a_1 = {a*i%26 : i for i in range(26)}.get(1,0) # a inverse
                crp_s = a_1 * (ord(s)-x-b) % 26
            crypted.append(chr(crp_s+x))
        else:
            crypted.append(s)

    return "".join(crypted)

if __name__ == "__main__":

    E = affine_cipher("Encrypt", input("Enter the String: "), 5, 7)
    D = affine_cipher("Decrypt", E, 5, 7)

    print("Encrypted: %s\nDecrypted: %s" % (E, D))

# EOF
