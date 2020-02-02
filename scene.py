import numpy as np 
import math as math
import os

class Scene:
    dirpath = os.path.dirname(os.path.realpath(__file__))
    def __init__(self,n,t):
        self.N = n
        self.T = t
    def vehicle_generate(self):
        print('generating vehicles ... in the scene')
    def pedestrain_generate(self):
        print('generating pedestrains ... in the scene')

    def poisson_generate_timestamps(self):
        lamda = float(self.N)/float(self.T)/60.0/60.0 #per second
        Time = int(self.T*60.0*60.0) #total seond
        poisson = np.random.poisson(lamda,Time)
        time_stamps = []
        time_stamp = 0.0
        for p in poisson:
            if p != 0:
                event_time = np.random.uniform(0,1.0,p)# per second, unit minute interval
                for t_s in event_time:
                    time_stamp=time_stamp+t_s;
                    time_stamps.append(time_stamp)
            else:
                time_stamp = time_stamp+1.0
        np.sort(time_stamps)
        total_sim_event = len(time_stamps)
        sim_mean = np.mean(poisson)
        print('Based on input parameters [{} events , {} hr], expected rate is {:.3f} events/second, \nSampled {} events based on poisson process within time {} hr,sample mean is {:.3f} events/second\nNext start generating actors in the scene ...'\
            .format(self.N,self.T,lamda,total_sim_event,self.T,sim_mean))
        return time_stamps
    


        
        


