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
    """Returns the car's current floor"""
    return self.elevatator_current_floor
  
  def is_at(self):
    """Prints the car's current floor"""
    print("Currently on {}'nd floor".format(self.elevatator_current_floor))
  
  def move_up(self):
    """Make car to move up"""
    self.is_at()
    self.elevatator_current_floor = self.elevatator_current_floor + 1
    print("Moving up {}'nd floor".format(self.elevatator_current_floor))

  def move_down(self):
    """Make car to move down"""
    self.is_at()
    self.elevatator_current_floor = self.elevatator_current_floor -1
    print("Moving down {}'nd floor".format(self.elevatator_current_floor))

  def stop(self):
    """Make car to stop, open and close doors"""
    print("Opening Doors \n Closing Doors")
  
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
    """Takes car to specified floor"""
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
