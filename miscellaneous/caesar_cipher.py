def encrypt(input_str, offset):
    encrypted_str = ''
    for ch in input_str:
        encrypted_str += chr(ord(ch) + offset)
    return encrypted_str

def decrypt(encrypted_str, offset):
    output_str = ''
    for ch in encrypted_str:
        output_str += chr(ord(ch) - offset)
    return output_str

test_str = 'The quick brown fox jumps over the lazy dog.'

print('Caesar Cipher')
print(f'test string: {test_str}')
enc_str = encrypt(test_str, 5)
print(f'encrypted:   {enc_str}')
dec_str = decrypt(enc_str, 5)
print(f'decrypted:   {test_str}')
