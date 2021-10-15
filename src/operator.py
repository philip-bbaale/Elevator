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
        """
        This function contains the algorithm to call the Elevator functions on the elevator car

        Parameters
        ----------
        inputs: int
            A sequence of requests made to the elevator car.

        Returns
        -------
        locations: int
            A list of all the floors the elevator car stopped at while operating. 
        """
        self.inputs = inputs
        
        locations = []
        for pair in range(len(self.inputs)):

            if self.inputs[pair][0] == "up" or "down":
                self.elevator.call_elevator(self.inputs[pair][1])
                locations.append(self.inputs[pair][1])
            elif self.inputs[pair][0] == "go":
                self.elevator.go_floor(self.inputs[pair][1])
                locations.append(self.inputs[pair][1])
                
        return locations