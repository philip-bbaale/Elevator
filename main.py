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

            if self.inputs[pair][0] == 0:
                self.elevator.call_elevator(self.inputs[pair][1])
                locations.append(self.inputs[pair][1])
            elif self.inputs[pair][0] == 1:
                self.elevator.go_floor(self.inputs[pair][1])
                locations.append(self.inputs[pair][1])
                
        print(locations)

    def work(self):
        print(self.elevator.floors_stopped())

Op = Operator([ (0,0), (0,11), (1,4), (1,11)])
Op.operate()
