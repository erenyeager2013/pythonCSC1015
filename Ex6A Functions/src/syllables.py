# Given a word, calculate how many syllables it contains.
# Vincent Mukwevo T 
# 30/03/2024

def count_syllables(word):
    count = 0
    # Your code here.
    vowels = ('a', 'e', 'i', 'o','u','y')
    seq = 0
    for i in word:
        if i in vowels:
            count = count +1
        elif (i not in vowels) and count > 0:
            count = 0
            seq = seq + 1

    if word[len(word)-1] in 'e' and seq > 0:
        pass   
    elif  word[len(word)-1] in vowels:
        seq = seq + 1
    return seq

def main():
    word= ''
    while word != 'q':
       word = input('Enter a word (or \'q\' to quit):\n')
       # Your code here.
       if word == 'q':
         pass
       else:
         syllables = count_syllables(word)
         if syllables== 1:
              print('The word \'{0}\' has {1} syllable.\n'.format(word,syllables))
         else:
            print('The word \'{0}\' has {1} syllables.\n'.format(word,syllables))
# Do not modify.
if __name__ == '__main__':
    main()

