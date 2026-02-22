#device smartphone laptop
#d   brand model     info about device
#s   storage 
#l   os ram

class device:
    def __init__(self, brand, model):
        self.brand=brand
        self.model=model
    def info(self):
        print(f"device is {self.brand} and its {self.model}")

my_naushniki=device("airpods", "pro")
my_naushniki.info()


class laptop(device):
    def __init__(self, brand, model, os, ram):
        super().__init__(brand, model)
        self.os=os
        self.ram=ram
    def about(self):
        if (self>=16):
            print("enough storage")
        else:
            print("not enough")
        print(f"laptop on {self.os}")
    def all(self):
        print(f"{self.brand} is {self.model}, and it  has {self.ram}, on {self.os}")

lenovo=laptop("lenovo", "ideapad", "windows10", 8)
lenovo.all()