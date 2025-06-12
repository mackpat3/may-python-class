#spend $100 more and get 10% discount
#spend $200 get 20% discount
#if we buy $80 , we pay $80
#if we buy $150, we pay $135
#we pay 10% tax

discount=0
sales_tax=0.1

def tax_func(price):
    taxes = price * sales_tax
    return taxes

def discount_func(price, discount):
    discount_sum = price * (discount / 100)
    return discount_sum

price=float(input("Enter price: "))
tax=tax_func(price)

if price > 100 and price <= 200:
   discount = discount_func(price,10)
elif price > 200:
   discount = discount_func(price,20)

total_price = price + tax - discount
print(total_price)

