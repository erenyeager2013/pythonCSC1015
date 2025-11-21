# A program with function that can be used to determine if a given pattern matches a given word
# Vincent T Mukwevo MKWVIN004
# 24/04/2024

def match(pattern, word) :
    if len(pattern)> 0 and len(word)> 0:
        if pattern[0] != '*':
            if (pattern[0] == word[0]) or (pattern[0] == '?'):
                pattern = pattern[1:]
                word = word[1:]
                return (True and (match(pattern,word)))
            else: return False
        elif pattern[0] == '*':
            if (len(pattern)>=3):
                if (pattern[1] == word[1]):
                    pattern = pattern[2:]
                    word = word[2:]
                    return (True and (match(pattern,word)))
                else: return False
            elif not(len(pattern)>=3):
                if pattern[-1] == word[-1]:
                    return True
            else: return True
    return True