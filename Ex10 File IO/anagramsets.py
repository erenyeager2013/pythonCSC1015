# A program that asks the user to enter a word length and a filename, The program will search a file for sets of words that are that length and are anagrams of each other, and will write the results to a file with the given filename.
# Vincent T Mukwevo
# 03/05/2024

def dictin(word):

    # Counts the occurrences of each letter in a word and records them in a dictionary.
    worddy = {}
    for ch in word:
        if ch in worddy:
            worddy[ch] += 1
        else:
            worddy[ch] = 1
    return worddy

def anagramfinder(search, word_list):
    
    # Finds anagrams of a given search word in a list of words.
    search = search.lower()
    criterion = len(search)
    diction1 = dictin(search)
    anagrams = []

    for line in word_list:
        line = line.strip().lower()

        if len(line) == criterion :
            diction2 = dictin(line)
            if diction1 == diction2:
                anagrams.append(line)

    anagrams.sort()
    return anagrams

# Obtain user input
length = int(input('Enter word length:\n'))
tryfilename = input('Enter file name:\n')

# Read the dictionary file into a list
with open('EnglishWords.txt', 'r', encoding='UTF-8') as dictionary:
    word_list = [word.strip() for word in dictionary]

# Process each word in the dictionary
with open(tryfilename, 'w') as outfile:
    begin = False
    for word in word_list:
        if word == 'start':
            begin = True
        if begin and len(word) == length:
            anag = anagramfinder(word, word_list)
            if len(anag) > 1:
              print(anag, file=outfile)

# Sorting the anagrams in output file
sortfile = open(tryfilename, 'r') 
sorting =[]
for line in sortfile: sorting.append(line)
sorting.sort()
sortfile.close()
sorted = open(tryfilename, 'w') 
for pair in sorting:
   print(pair, file=sorted, end='')
sorted.close()
print(f"Results written to '{tryfilename}'.")