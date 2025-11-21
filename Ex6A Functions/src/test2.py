week_num = 1
start_day = 1
days_in_month = 30 
data = 0
struc = ''
c = 0
for pr in range (0,start_day):
        if pr != start_day:
            struc =struc + '#'
            c = c + 1
for d in range (1,(8-c)):
    struc = struc + str(d)
    data = d
if week_num == 1:
  print(struc)
else:
     data = data*week_num
     struc = ''
     for d in range (data,data+7):
          if d < (days_in_month +1):
               struc = struc + str(d)
     print(struc)