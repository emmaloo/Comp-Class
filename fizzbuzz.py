howfartogo = input("How far do we want to go?")

for i in range(int(howfartogo)):
	if i%3 == 0 and i%5 == 0:
		print('Fizzbuzz')
	elif i%3 == 0:
		print('Fizz')
	elif i%5 == 0:
		print('Buzz')
	else:
		print(i)

