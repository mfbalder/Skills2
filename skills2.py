# Start time: 9:56pm
# End time: 11:04 (without bonuses)
import string

string1 = "I do not like green eggs and ham."
list1 = [2, 5, 12, 6, 1, -5, 8, 5, 6, -2, 2, 27]
list2 = [-5, 6, 4, 8, 15, 16, 23, 42, 2, 7]
words = ["I", "do", "not", "like", "green", "eggs", "and", "ham", "I", "do", "not", "like", "them", "Sam", "I", "am"]

"""
Write a function that takes a string and produces a dictionary with
all distinct elements as the keys, and the number of each element as
the value
Bonus: do the same for a file (i.e. twain.txt)
"""
def count_unique(string1):
	# Yes
	letter_dict = {}
	for char in string1:
		if char.isalpha():
			letter_dict[char] = letter_dict.get(char, 0) + 1
	return letter_dict

def count_unique_file(filename):
	# Yes, but what counts as a distinct element? A word? A letter?
	letter_dict = {}
	f = open(filename)
	for line in f:
		line = line.strip().split()
		for word in line:
			word = word.lower()
			if word.isalpha():
				letter_dict[word] = letter_dict.get(word, 0) + 1
	return letter_dict




"""
Given two lists, (without using the keywords 'if __ in ____' or the method 'index')
return a list of all common items shared between both lists
"""
def common_items(list1, list2):
	# Yes
	common = set.intersection(set(list1), set(list2))
	return list(common)


"""
Given two lists, (without using 'if __ in ____' or 'index')
return a list of all common items shared between both lists. This time,
use a dictionary as part of your solution.
"""
def common_items2(list1, list2):
	# yes, but dicey
    common = {}
    l = []
    for item in list1:
    	common.setdefault(item, 1)
    for item in list2:
    	common[item] = common.get(item, 0) + 1
    for item, value in common.items():
    	if value >= 2:
    		l.append(item)
    return l



"""
Given a list of numbers, return list of number pairs that sum to zero
"""
def sum_zero(list1): 
	# Dicey
	l = []
	for i in list1:
		for j in list1:
			if i + j == 0:
				l.append((i, j))
	return list(set(l))

def sum_zero2(list1):
	# print [[(x, y) if x + y == 0 for x in list1] for y in list1]




"""
Given a list of words, return a list of words with duplicates removed
"""
def find_duplicates(words):
	# Yes
    return list(set(words))


"""
Given a list of words, print the words in ascending order of length
Bonus: do it on a file instead of the list provided
Bonus: print the words in alphabetical order in ascending order of length
"""
def word_length(words):
	# Yes
    l = sorted(sorted(words), key=lambda x: len(x))
    for word in l:
    	print word

def word_length_file(filename):
	# Yes
	f = open(filename)
	whole_text = f.read().strip().split()
	whole_text = [word.strip(string.punctuation) for word in whole_text]
	l = sorted(sorted(whole_text), key=lambda x: len(x))
	for word in l:
		print word





"""
Here's a table of English to Pirate translations
English     Pirate

sir         matey
hotel       fleabag inn
student     swabbie
boy         matey
madam       proud beauty
professor   foul blaggart
restaurant  galley
your        yer
excuse      arr
students    swabbies
are         be
lawyer      foul blaggart
the         th'
restroom    head
my          me
hello       avast
is          be
man         matey

Write a program that asks the user to type in a sentence and then
print the sentece translated to pirate.
"""

def translate_to_pirate():
	eng_to_pirate = {"sir": "matey", "hotel": "fleabag inn", "student": "swabble", "boy": "matey", "madam": "proud beauty",
					"professor": "foul blaggart", "restaurant": "galley", "your": "yer", "excuse": "arr", "students": "swabbles", 
					"are": "be", "lawyer": "foul blaggart", "the": "th'", "restroom": "head", "my": "me", "hello": "avast",
					"is": "be", "man": "matey"}
	sentence = raw_input("Please enter a sentence to translate: ")
	sentence = sentence.split()
	translation = [eng_to_pirate.get(word.strip(string.punctuation), word.strip(string.punctuation)) for word in sentence]
	# translation = []
	# for word in sentence:
	# 	word = word.strip(string.punctuation)
	# 	translation.append(eng_to_pirate.get(word, word))

	# for word in sentence:
	# 	word = word.strip(string.punctuation)
	# 	if word in eng_to_pirate:
	# 		translation.append(eng_to_pirate[word])
	# 	else:
	# 		translation.append(word)
	return " ".join(translation)


def translate2():
	instructions = """
	English     Pirate

sir         matey
hotel       fleabag inn
student     swabbie
boy         matey
madam       proud beauty
professor   foul blaggart
restaurant  galley
your        yer
excuse      arr
students    swabbies
are         be
lawyer      foul blaggart
the         th'
restroom    head
my          me
hello       avast
is          be
man         matey"""
	eng_to_pirate = {}
	words = instructions.split('\n')
	print words
	# for i in range(2, len(words) - 1, 2):
	# 	eng_to_pirate[words[i]] = words[i + 1] 
	# 	print eng_to_pirate




