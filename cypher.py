alphaboot = 26

def getType():
	while True:
		print('Are you going to encrypt or decrypt?')
		mode = input().lower()
		if mode in 'encrypt e decrypt d'.split():
			return mode
		else:
			print('Enter "encrypt" or "e" or "decrypt" or "d".')

def getMessage():
	print('Message:')
	return input()

def getKey():
	key = 0
	while True:
		print('Enter the key number (1-%s)'%(alphaboot))
		key = int(input())
		if (key >= 1 and key <= alphaboot):
			return key

def getEncryptorDecrypt(type, message, key):
	if type[0] == 'd':
		key = -key
	translated =""

	for symbol in message:
		if symbol.isalpha():
			num = ord(symbol)
			num += key

			if symbol.isupper():
				if num > ord('Z'):
					num -= 26
				elif num < ord('A'):
					num += 26
			elif symbol.islower():
				if num > ord('z'):
					num -= 26
				elif num < ord('a'):
					num += 26
				translated += chr(num)
			else:
				translated += symbol
		return translated


type = getType()
message = getMessage()
key = getKey()


print('Translation:')
print(getEncryptorDecrypt(type, message, key))




