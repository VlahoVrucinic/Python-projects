def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    return x / y
    
print('Choose the operation you want to do :')
print('1. for addition')
print('2. for subtraction')
print('3. for multiplying')
print('4. for division')
    

while True:
    choice = input('Enter the number of the operation you want to do: ')
    
    if choice in ('1','2','3','4'):
        num1 = float(input('Enter the first number '))
        num2 = float(input('Enter the second number '))
    
    if choice == '1':
        print(num1,'+',num2,'=',add(num1,num2))
        
    if choice == '2':
        print(num1,'-',num2,'=',subtract(num1,num2))
    
    if choice == '3':
        print(num1,'*',num2,'=',multiply(num1,num2))
        
    if choice == '4':
        print(num1,'/',num2,'=',divide(num1,num2))
        
    print('Do you want to stop calculating? if yes enter no')
    keep_going = input('No? ')
    if keep_going == 'no':
        break