import random as r

KEY_LGTH = 5
test_str = 'The quick brown fox jumps over the lazy dog.'

def create_key(key_lgth):
    return [r.randint(1, 9) for _ in range(key_lgth)]

def encrypt(input_str, key):
    key_lgth = len(key)
    encrypted_str = ''
    for i in range(len(input_str)):
        encrypted_str += chr(ord(input_str[i]) + key[i % key_lgth])
    return encrypted_str

def decrypt(encrypted_str, key):
    key_lgth = len(key)
    output_str = ''
    for i in range(len(encrypted_str)):
        output_str += chr(ord(encrypted_str[i]) - key[i % key_lgth])
    return output_str

key = create_key(KEY_LGTH)
print('N-Key Encryption')
print(f'key:         {key}')
print(f'test string: {test_str}')
enc_str = encrypt(test_str, key)
print(f'encrypted:   {enc_str}')
dec_str = decrypt(enc_str, key)
print(f'decrypted:   {test_str}')

