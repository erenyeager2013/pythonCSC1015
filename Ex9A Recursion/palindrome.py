# A program that uses a recursive function to calculate whether or not a string is a palindrome or not
# Vincent T Mukwevo
# 24/04/2024

# this function recursively calss itself, slicing the string until only the middle character is left to compare
def palindrome(sente):
    if len(sente)> 1:
      if (sente[0] == sente[-1]) and palindrome(sente[1:-1]):
        return True
      else:
        return False
    else: return True

# obtaining the user input
sente = str(input('Enter a string: \n'))
answer = (palindrome(sente))
if answer == True:print('Palindrome!')
else: print('Not a palindrome!')