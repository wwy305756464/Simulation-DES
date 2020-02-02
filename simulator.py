import os
import collections
import argparse
import multiprocessing
import json
import time
import numpy as np
import math as math
import mpl_toolkits.mplot3d
import matplotlib
from scene import Scene

_author_  = 'Muyang Guo, Wei Zhao, Shushu Zhao, Wenyue Wang'

def parseArguments():
    '''
    random generator seed: 
    simulation time:

    '''
    parser = argparse.ArgumentParser()
    parser.add_argument('seed', help = 'put the seed number for the random number generator', type=float, default = 1)
    args = parser.parse_args()
    return args

def main():
    with open('config.json') as json_config_file:
        data = json.load(json_config_file)
    print("Simulation process of {name} starts!\nInitializing with configs ...".format(**data))
    Scene.vehicle_generate()
    Scene.pedestrain_generate()
    return

if __name__ == "__main__":
    args = parseArguments()
    print("arguments:", args)
    main() 
