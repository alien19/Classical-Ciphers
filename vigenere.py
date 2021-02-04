import numpy as np

def encrypt_vigenere(plainText, key, mode:bool = True):
    """
    encrypts plaintext with vegenere cipher method and writes the output in vigenere_cipher.txt
    Args: 
        plainText(python list): list of plaintext in vigenere_plain.txt file
        key(str): key of vegenere cipher
        mode(bool): flag deciding the mode of the cipher 
                    - True: auto mode
                    - False: repeating mode
    Returns:
        cipherText(python list): list of ciphertext of each plaintext in bytes
    """
    # k = np.fromstring(key, np.uint8)
    cipherText = []
    for p in plainText:
        p = p.replace('\n', '')
        p = p.replace(' ', '')

        if p.islower():
            offset = 97
            k = np.fromstring(key.lower(), np.uint8) - 97
        elif p.isupper():
            offset = 65
            k = np.fromstring(key.upper(), np.uint8) - 65
        else:
            p = p.lower()
            k = np.fromstring(key.lower(), np.uint8) - 97
            offset = 97

        if not mode:    # repetition mode
            r = (len(p) - k.shape[0]) // k.shape[0] + 1
            k = np.repeat(k, repeats=r+1)
            cipher = (np.fromstring(p, np.uint8) - offset + k[:len(p)])%26 + offset
        else:           # auto mode
            r = len(p) - k.shape[0]
            k = np.append(k, np.array(list(p[:r].encode())) - offset)
            cipher = (np.fromstring(p, np.uint8) - offset + k[:len(p)])%26 + offset
        cipherText.append(cipher.astype('uint8').tostring() + b'\n')
    
    # cipherText = [c + b'\n' for c in cipherText]
    with open("vigenere_cipher.txt", 'wb') as f:
        f.writelines(cipherText)
    return cipherText