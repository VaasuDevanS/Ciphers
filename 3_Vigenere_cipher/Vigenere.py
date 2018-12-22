"""
Vigenère Cipher (Poly-alphabetic Cipher)
"""
__author__ = "Vaasudevan (github.com/VaasuDevanS)"
__date__   = "Dec 21, 2018"
__link__   = "http://crypto.interactive-maths.com/vigenegravere-cipher.html"

from string import punctuation as P, digits as d
import re


def vigenere_encrypt(sent, key_phrase):

    # Keep-track for the spaces, non-alphanumeric and numeric chars
    extras = [(ix,c) for ix,c in enumerate(sent) if c in " "+P+d]
    
    # Generate key_stream
    sent = re.sub("[\W\d]", "", sent)
    sen_len, key_len = len(sent), len(key_phrase)
    key_stream = (key_phrase*abs(sen_len-key_len))[:sen_len]

    # Generate Tabula_Recta
    table = {}
    alphas = "".join((chr(i) for i in range(65, 65+26))) * 2
    alphabets = lambda c: alphas[alphas.index(c) : alphas.index(c)+26]
    for i in range(65, 65+26):
        for k,v in zip(range(65, 65+26), alphabets(chr(i))):
            table[chr(i), chr(k)] = v
    
    # Encrypt based on the table and insert the spaces
    encrypted = [table[(p,k)] for p,k in zip(sent, key_stream)]
    for ix, c in extras:
        encrypted.insert(ix, c)

    return "".join(encrypted)


def vigenere_decrypt(enc, key_phrase):

    # Keep-track for the spaces, non-alphanumeric and numeric chars
    extras = [(ix,c) for ix,c in enumerate(sent) if c in " "+P+d]

    # Generate key_stream
    enc = re.sub("[\W\d]", "", enc)
    enc_len, key_len = len(enc), len(key_phrase)
    key_stream = (key_phrase*abs(enc_len-key_len))[:enc_len]

    # Generate Tabula_Recta
    table = {}
    alphas = "".join((chr(i) for i in range(65, 65+26))) * 2
    alphabets = lambda c: alphas[alphas.index(c):alphas.index(c)+26]
    for i in range(65, 65+26):
        for k,v in zip(range(65, 65+26), alphabets(chr(i))):
            table[chr(k), v] = chr(i)

    # Decrypt based on the table
    decrypted = [table[(k,e)] for e,k in zip(enc, key_stream)]
    for ix, c in extras:
        decrypted.insert(ix, c)

    return "".join(decrypted)


if __name__ == "__main__":

    # Keyword for this Cipher
    key_phrase = "AwesomeCipher".upper()

    # Encrypt
    sent = input("Enter the String: ").upper()
    E = vigenere_encrypt(sent, key_phrase)

    # Decrypt
    D = vigenere_decrypt(E, key_phrase)

    print("Encrypted: %s\nDecrypted: %s" %(E, D))

# EOF
