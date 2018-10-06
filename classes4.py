class Flight: 

    counter = 1

    def __init__(self, origin, destination, duration): 

        #Keep track of id number
        self.id = Flight.counter
        Flight.counter +=1

        #Keep track of passengers 
        self.passengers = []

        #Details about flight
        self.origin = origin
        self.destination = destination
        self.duration = duration

    def print_info(self): #Pring details about flight 
        print(f"Flight origin: {self.origin}")
        print(f"Flight origin: {self.destination}")
        print(f"Flight origin: {self.duration}")

        print()
        print("Paasengers:")
        for passengers in self.passengers:
            print (f"{passengers.name}")
    
    def delay(self, amount):
        self.duration += amount
    
    def add_passenger(self, p):
        self.passengers.append(p)
        p.flight_id = self.id


class Passenger: 
    def __init__(self, name):
        self.name = name

def main():
    #Create flight
    f1 = Flight(origin="New York", destination="Paris", duration=540) #can be used witout paramntrs
    f1.delay(10)

    #Create passengers
    oksana = Passenger(name="Oksana")
    alex = Passenger(name="Bob")

    #Add passengers 
    f1.add_passenger(oksana)
    f1.add_passenger(alex)

    f1.print_info()
    print(f1.id)


if __name__ == "__main__": # menas to run this file if there was no import 
    main()