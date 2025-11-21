# A program that accepts a sentence as input and translates it to a variant of Pig Latin

sentence = input('Enter a sentence:\n')
sentence = sentence.lower()
new_sentence = ''
new_word = ''
start = 0

for i in range(len(sentence) ):
    if sentence[i] == ' ' or i == len(sentence):
        word = sentence[start:(i)]
        start = i + 1

        if word[0] in 'aeiou':
            new_sentence = new_sentence + word + 'way '
        else:
            for vtm in range(len(word)):
                if word[vtm] not in 'aeiou':
                    # Store consonants
                    new_word = new_word + word[vtm]
                else:
                    new_sentence = new_sentence + word[vtm:] + 'a' + new_word + 'ay '
                    new_word = ''
                    break

print(new_sentence)