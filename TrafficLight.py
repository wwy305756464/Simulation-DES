class TrafficLight:
  def __init__(self, greenTime,yellowTime,redTime):
    self.greenTime = greenTime;
    self.yellowTime = yellowTime;
    self.redTime = redTime;
    self.cycleTime =greenTime + yellowTime + redTime
    self.northLight = None;
    self.eastLight = None;
    self.westLight = None;
    return

  def setup(self):
      self.northLight = TrafficLight(self.greenTime,self.yellowTime, self.redTime);
      self.eastLight = TrafficLight(self.greenTime + self.cycleTime, self.yellowTime+ self.cycleTime, self.redTime+ self.cycleTime);
      self.westLight = TrafficLight(self.greenTime+ self.cycleTime*2, self.yellowTime+ self.cycleTime*2, self.redTime+ self.cycleTime*2);

