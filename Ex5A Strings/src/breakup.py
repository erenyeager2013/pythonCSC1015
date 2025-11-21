# A program that accepts a sentence as input and that outputs it as a comma-separated list of lowercase words with a full-stop at the end.

sente = input('Enter a sentence: \n')
sente = sente.lower()
print('The word list:',sente.replace(' ',', '), end='.')