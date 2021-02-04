import numpy as np
def encrypt_vernam(plainText, key):
    """
    encrypts plaintext with vernam cipher method and writes the output in vernam_cipher.txt
    Args:
        plainText(list): list of plaintext in vernam_plain.txt file 
                                [each line in the file is a list element]
        key(int): vernam cipher key
    Returns:
        cipherText(list): list of ciphertext of each plaintext (in bytes)
    """
    cipherText = []
    for p in plainText:
        p = p.replace('\n', '')
        p = p.replace(' ', '')
        # offset = 65
        if p.islower():
            offset = 97
        elif p.isupper():
            offset = 65
        else:
            p = p.lower()
            offset = 97

        p_nums = np.fromstring(p, np.uint8) - offset     
        cipher = ((p_nums.astype('int32')^(key.astype('int32') - offset) )%26 + offset).astype('uint8')
        cipherText.append(cipher.tostring() + b'\n')

    with open("vernam_cipher.txt", 'wb') as f:
        f.writelines(cipherText)
    return cipherText