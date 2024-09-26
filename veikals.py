from itertools import product


class Product:
    def __init__(self, name, price, quantity):
        self.name=name
        self.price=price
        self.quantity=quantity

    def get_total_price(self):
        total=self.price*self.quantity
        return(total)

    #def izv(self):
        #return ("{} maksā {} " ).format(self.name, self.price)

class ShoppingCart():
    def __init__(self, product):
       
        self.product=product



    def add_product_to_cart(self,product):
        return("Pievieno produktu",product.name)


    

    def remove_product_from_cart(self,product):
        return("Noņem produktu", product.name)

    def get_total_price(self, product):
        return("Kopējā summa ir", product.get_total_price)

maize=Product("Maize", 4 , 4)

print("Kopējā cena par maizi ir: ",maize.get_total_price())
siers=Product("Siers",2, 7)
print("Kopējā cena par sieru ir: ",siers.get_total_price())

maizes=ShoppingCart(maize)
print(maizes.add_product_to_cart(maize))
print(maizes.remove_product_from_cart(maize))
print(maizes.get_total_price(maize))

class Systemuser():
    def __init__(self, username, password, email):
        self.username=username
        self.password=password
        self.email=email

    def set_user_info(self,newusername,newpassword,newemail):
        self.username=newusername
        self.password=newpassword
        self.email=newemail
        print("Informācija ir nomainīta")
    def get_user_info(self):
        print("Informācija par lietotāju")
        print("Lietotājvārds: ",self.username)
        print("Parole: ", self.password)
        print("Email: ", self.email)


Karlis=Systemuser("Karlis", "qwerty", "Karlis@gmail.com")
Karlis.set_user_info("karlis", "12345", "karlis@gmail.com")
Karlis.get_user_info()



