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

class smartphone(device):
    def __init__(self, brand, model, storage):
        self.storage=storage
    def pamiat(self):
        if (self.storage>=128):
            print("enough storage")
        else:
            print("not enough")

phone=smartphone(256)
phone.pamiat()


class laptop(device):
    def __init__(self, brand, model, os, ram):
        self.os=os
        self.ram=ram
    def RAM(self):
        if (self>=16):
            print("enough storage")
        else:
            print("not enough")
        print(f"laptop on {self.os}")

lenovo=laptop("lenovo", "ideapad", "windows10", 8)

