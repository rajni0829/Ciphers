import random

def c_monoalphabetic(alpha,key,pt):
  ct = ''
  for i in pt:
    ind = alpha.index(i.upper())
    ct += key[ind]
  return ct


def d_monoalphabetic(alpha,key,cptxt):
  dt = ''
  for i in cptxt:
    ind = key.index(i.upper())
    dt += alpha[ind]
  return dt


pt = input("Plaintext : ")
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
key = ''.join(random.sample(alpha,len(alpha)))


cptxt = c_monoalphabetic(alpha,key,pt)
print(cptxt)
print(d_monoalphabetic(alpha,key,cptxt))