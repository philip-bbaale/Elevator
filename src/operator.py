from elevator import Elevator
from schedule import schedule

class Operator():
    """
    Contains algorithm to run the functions of the Elevator on the car
    """

    def __init__(self,floors):
        self.elevator = Elevator(floors)

    def run(self, inputs):
        """Algorithm that operates the elevator car"""

        self.inputs = inputs
        self.schedule = schedule(self.inputs)
        locations = []

        for pair in self.schedule:

            if pair[0] == "up" or "down":
                self.elevator.call_elevator(pair[1])
                locations.append(pair[1])
            elif pair[0] == "go":
                self.elevator.go_floor(pair[1])
                locations.append(pair[1])

        return locations
        
            
            
                
