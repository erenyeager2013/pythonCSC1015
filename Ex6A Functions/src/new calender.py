# new calender
def day_of_week(day, month, year):
    if month < 3:
        month += 12
        year -= 1
    k = year % 100
    j = year // 100
    h = (day + 13 * (month + 1) // 5 + k + k // 4 + j // 4 + 5 * j) % 7
    return (h + 5) % 7 + 1
def is_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
def month_num(month_name):
    # Your code here
    months = ('','january','february','march','april','may','june','july','august','september','october','november','december')
    month_name = month_name.lower()
    for i in range( 1,len(months)):
       if months[i] == month_name:
         month_num = i 
    return month_num

def num_days_in(month_num, year):
    if month_num == 2:
        return 29 if is_leap(year) else 28
    elif month_num in [4, 6, 9, 11]:
        return 30
    else:
        return 31
    
def num_weeks(num_days, week_day):
    if num_days % 7 != 0 and week_day > 4:
        return 6
    elif week_day <= 4 and num_days % 7 != 0:
        return 5
    else:
        return 4

def week(week_num, start_day, days_in_month):
    data = 0
    struc = ''
    c = 0
    for pr in range(1, start_day):
        struc += '  '
        c += 1
    for d in range(1, 9 - c):
        struc += f'{d:2d} '
        data = d
    if week_num == 1:
        return struc
    else:
        struc = ''
        if week_num == 2:
            data += 1
        else:
            data = ((week_num - 2) * 7) + data + 1
        for d in range(data, data + 7):
            if d < (days_in_month + 1):
                struc += f'{d:2d} '
    return struc
def main():
    # Your code here
    month_name = input('Enter month:\n')
    year = eval(input('Enter year:\n'))
    year0 = is_leap(year)
    month_nu = month_num(month_name)
    day_in_m = num_days_in(month_nu,year0)
    week_day = day_of_week(1,month_nu,year)
    week_num = num_weeks(day_in_m,week_day)
    print('Mo','Tu','We','Th','Fr','Sa','Su')
    for i in range(1,week_num+1):
        res = week(i,week_day,day_in_m)
        print(res)
    
if __name__=='__main__':
    main()