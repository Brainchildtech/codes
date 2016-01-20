import random

myWords = ["brain", "child", "monkey", "flower", "fish", "hello", "good"]


c = "y"

while (c == "y" or c == "Y"):
	secret = random.choice(myWords)
	guesses = ''
	turns = 5
	while turns > 0:
		count= 0
	
		for letter in secret:
			if letter in guesses:
				print letter,
			else:
				print '_',
				count += 1



		if count == 0:
			print 'You win!'
			c = raw_input("Do you want to continue : ")
		        break
   	
       
		guess = raw_input('guess a letter: ')
		guesses += guess
		if guess not in secret:
			turns -= 1
			print 'wrong.'
			print turns, 'more turns'
			if turns < 1: print ' --------      '
		        if turns < 1: print '        |      '
		        if turns < 1: print '        |      '
		        if turns < 5: print '        O      '
		        if turns < 4: print '      \_|_/    '
		        if turns < 3: print '        |      '
		        if turns < 2: print '       / \     '
		        if turns < 1: print '      0   0    '
		        if turns < 1: print 'The game is over.Try another chance'
		        if turns == 0:
				print 'The answer is', secret
				c = raw_input("Do you want to continue : ")
