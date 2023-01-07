#cashier_task14

print('=== Bongbong Supermarket Nota ===')

item_name = input('input item name : ')
price = float(input("input price item : "))
quantity = float (input('input quantity of item : '))
total_money = float(input('input total money you pay : '))
re_money = total_money - quantity * price

#nota
teks = f'''

===========================
Bongbong Supermarket Nota
===========================

- Item : {item_name}
- Price : {price}
- Quantity : {quantity}
- Total Money : IDR {total_money}
- Amount of change : IDR {re_money}

==========================

'''
#open and make new file
file = open('nota.txt', 'w')

#writing into file
file.write(teks)