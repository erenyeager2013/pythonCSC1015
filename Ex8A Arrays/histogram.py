# A program that takes in a list of marks (separated by spaces) and outputs a histogram representation of the marks according to the mark categories at UCT
# VIncent T Mukwevo MKWVIN004
# 16/04/2024

mylist = str(input('Enter a space-separated list of marks:\n'))
list = mylist.split(' ')
ones = 0 ; twosU = 0; twosL = 0; threes = 0; fs = 0
for i in range(len(list)):
    mark = int(list[i])
    if mark >= 75:    ones += 1
    elif mark >= 70 and mark < 75:   twosU += 1
    elif mark >=60 and mark < 70 :   twosL +=1
    elif mark >= 50 and mark < 60:   threes += 1
    elif mark < 50:   fs +=1
print('1 |{0}'.format('X'*ones))
print('2+|{0}'.format('X'*twosU))
print('2-|{0}'.format('X'*twosL))
print('3 |{0}'.format('X'*threes))
print('F |{0}'.format('X'*fs))