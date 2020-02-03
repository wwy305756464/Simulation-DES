import numpy as np
import math as math
import heapq

class Vehicle:
  def __init__(self, arrival_time,type,direction,lane,ID):
    self.ID = ID
    self.direction = direction
    self.lane = lane
    self.type = type
    self.arrival_time = arrival_time
  def __repr__(self):
    return "Vehicle ID : " + str(self.ID) + " " + "Arrival_Time: " + str(self.arrival_time) + ", Direction: " + str(self.direction)
  def __lt__(self, other):
    return self.arrival_time < other.arrival_time


