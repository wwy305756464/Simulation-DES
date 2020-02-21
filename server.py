import heapq
class server:

  def __init__(self, TrafficLight,global_list):
      TrafficLight.setup()
      self.TrafficLight = TrafficLight
      self.global_list = global_list
      return

  def run(self):
      for i in range(len(self.global_list)):
          for j in range(len(self.global_list[i])):
              arrival_time = self.global_list[i][j].arrival_time
              lane = self.global_list[i][j].lane
              self.update_wait_time(arrival_time,lane,i,j)
      return self.global_list

  def update_wait_time(self, arrival_time,lane,i,j):
      cycle_time = self.TrafficLight.westLight.redTime
      if(lane <= 3):
          curlight = self.TrafficLight.northLight
          mod_time = arrival_time % cycle_time
          if(mod_time > self.TrafficLight.northLight.yellowTime):
              self.global_list[i][j].waiteTime = cycle_time - mod_time

      elif(lane == 4):
          curlight = self.TrafficLight.eastLight
          mod_time = arrival_time % cycle_time
          if (mod_time > self.TrafficLight.eastLight.yellowTime):
              self.global_list[i][j].waiteTime = cycle_time - mod_time
      else:
          curlight = self.TrafficLight.westLight
          mod_time = arrival_time % cycle_time
          if (mod_time > self.TrafficLight.westLight.yellowTime):
              self.global_list[i][j].waiteTime = cycle_time - mod_time
