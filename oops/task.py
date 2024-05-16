#
class Shop:
    def __init__(self,name,qty,price):
        assert qty>0,f"your {qty} should be greater than zero"
        self.name=name
        self.qty=qty
        self.price=price

    def Total_price(self):
        total=self.price*self.qty
        print(f"your product {self.name} and it's Total price Rs.{total}")

P1=Shop("copy",-5,20)
P1.Total_price()

p2=Shop("book",2,200)
p2.Total_price()