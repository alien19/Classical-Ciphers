import numpy as np
def encrypt_hill(plainText, key):
    """
    encrypts plaintext with hill cipher method and writes the output in hill_cipher.txt
    Args:
        plainText(list): list of plaintext in hill_plain.txt file 
                                [each line in the file is a list element]
        key(list): hill cipher key matrix
    Returns:
        cipherText(list): list of ciphertexts opposite to each plaintext
    """
    if len(key) == 4:
        k = np.array(list(map(int, key))).reshape((2, 2))
        r = 2
    elif len(key) == 9:
        k =np.array(list(map(int, key))).reshape((3,3))
        r = 3
    cipherText = []
    # r = key.shape[0]
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

        if r==2 and len(p)%2:
            p = p + 'x'
        elif r==3:
            if len(p)%3==2:
                p = p + 'x'
            elif len(p)%3==1:
                p = p + 'xx'
        p_nums = np.fromstring(p, np.uint8) - offset
        res_b = b''
        for i in range(0, p_nums.shape[0], r):
            res = np.dot(k.astype('int32'), p_nums[i:i+r].reshape(-1, 1).astype('int32'))
            res = ((res%26) + offset).reshape(-1,).astype('uint8')
            res_b = b''.join((res_b, b''.join(res))) 
        
        cipherText.append(res_b + b'\n')
    if r==2:
        with open("hill_cipher_2x2.txt", 'wb') as f:
            f.writelines(cipherText)
    if r==3:
        with open("hill_cipher_3x3.txt", 'wb') as f:
            f.writelines(cipherText)
    return cipherText