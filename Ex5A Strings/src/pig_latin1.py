# A program that accepts a sentence as input and translates it to a variant of Pig Latin
# Vincent T Mukwevo MKWVIN004
# 20/03/2024

eng = input('Enter a sentence:\n')
# initialising some variables
sente = ""
sente1 = ''
end = 0
# main loop for words in eng sentence
for i in range (0,len(eng)-1):
    if (eng[i] == ' '):
        # creating word by splitting from main eng sentence
        word = eng[end:i]
        end = i + 1
        # checking if word starts with vowel and formatting the word
        if word[0] == 'a' or  word[0] == 'e' or  word[0] == 'i' or  word[0] == 'o' or  word[0] == 'u':
            sente = sente + word + 'way'
            print('sentence1 is: ' + sente)
        else:
            # word does not start with vowel 
            # loop to check the sequence of consonants
            for v in range (len(word)-1):
                if word[v] != 'a' or  word[v] != 'e' or  word[v] != 'i' or  word[v] != 'o' or  word[v] != 'u':
                    # variable to store consonants
                    sente1 = sente1 + word[v] 
                else:
                    sente = word[v:] + sente1 + 'ay'
                    print('sentence is: ' + sente)
    else:
        continue
# printing pig-latin sentence
print('sentence is: ' + sente)