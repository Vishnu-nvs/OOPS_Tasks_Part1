

# Create a class Product with attributes id, name, and price. Add method to calculate discounted price. 
# Create subclass ElectronicProduct with warranty attribute.



class Product:
    def __init__(self,id,name,price):
        self.id=id
        self.name=name
        self.price=price
    def discount_1(self):
        discount_item=(self.price * 5/100)
        item_price=self.price-discount_item
        print("Product Id :",self.id)
        print("porduct name is :",self.name)
        print("Orginal cost is :",self.price)
        print("after discount price is :",item_price)

class ElectronicProduct(Product):
    def __init__(self,id=None,name=None,price=None,warranty=None): 
        super().__init__(id,name,price)
        self.warranty=warranty
        if self.warranty is not None:
            self.discount()
        else:
            Product.discount_1(self)
    def discount(self):
        discount_item=(self.price * 5/100)
        item_price=self.price-discount_item
        print("Product Id :",self.id)
        print("porduct name is :",self.name)
        print("Orginal cost is :",self.price)
        print("after discount price is :",item_price)
        print("warranty is : ",self.warranty)
c=ElectronicProduct(101,"Smartphone",20000,"2 years")
# p=Product(102,"Laptop",50000)
# p.discount_1()


# Output:
# Product Id : 101
# porduct name is : Smartphone
# Orginal cost is : 20000
# after discount price is : 19000.0
# warranty is :  2 years