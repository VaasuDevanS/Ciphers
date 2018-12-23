"""
Playfair Cipher (Digraph Substitution Cipher)
"""
__author__ = "Vaasudevan (github.com/VaasuDevanS)"
__date__   = "Dec 22, 2018"
__link__   = "http://crypto.interactive-maths.com/playfair-cipher.html"

from string import ascii_uppercase as A
from pprint import pprint
import re

def polybius_square(key):

    # Generate Polybius Square
    polybius_str = ""
    for letter in key+A:
        if letter not in polybius_str and len(polybius_str) != 25:
            polybius_str += letter
    return [tuple(polybius_str[i:i+5]) for i in range(0,25,5)]


def generate_digraphs(key, sent):

    ch = sorted(set(key).union(sent).symmetric_difference(A))[0]

    # Generate Digraphs using Recursion
    ini_digraphs = [sent[i:i+2] for i in range(0, len(sent), 2)] # Initial
    digraphs = []
    for ix,digraph in enumerate(ini_digraphs):
        pair = digraph
        if len(pair) == 1:
            pair += ch
        if pair[0] == pair[1]:
            ini_digraphs[ix] = "{0}{1}{0}".format(pair[0], ch)
            return generate_digraphs(key, "".join(ini_digraphs))
        digraphs.append(pair)
    return digraphs, ch


def playfair_encrypt(sent, key):

    sent = re.sub("[\W\d]", "", sent).upper() # keep only Alpha
    key = re.sub("[\W\d]", "", key).upper()   # keep only Alpha

    polybius = polybius_square(key)
    digraphs, ch = generate_digraphs(key, sent) # rule1

    encrypted = []
    for a,b in digraphs:

        # check for row and col - rule2 & rule3
        for seq in polybius + list(zip(*polybius)):
            if a in seq and b in seq:
                seq = seq * 2
                a_enc, b_enc = seq[seq.index(a)+1], seq[seq.index(b)+1]
                encrypted.append(a_enc+b_enc+" ")
                break
        # form the rectangle - rule4
        else:
            row1 = [row for row in polybius if a in row][0]
            row2 = [row for row in polybius if b in row][0]
            a_enc = row1[ row2.index(b) ]
            b_enc = row2[ row1.index(a) ]
            encrypted.append(a_enc+b_enc+" ")

    return "".join(encrypted), ch


def playfair_decrypt(enc, key, ch):

    enc_digraphs = enc.split()              # Create enc_digraphs

    key = re.sub("[\W\d]", "", key).upper() # keep only Alpha
    polybius = polybius_square(key)         # Polybius square

    decrypted = []
    for a,b in enc_digraphs:

        # check for row and col - rule2 & rule3
        for seq in polybius + list(zip(*polybius)):
            if a in seq and b in seq:
                seq = seq * 2
                a_enc, b_enc = seq[seq.index(a)-1], seq[seq.index(b)-1]
                decrypted.append(a_enc+b_enc)
                break
        # form the rectangle - rule4
        else:
            row1 = [row for row in polybius if a in row][0]
            row2 = [row for row in polybius if b in row][0]
            a_enc = row1[ row2.index(b) ]
            b_enc = row2[ row1.index(a) ]
            decrypted.append(a_enc+b_enc)

    return "".join(decrypted).replace(ch, "")


if __name__ == "__main__":

    # Keyword for this Cipher
    key_phrase = "Playfair Cipher"

    # Encrypt
    sent = input("Enter the String: ")
    E, ch = playfair_encrypt(sent, key_phrase)
    print(ch)

    # Decrypt
    D = playfair_decrypt(E, key_phrase, ch)

    print("Encrypted: %s\nDecrypted: %s" %(E, D))

# EOF
