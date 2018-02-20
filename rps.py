from random import randint
butts = input("Rock destroys scissors, paper envelops rock, and scissors shred paper! Press enter to begin!")
player = input("rock(r), paper(p), scissors(s)?")
chosen = randint(1,3)

if chosen == 1:
	computer = "r"
elif chosen == 2:
	computer = "p"
elif chosen == 3:
	computer = "s"

if player == computer:
	print("Whoops! I guess it's a  D R A W!")
elif player == "r" and computer == "s":
	print("You win! Your rock dulled the scissors!")
	rock = open('rockart.txt')
	for line in rock:
		print(line)
elif player == "r" and computer == "p":
	print("You lose! The paper covered your rock!")
	loser = open('paperart.txt')
	for line in loser:
		print(line)
elif player == "p" and computer == "r":
	print("You win! Your paper covered the rock!")
	paper = open('paperart.txt')
	for line in paper:
		print(line)
elif player =="p" and computer == "s":
	print("You lose! Your paper got shredded!")
	ghhh = open('scissorsart.txt')
	for line in ghhh:
		print(line)
elif player == "s" and computer == "r":
	print("You lose! Your scissors are dull!")
	lll = open('rockart.txt')
	for line in lll:
		print(line)
elif player == "s" and computer == "p":
	print("You win! Your scissors mutilated the paper!")
	cut = open('scissorsart.txt')
	for line in cut:
		print(line)
print(player, "vs", computer)

chosen = randint(1,3)
print(end=" ")


