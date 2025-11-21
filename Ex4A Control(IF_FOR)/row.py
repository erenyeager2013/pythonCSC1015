# a program to print numbers 
# MKWVIN004 Vincent T Mukwevo
# 08/03/2024

value = eval(input('Enter a number between -6 and 93:\n'))
if value >= -6 and value <=93 :
    i = 0
    for i in range(0 , 7) :
        asse = value + i
        print ('%2.0f' %asse,end =' ')
else:
    print('Invalid input! The value of \'n\' should be between -6 and 93.')

        