# that accepts as input, a date and time in the form yyyy-mm-dd
# hh:mm, and outputs the same information in long form:

day = input('Enter the date and time (yyyy-mm-dd hh:mm):\n')
cut = 0
year = ''
for i in range (len(day)-1):

    if day[i] == '-':
        cut = cut + 1
        if cut == 1:
         year = day[:i]
         end1 = i+1
        elif cut == 2:
           month = day[end1:i]
           end2 = i+1
    elif day[i] == ' ':
        musi = day[end2:i]
        end3 = i+1
    elif day[i] == ':':
       hour = day[end3:i]
       hour = int(hour)
       if hour > 12:
          hour = hour - 12
          hour1 = str(hour) + day[i:] + ' pm' 
       elif hour == 12:
          hour1 = '12' + day[i:] + ' pm' 
       elif hour == 0:
          hour1 = '12' + day[i:] + ' am'
       else:
          hour1 = str(hour) + day[i:] + ' am'

month = int(month)
if month == 1:
   month1 = 'January'
elif month ==2:
   month1 ='February'
elif month ==3:
   month1 ='March'
elif month ==4:
   month1 ='April'
elif month ==5:
   month1 ='May'
elif month ==6:
   month1 ='June'
elif month ==7:
   month1 ='July'
elif month ==8:
   month1 ='August'
elif month ==9:
   month1 ='September'
elif month ==10:
   month1 ='October'
elif month ==11:
   month1 ='November'
elif month ==12:
   month1 ='December'

if musi[0] != '1'and musi[1] == '1':
   musi1 = str(int(musi)) + 'st'
elif musi[0] != '1'and musi[1] == '2':
    musi1 = str(int(musi)) + 'nd'
elif musi[0] != '1' and musi[1] == '3':
   musi1 = str(int(musi)) + 'rd'
elif musi[0] != '1'and musi[1] > '3':
   musi1 = str(int(musi)) + 'th'
elif musi[0] == '1':
   musi1 = str(int(musi)) + 'th'
print('{0} on the {1} of {2} {3}{4}'.format(hour1,musi1,month1,'\'', year[2:] ))