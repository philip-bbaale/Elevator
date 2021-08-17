from elevator import Elevator

class Operator():

    def __init__(self,inputs):
        self.inputs = inputs
        self.elevator = Elevator(12)
        self.car_current_floor = self.elevator.car_current_floor

    def operate(self):
        locations = []
        for pair in range(len(self.inputs)):

            # if self.inputs[pair][0] == "up" or "down":
            #     self.elevator.call_elevator(self.inputs[pair][1])
            #     locations.append(self.inputs[pair][1])
            # elif self.inputs[pair][0] == "go":
            #     self.elevator.go_floor(self.inputs[pair][1])
            #     locations.append(self.inputs[pair][1])
            pass
                
        print(locations)

    def work(self):
        print(self.elevator.floors_stopped())

Op = Operator([("up",3),("go",12),("up",7),("down",7),("go",7),("down",11),("down",12)])
Op.operate()
