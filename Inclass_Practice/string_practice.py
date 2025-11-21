# converting a characer to unicode
# MKWVIN004

char = input ('enter character\n')
print('unicode equivalent is: ', ord(char))
char2 = int(input('enter unicode:\n '))
print('character equivalent is: ', chr(char2))
strin = input('Enter your name: ')
strin2 =input('enter your surname: ')
print (' Hello '*2 + strin + strin2 )
print('your name has %s characters' %(len(strin)))
print('{1} {2}' .format(*strin))