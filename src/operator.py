from elevator import Elevator

class Operator():
    """
    Contains algorithm to run the functions of the Elevator on the car
    """

    def __init__(self,floors):
        self.elevator = Elevator(floors)

    def run(self, inputs):
        """Algorithm that operates the elevator car"""

        self.inputs = inputs
        locations = []

        for pair in range(len(self.inputs)):

            if self.inputs[pair][0] in range(len(self.inputs)) == "up" or "down":

                if self.inputs[pair][0] == "up":
                    for pair2 in range(pair+1, len(self.inputs)):

                        if self.inputs[pair2][0] == "up":
                            self.elevator.call_elevator(self.inputs[pair2][1])
                            locations.append(self.inputs[pair2][1])
                            del self.inputs[pair2]

                if self.inputs[pair][0] == "down":
                    for pair2 in range(pair+1, len(self.inputs)):

                        if self.inputs[pair2][0] == "down":
                            self.elevator.call_elevator(self.inputs[pair2][1])
                            locations.append(self.inputs[pair2][1])
                            del self.inputs[pair2]

                self.elevator.call_elevator(self.inputs[pair][1])
                locations.append(self.inputs[pair][1])
                del self.inputs[pair]

            elif self.inputs[pair][0] == "go":
                self.elevator.go_floor(self.inputs[pair][1])
                locations.append(self.inputs[pair][1])
                del self.inputs[pair]
                
        return(locations)