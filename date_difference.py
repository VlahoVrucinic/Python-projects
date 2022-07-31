# Entering the date
str_date1 = str(input('Enter the first date yyyy/mm/dd: '))
str_date2 = str(input('Enter the second date yyyy/mm/dd: '))

# Date variables
date1 = datetime.strptime(str_date1, '%Y/%m/%d') 
date2 = datetime.strptime(str_date2, '%Y/%m/%d')

# Subtraction
delta = date2 - date1
print(f'The difference is {delta.days} days')