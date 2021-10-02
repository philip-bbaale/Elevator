from src.operator import Operator

a = [("up",3),("go",12),("up",7),("down",7),("go",7),("down",11),("down",12)]

b = [("up",3),("go",12),("up",7),("down",7)]

#Creating an instance of an operator
Op = Operator(12)


def test_first_inputs():
    assert Op.run(b) == [3, 12, 7, 7]

def test_second_inputs():
    assert Op.run(a) == [3, 12, 7, 7, 7, 11, 12]