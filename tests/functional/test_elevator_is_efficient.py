from src.operator import Operator

#Creating an instance of an operator
Op = Operator(50)


def test_case_1():
    b = [("up",3),("go",12),("up",7),("down",7)]
    assert Op.run(b) == [3, 12, 7, 7]

def test_case_2():
    assert Op.elevator.elevatator_current_floor() == 7

    a = [("up",3),("go",12),("up",7),("down",7),("go",7),("down",11),("down",12)]
    assert Op.run(a) == [3, 12, 7, 7, 7, 11, 12]