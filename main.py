#Importing Operator class to access its functions.
from operator import Operator

#Creating an instance of an operator
Op = Operator([("up",3),("go",12),("up",7),("down",7),("go",7),("down",11),("down",12)])
Op.operate()
