# A program that searches a file for anagrams of a given word, printing the results in alphabetical order.
# Vincent T Mukwevo MKWVIN004
# 01/05/2024

print('***** Anagram Finder *****')
try:
 dictionary = open ('EnglishWords.txt','r', encoding = 'UTF-8')

#Obtaining search input
 search = str(input('Enter a word:\n'))
 search = search.lower()
 creterion = len(search)
 diction1= {}
 for ch in search:
         if ch in diction1:
             diction1[ch] += 1
         else:
             diction1[ch] = 1 
   
 anagrams = []
 # Code to find similar words to search input
 for line in dictionary:
     line = line.strip().lower()     
    
 # comparing the word from file to input
     if (len(line) == creterion) and (search != line):
          worddy = {}
          for ch in line:
             if ch in worddy:
                worddy[ch] += 1
             else:
                worddy[ch] = 1 
   
          if (diction1 == worddy):
             anagrams.append(line)   
 dictionary.close()
 anagrams.sort()
 if len(anagrams)>= 1:
    print(anagrams)  
 else:
     print('Sorry, anagrams of \'{0}\' could not be found.'.format(search))

except IOError:
    print('Sorry, could not find file \'EnglishWords.txt\'.')