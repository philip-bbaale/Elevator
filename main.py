#Importin Elevator class to access its functions.
from elevator import Elevator

#Operator class to make use of the Elevator functions.
class Operator():

    #Initializing user inputs and number of floors on building.
    def __init__(self,inputs):
        self.inputs = inputs
        self.elevator = Elevator(12)

    #Function to run the elevator
    def operate(self):
        locations = []
        
        for pair in range(len(self.inputs)):
            
            #Run if call operator is going up
            if self.inputs[pair][0] == "up":

                #Run if Call operator is on a higher floor than the car's current floor.
                if self.inputs[pair][1] > self.elevator.car_current_floor:
                    self.elevator.car_call_up(self.inputs[pair][1])
                    locations.append(self.inputs[pair][1])

                #Run if the call operator is a lower floor than the car's current floor.
                elif self.inputs[pair][1] <= self.elevator.car_current_floor:
                    self.elevator.car_call_down(self.inputs[pair][1])
                    locations.append(self.inputs[pair][1])

            #Run if call operator is going down
            elif self.inputs[pair][0] == "down":

                #Run if call operator is on a higher floor than the car's current floor.
                if self.inputs[pair][1] > self.elevator.car_current_floor:
                    self.elevator.car_call_up(self.inputs[pair][1])
                    locations.append(self.inputs[pair][1])

                #Run if call operator is on a lower or on the same floor as the car.
                elif self.inputs[pair][1] <= self.elevator.car_current_floor:
                    self.elevator.car_call_down(self.inputs[pair][1])
                    locations.append(self.inputs[pair][1])

            #Run if call operator is inside the car and going to a floor
            elif self.inputs[pair][0] == "go":
                
                #Run if call operator is going to a higher floor
                if self.inputs[pair][1] > self.elevator.car_current_floor:
                    self.elevator.car_go_up(self.inputs[pair][1])
                    locations.append(self.inputs[pair][1])
                    
                #Run if call operator is on a lower on same floor as car
                elif self.inputs[pair][1] <= self.elevator.car_current_floor:
                    self.elevator.car_go_down(self.inputs[pair][1])
                    locations.append(self.inputs[pair][1])

    def sort_requests(self):
        move_up = []
        move_down = []
        go_to = []
        first_come = self.inputs[0]

        for turple in self.inputs:
            if turple[0] == "up":
                move_up.append(turple)
            elif turple[0] == "down":
                move_down.append(turple)
            elif turple[0] == "go":
                go_to.append(turple)

        # move_up.sort(key=lambda x:x[1])
        # ups_and_go_tos.sort(key=lambda x: x[1])

        move_down.sort(key=lambda x:x[1], reverse=True)
        go_to.sort(key=lambda x:x[1])
        ups_and_go_tos = move_up + go_to
        final = ups_and_go_tos + move_down
        
        # print("Ups: ",move_up)
        # print("Downs: ",move_down)
        # print("Got to: ",go_to)
        # print("First Come: ",first_come)

        # print(locations)

        final_floors = [first_come]

        if first_come[0] == "up":
            if first_come[1] > self.elevator.car_current_floor:
                for item in move_up:
                    if item[1] > first_come:
                        final_floors.append(item)
            else:
                if first_come < self.elevator.car_current_floor:
                    for item in move_down:
                        if item[1] < first_come:
                            final_floors.append(item)
        elif first_come[0] == "down":
            if first_come[1] > self.elevator.car_current_floo:
                pass


    def work(self):
        print(self.elevator.floors_stopped())

Op = Operator([ ("up",3),("go",12),   ("up",7),("down",7),("go",7),("down",11),("down",12),("go",1)])
# Op.operate()
Op.sort_requests()
