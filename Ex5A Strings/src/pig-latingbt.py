# pig-latin
def to_pig_latin(word):
    vowels = 'aeiou'
    if word[0] in vowels:
        return word + 'way'
    else:
        for i, char in enumerate(word):
            if char in vowels:
                return word[i:] + 'a' + word[:i] + 'ay'
        # If no vowels found, just add "ay" to the end
        return word + 'ay'

def translate_to_pig_latin(sentence):
    words = sentence.lower().split()
    pig_latin_sentence = ' '.join(to_pig_latin(word) for word in words)
    return pig_latin_sentence

user_input = input('Enter a sentence:\n')
pig_latin_output = translate_to_pig_latin(user_input)
print("Pig Latin translation:", pig_latin_output)
