from elevator import Elevator

class Operator():

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

    def operate(self):
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
                
        print(locations)

    def work(self):
        print(self.elevator.floors_stopped())

Op = Operator([("up",3),("go",12),("up",5),("down",7),("go",7),("down",11),("down",12)])
Op.operate()
