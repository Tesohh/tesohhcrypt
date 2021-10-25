import tesohhcrypt
from colorama import Fore, Back, Style

text = input('Encrypted Text: ').lstrip()
rk = input('Key1: ').lstrip()
rv = input('Key2: ').lstrip()
key = tesohhcrypt.makeDictFromKeys(rk, rv)
decryptage = tesohhcrypt.decrypt(text, key)
print(Fore.BLUE + decryptage)