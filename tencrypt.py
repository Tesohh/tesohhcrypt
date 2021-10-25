import tesohhcrypt
from colorama import Fore, Back, Style

rk, rv = tesohhcrypt.createKey()
key = tesohhcrypt.makeDictFromKeys(rk, rv)
text = input('Text to encrypt (most english characters): ')
cryptage = tesohhcrypt.crypt(text, key)
print('Encrypted Text:' + Fore.MAGENTA, cryptage, Fore.RESET)
print('Key1:'+ Fore.MAGENTA, rk, Fore.RESET)
print('Key2:'+ Fore.MAGENTA, rv, Fore.RESET)