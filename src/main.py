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
fleet, rides, all_time, bonus = processInputFile(args.inputfile)
total_num_rides = len(rides)

ride_bar = tqdm.tqdm(total=len(rides))

while len(rides) > 0:
    # for ind, car in tqdm.tqdm(enumerate(fleet), total=len(fleet)):
    assigned = False
    for ind, car in enumerate(fleet):
        time = int(car.time)
        if car.time < all_time:
            # print('Time for vehicle {} = {}/{}'.format(ind, time, all_time))
            best_score_per_time = None
            quickest_finish_time = None
            for ride in rides:
                trial_dist = int(getDistance(car.current_position, ride.origin))
                wait_time = max(int(ride.start_time) - (time + trial_dist), 0)
                projected_finish_time = wait_time + trial_dist + ride.length
                score = ride.length + bonus
                if trial_dist <= int(ride.start_time) - int(time):
                    score += bonus
                # score_per_time = score / (projected_finish_time - time)
                # if ride finishes sooner than all others
                if quickest_finish_time is None or projected_finish_time < quickest_finish_time:
                # if best_score_per_time is None or score_per_time > best_score_per_time:
                    # if ride finishes in time allowed
                    if projected_finish_time <= int(ride.finish_time):
                        dist = trial_dist
                        best_ride = ride
                        quickest_finish_time = projected_finish_time
                        # best_score_per_time = score_per_time
            if quickest_finish_time is None:
                time = all_time + 1
            else:
                assigned = True
                car.time += best_ride.length + dist + wait_time
                time += car.time
                car.assign_ride(best_ride)
                ride_index = rides.index(best_ride)
                rides.pop(ride_index)
                ride_bar.update(1)
    if ind == len(fleet) - 1 and not assigned:
        break
            # print('Remaining rides {}'.format(len(rides)))

ride_bar.close()

rides_fulfilled = 0
hist_dict = {i: 0 for i in range(5)}
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
