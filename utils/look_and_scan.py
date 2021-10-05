def look_and_scan(inputs):
    """
    Returns ordered list sequence for elevator to operate

    Parameters
    __________
        inputs: List
            A list of Tuples with request direction in the 0 index and floor number in the 1 index.
    Returns
    _______
        An efficient list of ordered floors the elevator car should follow to operate.    
    """

    direction = bool
    car_current_floor = 0
    number_of_floors = 20
    up_scheduling = []
    down_scheduling = []

    # Genarate first come first served direction of the car
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
    
    while len(inputs) > 0:

        #Serve all requests in the up direction if they are greater than the elevator car current floor.
        if direction == True:
            for i in inputs:
                if i[0] == "go" and i[1] > car_current_floor:
                    up_scheduling.append(i)
                    inputs.remove(i)
                elif i[0] == "up" and i[1] > car_current_floor:
                    up_scheduling.append(i)
                    inputs.remove(i)
            else:
                direction = False
                up_scheduling.sort()
                car_current_floor = up_scheduling[-1][1]
        #Serve all request in the down direction if they are less than the elevator car current floor.
        if direction == False:
            for i in inputs:
                if i[0] == "go" and i[1] <= car_current_floor:
                    down_scheduling.append(i)
                    inputs.remove(i)
                elif i[0] == "down" and i[1] <= car_current_floor:
                    down_scheduling.append(i)
                    inputs.remove(i)
            else:
                direction = True
                down_scheduling.sort(key=lambda x:x[1], reverse=True)
                car_current_floor = down_scheduling[-1][1]

    #Arrange the sequence of floors according to First come First served
    if first_come_direction == True:
        new_disk_scheduling = up_scheduling + down_scheduling
    else:
        new_disk_scheduling = down_scheduling + up_scheduling

    return new_disk_scheduling

print(look_and_scan([("down", 5), ("go", 0), ("down", 5), ("up", 11), ("go", 0)]))