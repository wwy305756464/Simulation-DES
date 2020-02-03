import os
import collections
import argparse
import multiprocessing
import json
import time
from random import randint
import numpy as np
import math as mathå
import mpl_toolkits.mplot3d
import matplotlib
import matplotlib.pyplot as plt
import TrafficLight as tl
from scene import Scene
import server as sr

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
    dirpath = os.path.dirname(os.path.realpath(__file__))
    res_dir = results_dir = os.path.join(dirpath, 'outputs/')
    if not os.path.isdir(res_dir):
        os.makedirs(res_dir)
    print("saving ... {} plot ... ".format(name))
    x = time_stamps
    y = range(len(time_stamps))
    fig, ax = plt.subplots()
    plt.title(name)
    plt.ylabel('Events')
    plt.xlabel('Time in (s)')
    ax.scatter(x, y,marker="|",s=30)
    ax.scatter(x, y,marker="_",color='r', label=name+'(arrival)',s=3)
    ax.legend()
    plt.savefig(res_dir+name+'.png',dpi=600)

def save_poisson_hist_plot(poisson,name):
    print("saving ... {} plot ... ".format(name)) 
    dirpath = os.path.dirname(os.path.realpath(__file__))
    res_dir = results_dir = os.path.join(dirpath, 'outputs/')
    if not os.path.isdir(res_dir):
        os.makedirs(res_dir)
    fig, ax = plt.subplots()
    plt.title(name)
    plt.ylabel('count')
    plt.xlabel('bins')
    bin_num = (max(poisson)-min(poisson))*4
    n, bins, patches = plt.hist(poisson,bin_num, facecolor='b', alpha=0.75)
    plt.savefig(res_dir+name+'.png',dpi=600)



def main():
    args = parseArguments()
    with open('config.json') as json_config_file:
        data = json.load(json_config_file)
    print("Simulation process of {name} starts!\nInitializing with configs ...".format(**data))
    rng_seed = data["rng_seed"]
    main_scene = Scene(args.total_events,args.simulation_time,rng_seed)
    #  setting up input for vehicle_generate()
    initial_time_stamps, poisson = main_scene.poisson_generate_timestamps()
    num_trial = len(initial_time_stamps)
    car_type = np.zeros(shape=(num_trial,))
    which_lane = np.zeros(shape=(num_trial,))
    car_direction = np.zeros(shape=(num_trial,))
    car_id = np.arange(0, num_trial);
    for i in range(num_trial):
        car_type[i] = randint(0, 2)
        which_lane[i] = randint(0, 5)
        car_direction[i] = randint(0, 2)

    global_q = main_scene.vehicle_generate(initial_time_stamps, car_type, car_direction, which_lane,car_id)
    trafficLight = tl.TrafficLight(10,3,10)  # greenTime,yellowTime,redTime
    main_server = sr.server(trafficLight,global_q)
    updated_global_q = main_server.run()




    main_scene.pedestrain_generate()

    save_timestamps_plot(initial_time_stamps, 'Initial_Timestamps')
    save_poisson_hist_plot(poisson, 'Events_Poisson')
    return

if __name__ == "__main__":
    main() 
