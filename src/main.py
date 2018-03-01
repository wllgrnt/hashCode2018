#!/usr/bin/env python
import argparse
from input import processInputFile
from output import writeSolution
from grid import getDistance

parser = argparse.ArgumentParser()
parser.add_argument("inputfile")
parser.add_argument("outputfile")
args = parser.parse_args()
fleet, rides = processInputFile(args.inputfile)

print('Rides:', rides)

for car in fleet:
    dist = None
    closest_ride = None
    for ride in rides:
        trial_dist = getDistance(car.current_position, ride.origin)
        if dist is None or trial_dist < dist:
            dist = trial_dist
            closest_ride = ride
    car.assign_ride(closest_ride)
    rides.pop(rides.index(closest_ride))

print('Fleet:', fleet)

writeSolution(fleet, args.outputfile)
