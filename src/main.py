#!/usr/bin/env python
import argparse
from input import processInputFile
from output import writeSolution
from grid import getDistance

parser = argparse.ArgumentParser()
parser.add_argument("inputfile")
args = parser.parse_args()
fleet, rides = processInputFile(args.inputfile)

print('Fleet:', fleet)
print('Rides:', rides)

for car in fleet:
    dist = 1000000
    cloest_ride = None
    for ride in rides:
        if (getDistance(car.current_position, ride.origin) < dist):
            dist = getDistance(car.current_position, ride.origin)
            cloest_ride = ride
    car.assign_ride(ride)
    rides.pop(rides.index(ride))

writeSolution(fleet, "../out/out.txt")
