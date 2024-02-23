import time


class Myqueue:
    def __init__(self):
        self.orders = []
    def placeorders(self,po):
        time.sleep(0.2)
        self.orders.append(po)
    def serveorder(self):
        for i in self.orders:
            time.sleep(2)
            print(self.orders.pop(0))
obj = Myqueue()
obj.placeorders(po='pizza')
obj.placeorders(po='burger')
obj.placeorders(po='juice')
obj.serveorder()



