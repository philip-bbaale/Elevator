from src.elevator import Elevator

class Operator():
    """
    This class contains algorithm to run the functions of the Elevator on the elevator car.

    Parameters
    ----------
    floors: int
        The number of floors the elevator can access.
    """
    def __init__(self,floors):
        self.elevator = Elevator(floors)
    
    def run(self, inputs):
        self.inputs = inputs
        """Algorithm that operates the elevator car"""
        locations = []
        for pair in range(len(self.inputs)):

            if self.inputs[pair][0] == "up" or "down":
                self.elevator.call_elevator(self.inputs[pair][1])
                locations.append(self.inputs[pair][1])
            elif self.inputs[pair][0] == "go":
                self.elevator.go_floor(self.inputs[pair][1])
                locations.append(self.inputs[pair][1])
                
        return locations