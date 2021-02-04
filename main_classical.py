import os
import numpy as np
from caesar import encrypt_caesar
from vigenere import encrypt_vigenere
from vernam import encrypt_vernam
from hill import encrypt_hill
from playfair import encrypt_playfair

curdir = os.getcwd()

i = input('Caesar cipher key: ')
playfair_key = input('Play Fair Cipher: ')
vigenere_mode = int(input('Enter Vigenere Cipher mode: 1 for auto 0 for repetition: '))
vigenere_key = input('Vigenere Cipher key: ')
hill_key = input('Hill cipher key: ').split(' ')
# hill_key_2 = np.array([[5,17],[8,3]])
# hill_key_3 = np.array([[2,4,12],[9,1,6],[7,5,3]])
vernam_key = np.frombuffer(input('Vernam cipher key: ').encode(), np.uint8)


os.chdir('Classical Ciphers\Input Files\Caesar')
with open("caesar_plain.txt", 'r') as f:   
    plainText = f.readlines()
caesar_cipherText = encrypt_caesar(plainText, key=int(i))
os.chdir(curdir)

os.chdir('Classical Ciphers\Input Files\PlayFair')
with open("playfair_plain.txt", 'r') as f:   
    plainText = f.readlines()
playfair_cipherText = encrypt_playfair(plainText, playfair_key)
os.chdir(curdir)

os.chdir('Classical Ciphers\Input Files\Vigenere')
with open("vigenere_plain.txt", 'r') as f:
    plainText = f.readlines()
vigenere_cipherText = encrypt_vigenere(plainText, vigenere_key, mode=vigenere_mode)
os.chdir(curdir)

os.chdir('Classical Ciphers\Input Files\Hill')
with open("hill_plain_3x3.txt", 'r') as f:
    plainText = f.readlines()
hill_cipherText = encrypt_hill(plainText, hill_key)
os.chdir(curdir)

os.chdir('Classical Ciphers\Input Files\Vernam')
# key = np.frombuffer(b'SPARTANS', np.uint8) - 65
with open("vernam_plain.txt", 'r') as f:
    plainText = f.readlines()
vernam_cipherText = encrypt_vernam(plainText, vernam_key)
os.chdir(curdir)
