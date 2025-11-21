#  A program to reformat references
# Vincent T Mukwevo MKWVIN004
# 20/03/2024

ref = str(input('Enter the reference:\n'))
com = 0
# seperating Authors, title and the rest for data formatting
for comma in range (len(ref)-1):
    if ref[comma] == ',':
        com = com + 1
        if com == 1:
            name = ref[0:comma]
            end1 = comma +1
        elif com == 2:
            title = ref[end1:comma]
            end2 = comma +1
        else:
            rest = ref[end2:]
            continue
# formatting data:
#for the Author
name = name.capitalize()
# for the title
s = 0
title2 =''
for ed in range (len(title)- 1):
    if title[ed] == '(':
        en = ed +1
    if title[ed] == ')':
        vtm = ed + 2
while s < (vtm):
    if title[s] == ' ':
       title2 = title2 + ' ' + title[s+1].upper()
       s = s + 2
    else:
        if s == vtm:
            title2 = title2 + str(title[vtm]).upper()
            s = s + 1
        else:
          title2 = title2 + str(title[s]).lower()
          s = s + 1
title2 = title2 + str(title[(vtm+1):]).lower()
# printing output
print('Reformatted reference:\n{0},{1},{2}'.format(name,title2,rest))