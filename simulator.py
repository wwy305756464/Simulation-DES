import os
import collections
import argparse
import multiprocessing
import json
import time
from random import randint

import numpy as np
import math as math

from scene import Scene

_author_  = 'Muyang Guo, Wei Zhao, Shushu Zhao, Wenyue Wang'

def parseArguments():
    '''

    simulation time:

    '''
    parser = argparse.ArgumentParser()
    parser.add_argument('simulation time', help = ':indicate simulation duration time, requested here', type=float, default = 100)
    args = parser.parse_args()
    return args

def main():
    with open('config.json') as json_config_file:
        data = json.load(json_config_file)
    print("Simulation process of {name} starts!\nInitializing with configs ...".format(**data))
    s = np.random.poisson(70, 10)
    print(s)

    num_trial = 10;

    time_stamp = np.arange(0,num_trial);
    car_type = np.zeros(shape=(num_trial,))
    which_lane = np.zeros(shape=(num_trial,))
    car_direction = np.zeros(shape=(num_trial,))
    car_id = np.arange(0,num_trial);
    for i in range(num_trial):
        car_type[i] = randint(0,3)
        which_lane[i] = randint(0,5)
        car_direction[i] = randint(0,3)

    global_q = Scene.vehicle_generate(time_stamp,car_type,car_direction,which_lane,car_id)

    Scene.pedestrain_generate()
    return

if __name__ == "__main__":
    args = parseArguments()
    print("arguments:", args)
    main() 
