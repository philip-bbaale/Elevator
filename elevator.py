class Elevator():
  def __init__(self, num_floors):
    self.total_floors = num_floors
    self.car_current_floor = 5
    self.max_floor = 12
    self.min_floor = 0

  def get_car_current_floor(self):
    return self.car_current_floor

  def is_at(self):
    print("Currently on {}'nd floor".format(self.car_current_floor))

  def move_up(self):
    self.is_at()
    self.car_current_floor = self.car_current_floor + 1
    print("Moving up {}'nd floor".format(self.car_current_floor))

  def move_down(self):
    self.is_at()
    self.car_current_floor = self.car_current_floor -1
    print("Moving down {}'nd floor".format(self.car_current_floor))

  def stop(self):
    print("Opening Doors \n Closing Doors",self.car_current_floor)

  def car_call_up(self, user_call_floor):
    self.user_call_floor = user_call_floor
    while self.car_current_floor != self.user_call_floor and self.car_current_floor < self.max_floor:
      self.move_up()
    else:
      self.stop()

  def car_call_down(self, user_call_floor):
    self.user_call_floor = user_call_floor
    while self.car_current_floor != self.user_call_floor and self.car_current_floor > self.min_floor:
      self.move_down()
    else:
      self.stop()
    
  def car_go_up(self, user_go_floor):
    self.user_go_floor = user_go_floor
    while self.car_current_floor != self.user_go_floor:
      self.move_up()
    else:
      self.stop()

  def car_go_down(self, user_go_floor):
    self.user_go_floor = user_go_floor
    while self.car_current_floor != self.user_go_floor:
      self.move_down()
    else:
      self.stop()
