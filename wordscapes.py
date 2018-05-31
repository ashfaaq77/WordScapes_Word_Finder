file = open('words.csv', 'r')

try:
	alpha = str(input('Enter the following characters: (with a space between each character) \n').lower())
except ValueError:
	print("Wrong input")


characters = alpha.split(" ")

length = len(characters)


words_found = []
char_check = characters[:]

def check_word(word):
	count = 0
	for i in word:
		if i in char_check:
			count += 1
			char_check.remove(i)

	if count>=3 and len(word)-1==count:
		words_found.append(word)



for i in file:
	if len(str(i))<=length+1:
		check_word(str(i))
	char_check = characters[:]


file.close()

print(words_found)
			