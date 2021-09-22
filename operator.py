#Importing Elevator class to access its functions.
from elevator import Elevator

class Operator():
    """
    Contains algorithm to run the functions of the Elevator on the car
    """
    def __init__(self,inputs):
        self.inputs = inputs
        self.elevator = Elevator(12)
    
    def operate(self):
        """Algorithm that operates the elevator car"""
        locations = []
        for pair in range(len(self.inputs)):

            if self.inputs[pair][0] == "up" or "down":
                self.elevator.call_elevator(self.inputs[pair][1])
                locations.append(self.inputs[pair][1])
            elif self.inputs[pair][0] == "go":
                self.elevator.go_floor(self.inputs[pair][1])
                locations.append(self.inputs[pair][1])
                
        print(locations)
    
    def work(self):
        """Print floor log on which the car stopped"""
        print(self.elevator.floors_stopped())