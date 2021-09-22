#Ceasar Cipher Encryption - Decryption

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
plaintext = str(input('Plaintext : ')).replace(" ","")
key = str(input('Key : ')).replace(" ","")

plaintext = plaintext.upper()
key = key.upper()

alpha_dict = {}
for i,j in enumerate( alpha):
    alpha_dict[i] = j

# Making lengths of plain & CipherText equal
key_same_len = key
while len(key_same_len) != len(plaintext):
    for j,k in enumerate(key):
        if len(key_same_len) != len(plaintext):
            key_same_len += k

#Encryption
index_plaintext = []
index_key = []
cipher_ind = []

lis_plain = list(alpha_dict.keys())
lis_keys = list(alpha_dict.values())

for i in (plaintext):
    index_plaintext.append(lis_keys.index(i))

for i in (key_same_len):
    index_key.append(lis_keys.index(i))

for i,j in zip(index_plaintext,index_key):
    cipher_ind.append((i+j) % 26)

print("Encrypted Text is : ")

for i in cipher_ind:
    print(alpha_dict[i],end="")

print("\n")



# Decryption
plaintext = str(input('Enter CipherText : ')).replace(" ","")
key = str(input('Key : ')).replace(" ","")

plaintext = plaintext.upper()
key = key.upper()

alpha_dict = {}
for i,j in enumerate( alpha):
    alpha_dict[i] = j

# Making lengths of plain & CipherText equal
key_same_len = key
while len(key_same_len) != len(plaintext):
    for j,k in enumerate(key):
        if len(key_same_len) != len(plaintext):
            key_same_len += k

print("\n")

#Decryption
index_plaintext = []
index_key = []
cipher_ind = []

lis_plain = list(alpha_dict.keys())
lis_keys = list(alpha_dict.values())

for i in (plaintext):
    index_plaintext.append(lis_keys.index(i))

for i in (key_same_len):
    index_key.append(lis_keys.index(i))

for i,j in zip(index_plaintext,index_key):
    cipher_ind.append((i-j) % 26)

print("Decrypted Text is : ")

for i in cipher_ind:
    print(alpha_dict[i],end="")