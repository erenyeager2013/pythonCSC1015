# A program that accepts user input and outputs the preceding numbers in 6 rows and 7 columns
# MKWVIN004 Vincent T Mukwevo
# 09/03/2024
number = eval(input('Enter a number between -6 and 2:\n'))
index = 0
if number >=-6 and number <= 2:
    sum = number
    column= 0
    while column < 6:
         column = column+ 1
         while index < 7:
           sum = number + (index)
           index = index + 1
           print('%2.0f'%sum, end = ' ')
         print('')
         sum = sum +1
         number = sum
         index = 0
else:
    print('Invalid input! The value of \'n\' should be between -6 and 2.')    