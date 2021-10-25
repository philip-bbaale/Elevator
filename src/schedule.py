def schedule(inputs, elevator_current_floor):

    direction = bool
    up_scheduling = []
    down_scheduling = []
    car_current_floor = elevator_current_floor

    if inputs[0][0] == "up":
        direction = True
    elif inputs[0][0] == "down":
        direction = False
    elif inputs[0][0] == "go":
        if inputs[0][1] > car_current_floor:
            direction = True
        else:
            direction = False

    first_come_direction = direction

    while len(inputs) >= 0:
    #Serve all requests in the up direction if they are greater than the elevator car current floor.
        if direction == True:
            for i in inputs:
                print("True", i)
                if i[0] in ["go", "up"] and i[1] >= car_current_floor:
                    up_scheduling.append(i)
                    inputs.remove(i)

            print("Lorem111")
            direction = False
            up_scheduling.sort(key=lambda x:x[1])
            print(up_scheduling[-1][1])
            car_current_floor = up_scheduling[-1][1]
            
        #Serve all request in the down direction if they are less than the elevator car current floor.
        else:
            for i in inputs:
                print("False", i)
                if i[0] == ["go", "down"] and i[1] <= car_current_floor:
                    down_scheduling.append(i)
                    inputs.remove(i)

            print("Lorem222")
            direction = True
            down_scheduling.sort(key=lambda x:x[1], reverse=True)
            print(down_scheduling[-1][1])
            car_current_floor = down_scheduling[-1][1]

    #Arrange the sequence of floors according to First come First served
    if first_come_direction == True:
        new_disk_scheduling = up_scheduling + down_scheduling
    else:
        new_disk_scheduling = down_scheduling + up_scheduling

    return new_disk_scheduling