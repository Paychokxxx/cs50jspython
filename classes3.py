class Flight: 

    def __init__(self, origin, destination, duration): 
        self.origin = origin
        self.destination = destination
        self.duration = duration

    def print_info(self): #Pring details about flight 
        print(f"Flight origin: {self.origin}")
        print(f"Flight origin: {self.destination}")
        print(f"Flight origin: {self.duration}")
    
    def delay(self, amount):
        self.duration += amount

def main():
    f1 = Flight(origin="New York", destination="Paris", duration=540) #can be used witout paramntrs
    f1.delay(10)
    f1.print_info()

    f2 = Flight(origin="Moscow", destination="Paris", duration=666)
    f2.print_info()


if __name__ == "__main__": # menas to run this file if there was no import 
    main()