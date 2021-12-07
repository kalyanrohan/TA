class Shopping:

    def __init__(self,name,amount):
        self.name = name
        self.amount = amount
        self.price=0
        self.total=0
    
    def __PriceList(self):
        if self.name.lower()=="dry cured iberian ham":
            self.price=177.8
        elif self.name.lower()=="wagyu steaks":
            self.price=450
        elif self.name.lower()=="moose cheese":
            self.price=487.2
        else:
            self.price=0

    def total_price(self):
        self.__PriceList()
        self.total=self.price*self.amount
        return self.total

    def __str__(self):
        self.total_price()
        return f"Name: {self.name}\n Amount(pounds): {self.amount}\n Price: {self.price}\n Total: {self.total}"

    def get_price(self):
        self.__PriceList()
        return self.price