with open("scrabble.txt", 'r') as f:
	count = 0
	for line in f:
		if count > 5:
			break
		print(line)
		count += 1

my_dictionary = {'a':1,'b':3,'c':3,'d':2,'e':1,'f':4,
'g':2,'h':4,'i':1,'j':8,'k':5,'l':1,'m':3,'n':1,'o':1,
'p':3,'q':10,'r':1,'s':1,'t':1,'u':1,'v':4,'w':4,'x':8,
'y':4,'z':10}

def value(word):
# do code here
	return 5
print(value('zq'))

# 1) Write a program to compute the scrabble tile
#	 score of a given string input
#
# 2) Write a program to compute all "valid scrabble"
#	 words that you couldd make using all characters
#	 from an input string. Returns a list of valid
#	 words. If you can't make any words, return an
#	 empty list.
#	 example: valid_mords("RRAACCE") = ["RACECAR"]
#
# 3) The game of ghost is played by taking turns
#	 with a partner to add a letter to an increasingly
#	 long word. The first person to make a valid scrabble
#	 of length 3 or more loses.
#	 You must be thinking of a valid word when you name a letter.
#    write a game that implements ghost
#    addendum: write a bot to play ghost against you.

