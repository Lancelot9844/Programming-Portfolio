# Pizza Project
print('BPP Pizza Price Computer')
print('============================')


# Constant Values
price_of_pizza = 12.00  # every pizza costs 12 pounds
tuesday_discount = 0.50  # 50% discount to all pizza prices on tuesday. This discount doesn't apply to any delivery cost
delivery_cost = 2.50  # Delivery cost is 2.50 pounds unless there are 5 or more pizzas in the order,in which it is free
app_discount = 0.25  # 25% discount applies if the customer orders via BPP app.Addition to Tuesday discount.


# Asking for inputs
while True:
    try:
        no_of_pizzas = int(input('How many pizzas ordered? '))
        if no_of_pizzas < 0:
            print('Please enter a positive integer! ')
        else:
            break
    except ValueError:
        print('Please enter a number! ')

while True:
    delivery_required = input('Is delivery required (y/n) ? ').lower()
    if delivery_required not in ['y', 'n']:
        print('Only Enter in "y" or "n" ')
    else:
        break

while True:
    is_tuesday = input('Is it Tuesday (y/n) ? ').lower()
    if is_tuesday not in ['y', 'n']:
        print('Please answer in "y" or "n" ')
    else:
        break


while True:
    is_app_used = input('Did the customer use the BPP App ? (y/n) ').lower()
    if is_app_used not in ['y', 'n']:
        print('Please answer in "y" or "n" ')
    else:
        break


# Price of pizza
Total_price = no_of_pizzas * price_of_pizza


# Tuesday discount
if is_tuesday == 'Y':
    Total_price = Total_price - (Total_price * tuesday_discount)


# Delivery cost
if delivery_required == 'y':
    if no_of_pizzas > 4:
        Total_price = Total_price + 0.00
    else:
        Total_price = Total_price + 2.50


# App discount
if is_app_used == 'y':
    Total_price = Total_price - (Total_price * app_discount)


# Total price
Total_price = format(Total_price, '.2f')
print(f'Total Price : ￡{Total_price}')
