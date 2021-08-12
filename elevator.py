class Elevator():
  def __init__(self, num_floors):
    self.total_floors = num_floors
    self.elevatator_current_floor = 0

  def elevator_current_floor(self):
    return self.elevatator_current_floor

  def is_at(self):
    print("Currently on {}'nd floor".format(self.elevatator_current_floor))

  def move_up(self):
    self.is_at()
    self.elevatator_current_floor = self.elevatator_current_floor + 1
    print("Moving up {}'nd floor".format(self.elevatator_current_floor))

  def move_down(self):
    self.is_at()
    self.elevatator_current_floor = self.elevatator_current_floor -1
    print("Moving down {}'nd floor".format(self.elevatator_current_floor))

  def stop(self):
    print("Opening Doors \n Closing Doors")

  def call_elevator(self, user_call_floor):
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
