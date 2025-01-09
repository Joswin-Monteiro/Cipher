# TODO : Immplement this cipher for symbols and numbers

num_to_str = {
    0: 'a',
    1: 'b',
    2: 'c',
    3: 'd',
    4: 'e',
    5: 'f',
    6: 'g',
    7: 'h',
    8: 'i',
    9: 'j',
    10: 'k',
    11: 'l',
    12: 'm',
    13: 'n',
    14: 'o',
    15: 'p',
    16: 'q',
    17: 'r',
    18: 's',
    19: 't',
    20: 'u',
    21: 'v',
    22: 'w',
    23: 'x',
    24: 'y',
    25: 'z',
}

str_to_num = {
    'a': 0, 
    'b': 1, 
    'c': 2, 
    'd': 3, 
    'e': 4, 
    'f': 5, 
    'g': 6, 
    'h': 7, 
    'i': 8, 
    'j': 9, 
    'k': 10,  
    'l': 11,  
    'm': 12, 
    'n': 13, 
    'o': 14, 
    'p': 15, 
    'q': 16, 
    'r': 17, 
    's': 18, 
    't': 19, 
    'u': 20, 
    'v': 21, 
    'w': 22, 
    'x': 23, 
    'y': 24, 
    'z': 25, 
}

def encrypt(text: str) -> str:
    encrypted_text = ""
    is_upper_case = False
    for letter in text:
        if letter == ' ':
            encrypted_text += ' '
            continue
        if letter.isupper():
            is_upper_case = True
            letter = letter.lower()
        val = str_to_num[letter]
        encrypted_value = (val + 3) % 26
        if is_upper_case:
            encrypted_text += (num_to_str[encrypted_value]).upper()
            is_upper_case = False
        else:
            encrypted_text += num_to_str[encrypted_value]
            is_upper_case = False
    return encrypted_text

def decrypt(text: int) -> str:
    decrypted_text = ""
    is_upper_case = False
    for letter in text:
        if letter == ' ':
            decrypted_text += ' '
            continue
        if letter.isupper():
            is_upper_case = True
            letter = letter.lower()
        val = str_to_num[letter]
        decrypted_value = (val - 3) % 26
        if is_upper_case:
            decrypted_text += (num_to_str[decrypted_value]).upper()
            is_upper_case = False
        else:
            decrypted_text += num_to_str[decrypted_value]
            is_upper_case = False
    return decrypted_text

def main():
    text = "Hello World"
    encrypted_text = encrypt(text)
    print(encrypted_text)
    decrypted_text = decrypt(encrypted_text)
    print(decrypted_text)

if __name__ == "__main__":
    main()
