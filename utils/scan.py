def scan(inputs):
    """
    Returns ordered list sequence for elevator to operate.

    Parameters
    __________
        inputs: List
            A list of Tuples with request direction in the 0 index and floor number in the 1 index.
    Returns
    _______
        An efficient list of ordered floors the elevator car should follow to operate.
    """

    car_current_floor = 0
    up_schedule = []
    down_schedule = []

    # Genarate first come first served direction of the car
    first_request = inputs[0][0]
    first_request_dest_floor = inputs[0][1]

    #TODO:This will not work if car_current_floor starts at top most floor. Fix it.
    #Update the function to work regardless of car_current_floor's initial value.
    #Right now it only works if car_current_floor = 0 at the start
    car_going_up = first_request == "up" or (first_request == "go" and first_request_dest_floor > car_current_floor)

    def update_schedule():

        def _same_direction(user_current_floor):
            is_same_dir = user_current_floor > car_current_floor
            return is_same_dir == car_going_up

        anti_direction = "down" if car_going_up else "up"
        schedule = []

        for i in inputs:
            user_req = i[0]
            user_curr_floor = i[1]
            if user_req != anti_direction and _same_direction(user_curr_floor):
                schedule.append(i)
                inputs.remove(i)
        return schedule

    while inputs:
        current_schedule = up_schedule if car_going_up else down_schedule
        current_schedule += update_schedule()
        car_current_floor = current_schedule[-1][1]
        car_going_up = not car_going_up


    up_schedule.sort(key=lambda x:x[1])
    down_schedule.sort(key=lambda x:x[1], reverse=True)

    final_schedule = up_schedule + down_schedule
    return final_schedule if car_going_up else final_schedule.reverse()

print(scan([("up",3),("go",12),("up",7),("down",7),("go",7),("down",11),("down",12)]))
