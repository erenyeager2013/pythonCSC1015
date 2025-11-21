# test3
month_name = input('enter month\n')
month_name = month_name.lower()
months = ('january','february','march','april','may','june','july','august','september','october','november','december')
for i in range( len(months)-1):
    if months[i] == month_name:
        month_num = i
print(month_num)