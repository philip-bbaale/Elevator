from operator import Operator

#Cases of the requests to the elevator operator
a = [("up",3),("go",12),("up",7),("down",7),("go",7),("down",11),("down",12)]

b = [("up",3),("go",12),("up",7),("down",7)]

#Creating an instance of an operator
Op = Operator(12)

#calling the run function on the operator 
Op.run(b)
Op.run(a)
