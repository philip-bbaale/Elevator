class Elevator():
  """
  Contains functions of the car.

  Parameters
  ----------
  num_floors: int
  The number of floors the elevator can access.

  elevator_current_floor: int, optional
  The car's current floor which is "ground floor", "0" by default.
  """
  def __init__(self, num_floors):
    self.total_floors = num_floors
    self.elevatator_current_floor = 0
  
  def elevator_current_floor(self):
    """
    Returns the car's current floor
    
    Returns
    -------
    int: the current floor the elevator car is at.
    """
    return self.elevatator_current_floor
  
  def is_at(self):
    """This function prints the elevator car's current floor"""
    print("Currently on {}'nd floor".format(self.elevatator_current_floor))

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
    self.elevatator_current_floor = self.elevatator_current_floor + 1

  def move_down(self):
    """
    This function moves the elevator car down by decrementing the elevator car's current floor by 1.

    Returns
    -------
    int: elevator car current floor - 1
    """
    self.elevatator_current_floor = self.elevatator_current_floor -1
  
  def call_elevator(self, user_call_floor):
    """Call car to floor"""
    self.user_call_floor = user_call_floor

    if self.user_call_floor > self.elevatator_current_floor:
      while self.elevatator_current_floor != self.user_call_floor:
        self.move_up()
      else:
        self.stop()

    if self.user_call_floor <= self.elevatator_current_floor:
      while self.elevatator_current_floor != self.user_call_floor:
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

    if self.user_go_floor > self.elevatator_current_floor:
      while self.elevatator_current_floor != self.user_go_floor:
        self.move_up()
      else:
        self.stop()

    if self.user_go_floor <= self.elevatator_current_floor:
      while self.elevatator_current_floor != self.user_go_floor:
        self.move_down()
      else:
        self.stop()
