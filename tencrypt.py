import tesohhcrypt
import sys

rk, rv = tesohhcrypt.createKey() # creates Key1 (rk) and Key2 (rv)

prompt = input('Fixed Key1 (leave empty for new key): ')
# print(prompt)
if prompt != '':
	rk = prompt # in case a user wants to use a fixed Key1, set rk to the custom key
else:
	sys.stdout.write(rk + '\n')

prompt = input('Fixed Key2 (leave empty for new key): ')
# print(prompt)
if prompt != '':
	rv = prompt # in case a user wants to use a fixed Key1, set rk to the custom key
else:
	sys.stdout.write(rv + '\n')

key = tesohhcrypt.makeDictFromKeys(rk, rv) # convert to a TCrypt-Readable format

text = input('Text to encrypt (most english characters): ')
cryptage = tesohhcrypt.crypt(text, key) # encrypt using the converted, TCrypt-Readable format
print('Encrypted Text:', cryptage)
# print('Key1:', rk)
# print('Key2:', rv)

if "--save" in sys.argv:
	with open('tcrypt.txt', 'w') as f:
		f.write(f'{cryptage}\n{rk}\n{rv}') # if someone wants to save the data to a file
		print('Saved output to ./tcrypt.txt')