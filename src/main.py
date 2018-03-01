#!/usr/bin/env python
import argparse
from input import processInputFile
from output import writeSolution
from grid import getDistance
from ascii_graph import Pyasciigraph
import tqdm

parser = argparse.ArgumentParser()
parser.add_argument("inputfile")
parser.add_argument("outputfile")
args = parser.parse_args()
fleet, rides, all_time = processInputFile(args.inputfile)
total_num_rides = len(rides)

ride_bar = tqdm.tqdm(total=len(rides))

for ind, car in tqdm.tqdm(enumerate(fleet), total=len(fleet)):
    while (True):
        best_ride = None
        best_score = 0
        for ride in rides:
            dist = getDistance(car.current_position, ride.origin)
            length = ride.length
            bonus = (int(car.time) + dist < int(ride.start_time))

            if (max(int(car.time) + dist + ride.length, int(ride.start_time)) > int(ride.finish_time)):
                continue

            #if bonus and length > best_score:
            if length > best_score:
                best_score = length
                best_ride = ride

        if (best_ride == None):
            break

        car.assign_ride(best_ride)
        rides.pop(rides.index(best_ride))
        car.pass_time_until_free()




ride_bar.close()

rides_fulfilled = 0
hist_dict = {}
for ind, car in enumerate(fleet):
    # print('{} {}'.format(ind, car.num_rides))
    if car.num_rides not in hist_dict:
        hist_dict[car.num_rides] = 0
    hist_dict[car.num_rides] += 1
    rides_fulfilled += car.num_rides

sorted_keys = sorted(hist_dict.keys())
hist = []
for key in sorted_keys:
    hist.append((key, hist_dict[key]))

print('\n\nFulfilled {}/{} rides'.format(rides_fulfilled, total_num_rides))

graph = Pyasciigraph()
for line in graph.graph('cars num_rides', hist):
    print(line)

writeSolution(fleet, args.outputfile)
