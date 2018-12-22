"""
Simple Caesar Cipher function based on key_value and mod26.
mod26 restricts the encrypted characters as alphabets
"""
__author__ = "Vaasudevan (github.com/VaasuDevanS)"
__date__   = "Dec 13, 2018"
__link__   = "http://crypto.interactive-maths.com/caesar-shift-cipher.html"

def crypt(typ, sentence, key_value):

    # Decides whether Encryption or Decryption
    key = key_value if typ.lower().startswith('e') else -key_value
    crypted_letters = []

    # Loop each character in sentence
    for s in sentence:
        if s.isalpha(): # [A-Za-Z]
            x = 65 if s.isupper() else 97
            crp_s = (ord(s) - x + key) % 26
            crypted_letters.append(chr(crp_s+x))
        else:
            crypted_letters.append(s)

    # Join everything and return the string
    return "".join(crypted_letters)

if __name__ == "__main__":

    E = crypt("Encrypt", input("Enter the String: "), 2019)
    D = crypt("Decrypt", E, 2019)

    print("Encrypted: %s\nDecrypted: %s" % (E, D))

# EOF
