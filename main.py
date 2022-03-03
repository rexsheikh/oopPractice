# from alarm_clock import AlarmClock

# rexs_alarm_clock = AlarmClock()

# print(rexs_alarm_clock.alarm_time)
# rexs_alarm_clock.change_time('1300')
# rexs_alarm_clock.alarm_toggle(False)
# print(rexs_alarm_clock.alarm_on)

# 1.	Print the customer’s name to the terminal
# 2.	Call the customer’s add product to shopping cart method three times and add the three products objects you created
# 3.	Call the customer’s view products method
# 4.	Call the customer’s shopping cart’s get cart total method. Capture the total the method returns in a variable and print to the terminal
# 5.	Call the customer’s shopping cart’s empty cart method
# 6.	Check if all products have been removed from the shopping cart


from ShoppingCart import ShoppingCart
from Customer import Customer
from Product import Product 


banana = Product('banana',1,'fruit')
salsa = Product('salsa',2,'sauce')
milk = Product('milk',3,'dairy')


rex = Customer('rex')
shopping_cart = rex.shopping_cart.products
rex.shopping_cart.add_to_cart(banana)
rex.shopping_cart.add_to_cart(salsa)
rex.shopping_cart.add_to_cart(milk)



rex.view_all(rex.shopping_cart.products)
total = rex.shopping_cart.current_total(rex.shopping_cart.products)
print(total)

rex.remove_all(rex.shopping_cart.products)
rex.view_all(rex.shopping_cart.products)



