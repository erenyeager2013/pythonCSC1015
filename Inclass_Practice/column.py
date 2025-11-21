# program that prints list of numbers
# MKWVIN004 Mukwevo Vincent T
# 03/08/2024

number = eval(input('Enter a number between -6 and 2:\n'))
if number >=-6 and number <= 2:
    n = 0
    ass = 0
    print(number)
    while (ass + 7) < (number+ 41) :
     n= n+1
     ass = (n*7) + number
     print ('%2.0f'%ass)
else:
   print('Invalid input! The value of \'n\' should be between -6 and 2.')     