# 30 December 2021

import random



tot = 1000
wincount_intialguess = 0
wincount = 0


def monty():
	prize = random.randint(1,3)

	guess = random.randint(1,3)

	l = [1,2,3]
	try:
		l.remove(prize)
		l.remove(guess)

	except ValueError:
		pass

	if len(l)>1:
		opendoorindex = random.randint(0,1)
	else:
		opendoorindex = 0

	opendoor = l[opendoorindex]

	l2 = [1,2,3]
	l2.remove(opendoor)
	l2.remove(guess)
	switchguess = l2[0]


	#print(prize, guess, opendoor, finalguess)

	if prize == switchguess:
		global wincount
		wincount += 1


	if prize == guess:
		global wincount_intialguess
		wincount_intialguess += 1



for i in range(0, tot):
	monty()

print("stay: ", (wincount_intialguess*100)/tot)
print("switch: ", (wincount*100)/tot)

