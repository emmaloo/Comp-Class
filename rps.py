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
elif player == "r" and computer == "p":
	print("You lose! The paper covered your rock!")
elif player == "p" and computer == "r":
	print("You win! Your paper covered the rock!")
elif player =="p" and computer == "s":
	print("You lose! Your paper got shredded!")
elif player == "s" and computer == "r":
	print("You lose! Your scissors are dull!")
elif player == "s" and computer == "p":
	print("You win! Your scissors mutilated the paper!")
print(player, "vs", computer)

chosen = randint(1,3)
print(end=" ")


