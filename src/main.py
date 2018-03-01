#!/usr/bin/env python
import argparse
from input import processInputFile
from output import writeSolution
from grid import getDistance
from copy import deepcopy

parser = argparse.ArgumentParser()
parser.add_argument("inputfile")
parser.add_argument("outputfile")
args = parser.parse_args()
fleet, rides, all_time = processInputFile(args.inputfile)
total_num_rides = len(rides)

# print('Rides:', rides)
for ind, car in enumerate(fleet):
    print('Assigning rides to vehicle {}/{}'.format(ind, len(fleet)))
    time = 0
    while len(rides) > 0 and time < all_time:
        print('Time for vehicle {} = {}/{}'.format(ind, time, all_time))
        dist = None
        closest_ride = None
        for ride in rides:
            trial_dist = getDistance(car.current_position, ride.origin)
            if dist is None or trial_dist < dist:
                # check if the time taken to reach and perform the ride is feasible
                if trial_dist + ride.length < int(ride.finish_time) - int(time):
                    # check if the time taken to reach and perform the ride is feasible
                    # if trial_dist < int(ride.start_time) - int(time):
                    dist = trial_dist
                    best_ride = ride
        if dist is None:
            time = all_time + 1
        else:
            print('Assigning {} to vehicle {}'.format(best_ride.ride_id, ind))
            car.time += best_ride.length + dist
            time += car.time
            car.assign_ride(best_ride)
            ride_index = rides.index(best_ride)
            rides.pop(ride_index)
            print('Remaining rides {}'.format(len(rides)))

rides_fulfilled = 0
for ind, car in enumerate(fleet):
    print('{} {}'.format(ind, car.num_rides))
    rides_fulfilled += car.num_rides

print('Fulfilled {}/{} rides'.format(rides_fulfilled, total_num_rides))

writeSolution(fleet, args.outputfile)
