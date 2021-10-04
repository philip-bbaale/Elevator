def look_and_scan(inputs):

    direction = bool
    car_cuurent_floor = 0
    number_of_floors = 20
    up_scheduling = []
    down_scheduling = []


    if inputs[0][0] == "up":
        direction = True
    elif inputs[0][0] == "down":
        direction = False
    elif inputs[0][0] == "go":
        if inputs[0][1] > car_cuurent_floor:
            direction = True
        else:
            direction = False

    first_come_direction = direction
    
    while len(inputs) > 0:

        if direction == True:
            for i in inputs:
                if i[0] == "go" and i[1] > car_cuurent_floor:
                    up_scheduling.append(i[1])
                    inputs.remove(i)
                elif i[0] == "up" and i[1] > car_cuurent_floor:
                    up_scheduling.append(i[1])
                    inputs.remove(i)
            else:
                direction = False
                up_scheduling.sort()
                car_cuurent_floor = up_scheduling[-1]

        if direction == False:
            for i in inputs:
                if i[0] == "go" and i[1] <= car_cuurent_floor:
                    down_scheduling.append(i[1])
                    inputs.remove(i)
                elif i[0] == "down" and i[1] <= car_cuurent_floor:
                    down_scheduling.append(i[1])
                    inputs.remove(i)
            else:
                direction = True
                down_scheduling.sort(reverse=True)
                car_cuurent_floor = down_scheduling[-1]

    if first_come_direction == True:
        new_disk_scheduling = up_scheduling + down_scheduling
    else:
        new_disk_scheduling = down_scheduling + up_scheduling

    return new_disk_scheduling

print(look_and_scan([("down", 5), ("go", 0), ("down", 5), ("up", 11), ("go", 0)]))