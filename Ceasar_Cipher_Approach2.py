
def caesar_cipher(plaintext):
  s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  key = 3
  ciphertext = ""
  for i in (plaintext):
    ind = s.index(i.upper())
    c = (ind + key) % 26
    ciphertext += s[c]
  return ciphertext


def caesar_decipher(ciphertxt):
  st = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  key = 3
  deciphertext = ""
  for i in ciphertxt:
    ind = st.index(i.upper())
    d = (ind - key) % 26
    deciphertext += st[d]
  return deciphertext

plaintext = input("Enter Plaintext : ")
ciphertxt = caesar_cipher(plaintext)
print(ciphertxt)

print(caesar_decipher(ciphertxt))
