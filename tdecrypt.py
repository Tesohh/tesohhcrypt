import tesohhcrypt

text = input('Encrypted Text: ').lstrip()
rk = input('Key1: ').lstrip()
rv = input('Key2: ').lstrip()
key = tesohhcrypt.makeDictFromKeys(rk, rv) # convert to a TCrypt-Readable format 
decryptage = tesohhcrypt.decrypt(text, key) # decrypt using the converted, TCrypt-Readable format
print(decryptage)