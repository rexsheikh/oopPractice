from Product import Product


class ShoppingCart:
    def __init__(self):
        self.products = []
        self.total = 0

    def current_total(self,products):
        for i in range(0,len(products)):
            self.total += products[i].price
        return self.total
    
    def add_to_cart(self,product):
        self.products.append(product)


    



