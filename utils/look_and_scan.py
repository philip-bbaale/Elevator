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
    up_scheduling = []
    down_scheduling = []

    # Genarate first come first served direction of the car

    first_request = inputs[0][0]
    if first_request == "up":
        direction = True
    elif first_request == "down":
        direction = False
    elif first_request == "go":
        direction = True if inputs[0][1] > car_current_floor else False

    def update_schedule():

        def _same_direction(user_current_floor):
            is_before = user_current_floor > car_current_floor
            return is_before == direction

        anti_direction = "down" if direction else "up"
        schedule = []

        for i in inputs:
            user_req = i[0]
            user_curr_floor = i[1]
            if user_req != anti_direction and _same_direction(user_curr_floor):
                schedule.append(i)
                inputs.remove(i)
        return schedule

    while inputs:
        if direction:
            up_scheduling += update_schedule()
            direction = not direction
            car_current_floor = up_scheduling[-1][1]
        else:
            down_scheduling +=update_schedule()
            direction = not direction
            car_current_floor = down_scheduling[-1][1]

    up_scheduling.sort(key=lambda x:x[1])
    down_scheduling.sort(key=lambda x:x[1], reverse=True)

    final_schedule = up_scheduling + down_scheduling
    return final_schedule if direction else final_schedule.reverse()

print(look_and_scan([("up",3),("go",12),("up",7),("down",7),("go",7),("down",11),("down",12)]))
