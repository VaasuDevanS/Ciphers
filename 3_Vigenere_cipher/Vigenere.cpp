/*
* Vigenère Cipher (Poly-alphabetic Cipher)
* Author: Vaasudevan (github.com/VaasuDevanS)
* Date: Dec 21, 2018
* Link: http://crypto.interactive-maths.com/vigenegravere-cipher.html
*/

#include <iostream>
#include <cmath>    // abs
using namespace std;

string encrypt(string input, string key)
{
    string encrypted = "";

    // Generate key_stream (match key_phrase with input_length)
    int input_len=input.size(), key_len=key.size();
    int diff = abs(input_len-key_len);
    string key_stream = "";
    for(int i=0; i<diff; i++)
        key_stream += key;
    key_stream = key_stream.substr(0, input_len);

    // Generate Tabula_Recta
    string Al = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"; Al += Al;
    char table[100][100];
    for(int i=65; i<65+26; i++) {
        string A_i = Al.substr(Al.find(i), 26);
        int k = 0;
        for(int j=65; j<65+27; j++) {
            table[i][j] = A_i[k++];
        }
    }

    /*
    // Print the Tabula_Recta
    cout << "   ";
    for(int i=65; i<65+26; i++)
        cout << (char)i << " ";
    cout << endl;
    for(int i=65; i<65+26; i++) {
        cout << (char)i << " ";
        for(int j=65; j<65+27; j++){
            cout << table[i][j] << " ";
        }
        cout <<endl;
    }
    */

    // Encrypt
    for(int i=0; i<input.size(); i++) {
        encrypted += table[input[i]][key_stream[i]];
    }

    return(encrypted);
}

string decrypt(string enc, string key)
{
    string decrypted = "";

    // Generate key_stream (match key_phrase with input_length)
    int enc_len=enc.size(), key_len=key.size();
    int diff = abs(enc_len-key_len);
    string key_stream = "";
    for(int i=0; i<diff; i++)
        key_stream += key;
    key_stream = key_stream.substr(0, enc_len);

    // Generate Tabula_Recta
    string Al = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"; Al += Al;
    char table[100][100];
    for(int i=65; i<65+26; i++) {
        string A_i = Al.substr(Al.find(i), 26);
        int k = 0;
        for(int j=65; j<65+26; j++) {
            table[j][A_i[k++]] = i;
        }
    }

    // DECRYPT
    for(int i=0; i<enc.size(); i++) {
        decrypted += table[key_stream[i]][enc[i]];
    }

    return(decrypted);
}

int main()
{
    string input, encrypted, decrypted, key="AWESOMECIPHER";
    cout << "Enter the String (only alpha): ";
    getline(cin, input);

    encrypted = encrypt(input, key);     // Call Encrypt
    decrypted = decrypt(encrypted, key); // Decrypt the Encrypted

    // Print the Encrypted and the Decrypted
    cout << "Encrypted: " << encrypted << endl;
    cout << "Decrypted: " << decrypted << endl;
}

// EOF
