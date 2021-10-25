import random

def crypt(text:str, key:dict):
	text = text.replace(' ', '|')
	newText = ""
	for i in text:
		newText += key[i]
	return newText

def decrypt(text:str, key:dict):
	newText = ""
	invertedKey = dict((v,k) for k,v in key.items())
	for i in text:
		newText += invertedKey[i]
	return newText.replace('|', ' ')

def createKey():
	ak = "abcdefghijklmnopqrstuvwxyz`1234567890-=~!@#$%^&*()_+[];:',.<>/?|"
	av = "abcdefghijklmnopqrstuvwxyz`1234567890-=~!@#$%^&*()_+[];:',.<>/?|"
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
	result = {}
	for i in range(len(rk)):
		result[rk[i]] = rv[i]
	return result