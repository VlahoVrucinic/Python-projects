import openpyxl
from openpyxl import Workbook

# Setting up the workbook
workbook = Workbook()
workbook.save(filename = 'Exercise.xlsx')

wb = openpyxl.Workbook()
sheet = wb.active 

#NAMES
sheet['A1'] = 'NAME'
sheet['A2'] = 'Bill'
sheet['A3'] = 'Joseph'
sheet['A4'] = 'Phil'
sheet['A5'] = 'Steve'
sheet['A6'] = 'John'
sheet['A7'] = 'Joanne'
sheet['A8'] = 'Mary'
sheet['A9'] = 'Emma'
sheet['A10'] = 'Victoria'
sheet['A11'] = 'Olivia'
sheet['A12'] = 'Anna'
sheet['A13'] = 'William'
sheet['A14'] = 'Charles'
sheet['A15'] = 'Taylor'

sheet.column_dimensions['A'].width = 23



#SURNAMES
sheet['B1'] = 'SURNAME'
sheet['B2'] = 'Smith'
sheet['B3'] = 'Jones'
sheet['B4'] = 'Taylor'
sheet['B5'] = 'Williams'
sheet['B6'] = 'Brown'
sheet['B7'] = 'Johnson'
sheet['B8'] = 'Davies'
sheet['B9'] = 'Lewis'
sheet['B10'] = 'Clarke'
sheet['B11'] = 'Allen'
sheet['B12'] = 'Anderson'
sheet['B13'] = 'Miller'
sheet['B14'] = 'Scott'
sheet['B15'] = 'Walker'

sheet.column_dimensions['B'].width = 20



#AGE
sheet['C1'] = 'AGE'
sheet['C2'] = 22
sheet['C3'] = 25
sheet['C4'] = 35
sheet['C5'] = 39
sheet['C6'] = 18
sheet['C7'] = 40
sheet['C8'] = 42
sheet['C9'] = 33
sheet['C10'] = 21
sheet['C11'] = 44
sheet['C11'] = 48
sheet['C12'] = 49
sheet['C13'] = 52
sheet['C14'] = 18
sheet['C15'] = 26

#INCOME
sheet['D1'] = 'INCOME'
sheet['D2'] = 4600
sheet['D3'] = 6500
sheet['D4'] = 7000
sheet['D5'] = 5500
sheet['D6'] = 3500
sheet['D7'] = 9000
sheet['D8'] = 7600
sheet['D9'] = 10000
sheet['D10'] = 5300
sheet['D11'] = 8200
sheet['D12'] = 10500
sheet['D13'] = 12000
sheet['D14'] = 4200
sheet['D15'] = 5500

sheet.column_dimensions['D'].width = 22



# Sum of people

sheet['A17'] = 'The number of names is: '
sheet['A18'] = '=COUNTA(A2:A15)'

# Lowest and highest age
sheet['B17'] = 'The lowest age is: '
sheet['B18'] = 'The highest age is: '
sheet['C17'] = '=MIN(C2:C15)'
sheet['C18'] = '=MAX(C2:C15)'

# Average income

sheet['D17'] = 'The average income is: '
sheet['D18'] = '=AVERAGE(D2:D15)'

# Filter 
# ws stoji za worksheet tables

ws = wb.active

ws.auto_filter.ref = 'A1:D15'   
ws.auto_filter.add_filter_column(0,['AGE','INCOME'])
ws.auto_filter.add_sort_condition("C2:C7")


wb.save('Exercise.xlsx')