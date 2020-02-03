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
import matplotlib.pyplot as plt
from scene import Scene

_author_  = 'Muyang Guo, Wei Zhao, Shushu Zhao, Wenyue Wang'

def parseArguments():
    '''

    simulation time:

    '''
    parser = argparse.ArgumentParser()
    parser.add_argument('total_events', help = ':indicate the total events would like to simulate, requested here', type=float, default = 100)
    parser.add_argument('simulation_time', help = ':indicate simulation duration time, unit is hour, requested here', type=float, default = 1)

    args = parser.parse_args()
    return args

def save_timestamps_plot(time_stamps,name):
    print("saving ... {} plot ... ".format(name))
    x = time_stamps
    y = range(len(time_stamps))
    fig, ax = plt.subplots()
    plt.title(name)
    plt.ylabel('Events')
    plt.xlabel('Time in (s)')
    ax.scatter(x, y,marker="|",s=300)
    ax.scatter(x, y,marker="_",color='r', label=name+'(arrival)')
    ax.legend()
    plt.savefig(name+'.png',dpi=1200)

def main():
    args = parseArguments()
    with open('config.json') as json_config_file:
        data = json.load(json_config_file)
    print("Simulation process of {name} starts!\nInitializing with configs ...".format(**data))
    main_scene = Scene(args.total_events,args.simulation_time)
    initial_time_stamps = main_scene.poisson_generate_timestamps()
    
    main_scene.vehicle_generate()
    main_scene.pedestrain_generate()

    save_timestamps_plot(initial_time_stamps,'Initial_Timestamps')
    return

if __name__ == "__main__":
    main() 
