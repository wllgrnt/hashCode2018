#!/usr/bin/env python
import argparse
from input import processInputFile
from output import writeSolution
from grid import getDistance
from copy import deepcopy
from ascii_graph import Pyasciigraph
import tqdm

parser = argparse.ArgumentParser()
parser.add_argument("inputfile")
parser.add_argument("outputfile")
args = parser.parse_args()
fleet, rides, all_time, bonus = processInputFile(args.inputfile)
total_num_rides = len(rides)

ride_bar = tqdm.tqdm(total=len(rides))

while len(rides) > 0:
    assigned = False
    for ind, car in enumerate(fleet):
        time = int(car.time)
        if car.time < all_time:
            best_score_per_time = None
            best_ride = None
            for ride_ind, ride in enumerate(rides):
                trial_dist = int(getDistance(car.current_position, ride.origin))
                wait_time = max(int(ride.start_time) - (time + trial_dist), 0)
                time_to_complete = trial_dist + wait_time + ride.length
                projected_finish_time = time_to_complete + time 
                if projected_finish_time < int(ride.finish_time):
                    score = ride.length
                    if trial_dist <= int(ride.start_time) - int(time):
                        score += bonus
                    score_per_time = score / time_to_complete
                    if best_score_per_time is None or score_per_time > best_score_per_time:
                        dist = trial_dist
                        best_ride = ride
                        best_ride_ind = ride_ind
                        best_wait_time = wait_time
                        best_score_per_time = score_per_time
                        best_ride.projected_finish_time = projected_finish_time
                        best_ride.time_to_complete = time_to_complete
            if best_ride is None:
                time = all_time + 1
            else:
                assigned = True
                if best_ride.projected_finish_time < all_time:
                    car.time += best_ride.time_to_complete
                    car.current_position = best_ride.destination
                    car.assign_ride(best_ride)
                    ride_index = best_ride_ind
                    rides.pop(ride_index)
                    ride_bar.update(1)
    if ind == len(fleet) - 1 and not assigned:
        break

ride_bar.close()

rides_fulfilled = 0
hist_dict = {i: 0 for i in range(5)}
for ind, car in enumerate(fleet):
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
