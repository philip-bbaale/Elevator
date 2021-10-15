from src.operator import Operator

#Creating an instance of an operator
Op = Operator(50)


def test_case_1():
    """
    This function tests that the Elevator returns the order of the expected floors it will stop at while operating.

    Variables
    ---------
    b: list
        A sequence of requests made to the elevator car.

    Functions
    ---------
    run()
        This function calls the Elevator functions on the elevator car.
    """
    b = [("up",3),("go",12),("up",7),("down",7)]
    assert Op.run(b) == [3, 12, 7, 7]

def test_case_2():
    assert Op.elevator.elevator_current_floor() == 7

    a = [("up",3),("go",12),("up",7),("down",7),("go",7),("down",11),("down",12)]
    assert Op.run(a) == [3, 12, 7, 7, 7, 11, 12]