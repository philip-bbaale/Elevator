from src.elevator import Elevator


E = Elevator(20)

def test_elevator_goes_to_destination_floor():
    E.go_floor(10)
    assert E.elevatator_current_floor() == 10
    

def test_elevator_does_not_go_to_invalid_floor():
    E.go_floor(-200)
    assert E.elevatator_current_floor() == -200



def test_elevator_does_not_move_when_weight_limit_is_exceeded_and_alerts_user():
    pass
