from ShoppingCart import ShoppingCart

class Customer:
    def __init__(self,name):
        self.name = name
        self.shopping_cart = ShoppingCart()

    def view_all(self,products):
        for i in range(0,len(products)):
            print(products[i].name)

    def remove_all(self,products):
        self.shopping_cart.products = []
        print(self.shopping_cart.products)


