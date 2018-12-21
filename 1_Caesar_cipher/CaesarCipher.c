/*
* Simple Caesar Cipher function based on key_value and mod26.
* mod26 restricts the encrypted characters as alphabets
* Author: Vaasudevan (github.com/VaasuDevanS)
* Date: Dec 14, 2018
*/

#include <stdio.h>
#include <ctype.h>
#define MAX 100

char *encrypt(char *arr, int key)
{
    static char encrpt[MAX];
    for(int i=0; arr[i] != '\0'; i++) {
        char c = arr[i];
        // Encrypt if its only character [a-zA-Z]
        if ( (c>='a' && c<='z') || (c>='A' && c<='Z') ) {
            int flag = isupper(c) ? 65 : 97;
            int d = ( c - flag + key ) % 26;
            encrpt[i] = d + flag;
        }
        else {
            encrpt[i] = c;
        }
    }
    return encrpt;
}

char *decrypt(char *arr, int key)
{
    static char decrpt[MAX];
    for(int i=0; arr[i] != '\0'; i++) {
        char c = arr[i];
        // Decrypt if its only character[a-zA-Z]
        if ( (c>='a' && c<='z') || (c>='A' && c<='Z') ) {
            int flag = isupper(c) ? 65 : 97;
            int d = ( c - flag - key ) % 26;
            d = (d<0)? d+26: d; // C performs modulus towards 0
            decrpt[i] = d + flag;
        }
        else {
            decrpt[i] = c;
        }
    }
    return decrpt;
}

int main()
{
    char input[MAX], *encrypted, *decrypted, ch;
    int i=0;

    // Read the String from the User
    printf("Enter the String: ");
    while ((ch=getchar()) != '\n'){
        input[i] = ch;
        i++;
    }
    input[i] = '\0'; // Mark End-of-String

    encrypted = encrypt(input, 2019);     // Call Encrypt
    decrypted = decrypt(encrypted, 2019); // Decrypt the encrypted

    // Print the Encrypted and Decrypted string
    printf("Encrypted: %s\n", encrypted);
    printf("Decrypted: %s\n", decrypted);
}

// EOF
