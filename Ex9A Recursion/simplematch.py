# A program containing a function that can be used to determine if a given pattern matches a given word.
# VIncent T Mukwevo MKWVIN004
# 24/04/2024

def match(pattern, word):
    if (len(pattern)> 0) and (len(word )> 0)  :
      if len(pattern) == len(word) :
        if (pattern[0] == word[0]) or (pattern[0] == '?'):
            pattern = pattern[1:]
            word = word[1:]
            return (True and (match(pattern,word)))
        else: return False
      return False
    return True