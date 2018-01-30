text = input ("What should the cat say?")

def box(text):
	print('<:', text, ':>')

meowsay = open('meowart.txt')
box(text)
for line in meowsay:
	print(line, end='')


