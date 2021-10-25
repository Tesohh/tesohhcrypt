import random

print('-- TesohhCrypt v1.0 --')
if __name__ == "__main__":
	print('easter egg found')


def crypt(text:str, key:dict):
	'''Crypts plain text.
	\nRemember, the `key` must be the converted one through `makeDictFromKeys()`'''
	# text = text.lower()
	text = text.replace(' ', '|')
	newText = ""
	for i in text:
		newText += key[i]
	return newText

def decrypt(text:str, key:dict):
	'''Decrypts Tesohh-Crypted text.
	\nRemember, the `key` must be the converted one through `makeDictFromKeys()`'''
	newText = ""
	invertedKey = dict((v,k) for k,v in key.items())
	for i in text:
		newText += invertedKey[i]
	return newText.replace('|', ' ')

def createKey():
	'''Creates a `Key1` and a `Key2`.'''
	ak = "ABCDEFGHIJKLMNOPQRSTUVWXYZ{}\"abcdefghijklmnopqrstuvwxyz`1234567890-=~!@#$%^&*()_+[];:',.<>/?|\\" #change this if you want to add new characters
	# note that adding more characters will make the keys longer.
	av = ak
	# keyDict = {}

	ak = list(ak)
	av = list(av)
	for i in range(100):
		random.shuffle(ak)
		random.shuffle(av)
	rk = ''.join(ak)
	rv = ''.join(av)
	return rk, rv

def makeDictFromKeys(rk:str, rv:str):
	'''Creates a TCrypt-Readable Key.'''
	result = {}
	for i in range(len(rk)):
		result[rk[i]] = rv[i]
	return result