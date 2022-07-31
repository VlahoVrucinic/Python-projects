#dates
d1 = datetime.today()
d2_str = str(input('Enter the date of your birthday yyyy/mm/dd: '))
d2 = datetime.strptime(d2_str, '%Y/%m/%d')

# age
age_days = (abs(delta.days))
age_years = age_days // 365
print(f'You are {age_years} years old')