class Elevator():
  """
  This Class contains functions of the elevator car.

  Parameters
  ----------
  num_floors: int
    The number of floors the elevator can access.

  elevator_current_floor: int, optional
    The car's current floor which is "ground floor", "0" by default.
  """
  def __init__(self, num_floors):
    self.total_floors = num_floors
    self.elevator_current_floor = 0
  
  def elevator_current_floor(self):
    """
    Returns the car's current floor
    
    Returns
    -------
    int: the current floor the elevator car is at.
    """
    return self.elevator_current_floor
  
  def is_at(self):
    """This function prints the elevator car's current floor"""
    print("Currently on {}'nd floor".format(self.elevator_current_floor))

  def stop(self):
    """This function prints "Opening Doors" and "Closing doors" to signal the elevator car stoping at a floor."""
    print("Opening Doors \n Closing Doors")
  
  def move_up(self):
    """
    This function moves the elevator car up by incrementing the elevator car's current floor by 1.

    Returns
    -------
    int: elevator car current floor + 1
    """
    self.elevator_current_floor = self.elevator_current_floor + 1

  def move_down(self):
    """
    This function moves the elevator car down by decrementing the elevator car's current floor by 1.

    Returns
    -------
    int: elevator car current floor - 1
    """
    self.elevator_current_floor = self.elevator_current_floor -1
  
  def call_elevator(self, user_call_floor):
    """
    This function calls the elevator car to a requested floor.

    Parameters
    ----------
    user_call_floor: int
      The floor number from which the user calls the elevator car.

    Returns
    -------
    This function checks if the user_call_floor is higher or lower than the elevator car's current floor and calls the move_up or move_down function respectively until the user_call_floor and the elevator_current_floor are the same.
    """
    self.user_call_floor = user_call_floor

    if self.user_call_floor > self.elevator_current_floor:
      while self.elevator_current_floor != self.user_call_floor:
        self.move_up()
      else:
        self.stop()

    if self.user_call_floor <= self.elevator_current_floor:
      while self.elevator_current_floor != self.user_call_floor:
        self.move_down()
      else:
        self.stop()

  def go_floor(self, user_go_floor):
    """
      Takes car to specified floor
      user_go_floor: int
      description: the user's destination floor
    """
    self.user_go_floor = user_go_floor

    if self.user_go_floor > self.elevator_current_floor:
      while self.elevator_current_floor != self.user_go_floor:
        self.move_up()
      else:
        self.stop()

    if self.user_go_floor <= self.elevator_current_floor:
      while self.elevator_current_floor != self.user_go_floor:
        self.move_down()
      else:
        self.stop()
