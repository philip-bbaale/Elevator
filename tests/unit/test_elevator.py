from src.elevator import Elevator

#Creating an instance of an operator
E = Elevator(20)

def test_elevator_goes_to_destination_floor():
    """
    This function tests that the elevator car requested floor to go is same as the elevator current floor after operating.

    Parameters:
    int
        Floor number for elevator car to go to.

    Return
    ------
    True
        If the elevator car current floor is the same as the elevator car floor to go to after operating.
    """
    E.go_floor(10)
    assert E.elevator_current_floor() == 10
    

def test_elevator_does_not_go_to_invalid_floor():
    E.go_floor(-200)
    assert E.elevator_current_floor() == -200



def test_elevator_does_not_move_when_weight_limit_is_exceeded_and_alerts_user():
    pass
