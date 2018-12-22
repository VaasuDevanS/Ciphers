/*
* Affine Cipher function based on ax+b and mod26.
* mod26 restricts the encrypted characters as alphabets
* Author: Vaasudevan (github.com/VaasuDevanS)
* Date: Dec 20, 2018
* Link: http://crypto.interactive-maths.com/affine-cipher.html
*/

#include <iostream>
#include <ctype.h>
using namespace std;

string encrypt(string in, int a, int b)
{
    string encrypted;
    for(char c : in) {
        // Encrypt if its only character [a-zA-Z]
        if ( (c>='a' && c<='z') || (c>='A' && c<='Z') ) {
            int flag = isupper(c) ? 65 : 97;
            int d = ( a * (c-flag) + b  ) % 26;
            encrypted.push_back(d + flag);
        }
        else {
            encrypted.push_back(c);
        }
    }
    return encrypted;
}

string decrypt(string enc, int a, int b)
{
    string decrypted; int a_1=0;
    // inverse
    for (int i=0; i<26; i++) {
        if (a*i%26 == 1)
            a_1 = i;
    }
    for(char c : enc) {
        // Decrypt if its only character[a-zA-Z]
        if ( (c>='a' && c<='z') || (c>='A' && c<='Z') ) {
            int flag = isupper(c) ? 65 : 97;
            int d = ( a_1 * (c-flag-b) ) % 26;
            d = (d<0)? d+26: d; // C performs modulus towards 0
            decrypted.push_back(d + flag);
        }
        else {
            decrypted.push_back(c);
        }
    }
    return decrypted;
}

int main()
{
    string input, encrypted, decrypted;
    cout << "Enter the String: ";
    getline(cin, input);

    encrypted = encrypt(input, 5, 7);     // Call Encrypt
    decrypted = decrypt(encrypted, 5, 7); // Decrypt the Encrypted

    // Print the Encrypted and the Decrypted
    cout << "Encrypted: " << encrypted << endl;
    cout << "Decrypted: " << decrypted << endl;
}

// EOF
