import random

# Random Game Name Generator

firstL=["Super","evil","Pro","Sad","Golden","Best","Beautiful","Green","Blue","Fat","Old","Wise","Young","First","Big","fast","Small","Smart","tiny"]

secondL=["Jumper","Killer","Noob","Man","Hero","devil","Thief","Kid","Dragon","skeleton","Archer","Runner","Jumper","Knight","Adventurer","Warrior","Mage","Druid","Ninja"]

first=random.choice(firstL)
second=random.choice(secondL)
name=first+"_"+second

print "Your Random Game Name is {}".format(name)


raw_input()
