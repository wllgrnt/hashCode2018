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
    # print('Assigning rides to vehicle {}/{}'.format(ind, len(fleet)))
    time = 0
    while len(rides) > 0 and time < all_time:
        # print('Time for vehicle {} = {}/{}'.format(ind, time, all_time))
        dist = None
        closest_ride = None
        for ride in rides:
            trial_dist = getDistance(car.current_position, ride.origin)
            if dist is None or trial_dist < dist:
                # check if the time taken to reach and perform the ride is feasible
                wait_time = max(int(ride.start_time) - (time + trial_dist), 0)
                if wait_time + trial_dist + ride.length <= int(ride.finish_time) - int(time):
                    # check if the time taken to reach and perform the ride is feasible
                    # if trial_dist + time < ride.start_time:
                    dist = trial_dist
                    best_ride = ride
        if dist is None:
            time = all_time + 1
        else:
            # print('Assigning {} to vehicle {}'.format(best_ride.ride_id, ind))
            car.time += best_ride.length + dist + wait_time
            time += car.time
            car.assign_ride(best_ride)
            ride_index = rides.index(best_ride)
            rides.pop(ride_index)
            ride_bar.update(1)
            # print('Remaining rides {}'.format(len(rides)))

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
