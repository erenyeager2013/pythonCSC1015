# A program that accepts a sentence as input and translates it to a variant of Pig Latin

sente = input('Enter a sentence:\n')
sente = sente.lower()
new_sente = ''
new_word = ''
start = 0
spac = 0
for i in range(len(sente)-1):
    if sente[i] == ' ' or (i == (len(sente)-1)):
        word = sente[start:(i)]
        start = i + 1

        if word[0] in ('aeiou'):
            new_sente = new_sente + word + 'way '
        else:
              for v in range (len(word)-1):
                if word[v] not in ('aeiou'):
                    # variable to store consonants
                    new_word = new_word + word[v] 
                else:
                   new_sente =new_sente + word[v:] + 'a' + new_word + 'ay '
                   new_word =''
                   break
print(new_sente)     