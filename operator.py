#Importing Elevator class to access its functions.
from elevator import Elevator

#Operator class to make use of the Elevator functions.
class Operator():
    
    #Initializing user inputs and number of floors on building.
    def __init__(self,inputs):
        self.inputs = inputs
        self.elevator = Elevator(12)

    # def operate(self):
    #     for pair in self.inputs:
    #         print("pait",pair)
    #         if pair[0] == 0:
    #             self.elevator.call_elevator(pair[1])
    #         elif pair[0] == 1:
    #             self.elevator.go_floor(pair[1])
    
    #Function to run the elevator.
    def operate(self):
        locations = []
        for pair in range(len(self.inputs)):

            if self.inputs[pair][0] == "up" or "down":
                self.elevator.call_elevator(self.inputs[pair][1])
                locations.append(self.inputs[pair][1])
            elif self.inputs[pair][0] == "go":
                self.elevator.go_floor(self.inputs[pair][1])
                locations.append(self.inputs[pair][1])
                
        print(locations)
    
    #Print floor log on which the car stopped.
    def work(self):
        print(self.elevator.floors_stopped())