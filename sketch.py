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
N = 5000
T = 1
lamda = float(N)/float(T)/60.0/60.0 #per second
Time = int(T*60.0*60.0) #total seond
poisson = np.random.poisson(lamda,Time)
time_stamps=[]
time_stamp = 0.0
for p in poisson:
    if p != 0:
        event_time = np.random.uniform(0,1.0,p)# per second, unit interval
        for t_s in event_time:
            time_stamp=time_stamp+t_s;
            time_stamps.append(time_stamp)
    else:
        time_stamp = time_stamp+1.0
np.sort(time_stamps)
total_sim_event = len(time_stamps)
sim_mean = np.mean(poisson)

n, bins, patches = plt.hist(poisson,60, facecolor='b', alpha=0.75)
plt.show()


# # setup toolbar
# sys.stdout.write("[%s]" % (" " * toolbar_width))
# sys.stdout.flush()
# sys.stdout.write("\b" * (toolbar_width+1)) # return to start of line, after '['

# for i in range(toolbar_width):
#     # time.sleep(0.1) # do real work here
#     # update the bar
#     sys.stdout.write("-")
#     sys.stdout.flush()

# sys.stdout.write("]\n") # this ends the progress bar

