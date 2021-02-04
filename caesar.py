import os
import numpy as np


def encrypt_caesar(plainText, key):
    """
    encrypts plaintext with caesar cipher method and writes the output in caesar_cipher.txt
    Args:
        plainText(list): list of plaintext in caesar_plain.txt file 
                                [each line in the file is a list element]
        key(int): caesar cipher shift key
    Returns:
        cipherText(list): list of ciphertext of each plaintext (in bytes)
    """
    cipherText = []
    for p in plainText:
        # remove spaces in plaintext
        p = p.replace(' ', '')
        if p.islower():
            offset = 97
        elif p.isupper():
            offset = 65
        else:
            p = p.lower()
            offset = 97
        # cipher = ''
        # for c in p:
        #     if c.islower():
        #         temp = (ord(c) - 97 + key)%26 + 97
        #     elif c.isupper():
        #         temp = (ord(c) - 65 + key)%26 + 65
        #     if c !='\n':
        #         cipher+= chr(temp)
        # cipherText.append(cipher+'\n')
        # or
        cipher = (np.fromstring(p, np.uint8) - offset + key)%26 + offset
        cipherText.append(cipher.tostring() + b'\n')

    with open("caesar_cipher.txt", 'wb') as f:
        f.writelines(cipherText)
    return cipherText
