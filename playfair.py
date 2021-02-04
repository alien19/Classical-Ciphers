import numpy as np
from collections import OrderedDict

# key = []
# key[:0]  = input()
# alpha = [chr(c) for c in range(97, 123)]
# alpha.remove('j')
# pf_matrix = np.array(list(OrderedDict.fromkeys(key + alpha))).reshape(5,5)


def encrypt_playfair(plainText, key):
    """
    encrypts plaintext with playfair cipher method and writes the output in playfair_cipher.txt
    Args:
        plainText(list): list of plaintext in playfair_plain.txt file 
                                [each line in the file is a list element]
        key(list): playfair cipher key
    Returns:
        cipherText(list): list of ciphertext of each plaintext
    """    
    if key.islower():
        alpha = [chr(c) for c in range(97, 123)]
        alpha.remove('j')
    elif key.isupper():
        alpha = [chr(c) for c in range(65, 91)]
        alpha.remove('J')
    else:
        key = key.lower()
        alpha = [chr(c) for c in range(97, 123)]
        alpha.remove('j')
    k = []        
    k[:0] = key
    pf_matrix = np.array(list(OrderedDict.fromkeys(k + alpha))).reshape(5,5)

    total_par = []
    for p in plainText:
        p = p.replace('\n', '')
        par = []
        for i in range(0, len(p)+1, 2):
            try:
                if p[i]==p[i+1]:    # if there are similar consecutive
                    p = p[:i+1] + 'x' + p[i+1:]
                    if len(p)%2:
                        p = p + 'x'
                par.append(p[i:i+2])
            except IndexError:
                break
        total_par.append(par)

    cipherText = []
    for text in total_par:
        cipher = ''
        for pair in text:
            pair = pair.replace('j', 'i')
            first_idx = np.argwhere(pf_matrix==pair[0])[0]
            sec_idx = np.argwhere(pf_matrix==pair[1])[0]
            if first_idx[0]==sec_idx[0]:    # letters are in the same row
                cipher += pf_matrix[first_idx[0], (first_idx[1]+1)%5] + pf_matrix[sec_idx[0], (sec_idx[1]+1)%5]
            elif first_idx[1]==sec_idx[1]:    # letters are in the same column
                cipher += pf_matrix[(first_idx[0]+1)%5, first_idx[1]] + pf_matrix[(sec_idx[0]+1)%5, sec_idx[1]]
            else:
                cipher += pf_matrix[first_idx[0], sec_idx[1]] + pf_matrix[sec_idx[0], first_idx[1]]
        cipherText.append(cipher+'\n')


    with open("playfair_cipher.txt", 'w') as f:
        f.writelines(cipherText)
    return cipherText


