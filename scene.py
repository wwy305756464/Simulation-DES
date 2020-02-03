import numpy as np 
import math as math
import Vehicle
import os
import heapq

class Scene:
    dirpath = os.path.dirname(os.path.realpath(__file__))
    def __init__(self):
        self.n = 1
        self.q = []
    def vehicle_generate(time_stamp,car_type,car_direction,which_lane,ID):
        print('generating vehicles ... in the scene')
        numberOfCar = len(time_stamp)
        global_q_list = [];
        # create 6 empty list for each lane
        for i in range(6):
            global_q_list.append([])
        # N1 = [];
        # N2 = [];
        # N3 = [];
        # N4 = [];
        # E1 = [];
        # W1 = [];

        for i in range(numberOfCar):
            car_i = Vehicle.Vehicle(time_stamp[i],car_type[i],car_direction[i],which_lane[i],ID[i])
            global_q_list[int(which_lane[i])].append(car_i)
        # add each car to certain lane

        for i in range(6):# heapify each lane
            heapq.heapify(global_q_list[i])

        return global_q_list;


    def pedestrain_generate():
        print('generating pedestrains ... in the scene')
    
    
        

        
        


