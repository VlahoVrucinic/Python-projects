def tax_calculator():
    price = int(input('Please enter the price of the item: '))
    tax_rate = int(input('Please enter the tax rate: '))
    
    tax_rate = tax_rate / 100
    tax = price * tax_rate
    item = price + tax
    
    
    print(f'The tax on this price is: {tax}')
    print(f'Your item plus the tax is: {item}')