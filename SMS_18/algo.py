import time, random
import threading

class Stock:
    '''
    Class for Stock object.
    Variable description:
    name: Name of Stock
    p0: Initial Price of Stock
    pf: Final price of Stock
    total_time: The time duration for which the event runs
    price: Current Price of the Stock
    fraction: To divide the total_time into a number of time intervals
              update the stock price 
    '''


    def __init__(self, name, p0, pf, total_time, price = 0, fraction = 15, start_time = time.time()):
        self.name = name
        self.p0 = p0
        self.price = p0
        self.pf = pf
        self.total_time = total_time
        self.fraction = fraction
        self.start_time = start_time
        thread = threading.Thread(target=self.st_line_fx, args=())
        thread.start()

    def __str__(self):
        return self.name
   
    def st_line_fx(self):
        while True:
            slope = (self.pf - self.p0) / self.total_time
            present_time = time.time()
            self.price = self.p0 + (slope * (present_time - self.start_time) / 60)