class TrafficLight:
  def __init__(self, greenTime,yellowTime,redTime):
    self.greenTime = greenTime
    self.yellowTime = yellowTime
    self.redTime = redTime
    self.cycleTime =greenTime + yellowTime + redTime
    self.northLight = None
    self.eastLight = None
    self.westLight = None
    return

  def setup(self):
      # end time for green yellow red
      self.northLight = TrafficLight(self.greenTime, self.yellowTime + self.greenTime, self.cycleTime)
      self.eastLight = TrafficLight(self.greenTime + self.cycleTime, self.greenTime + self.yellowTime+ self.cycleTime, self.cycleTime*2)
      self.westLight = TrafficLight(self.greenTime+ self.cycleTime*2, self.yellowTime +self.greenTime+ self.cycleTime*2, self.cycleTime*3)

