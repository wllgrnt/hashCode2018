import argparse

from input import processInputFile
from grid import getDistance

# from output import writeSolution
# from grid import getDistance

parser = argparse.ArgumentParser()
parser.add_argument("inputfile")
parser.add_argument("outputfile")
args = parser.parse_args()
print("input from", args.inputfile)
print("solution at", args.outputfile)

fleet, rides, all_time, bonus = processInputFile(args.inputfile)

# make a dict of the rides
ridesDict = {
    str(x.ride_id): {
        "origin": x.origin,
        "destination": x.destination,
        "start_time": x.start_time,
        "finish_time": x.finish_time,
        "is_assigned": False
    }
    for x in rides
}

with open(args.outputfile) as flines:
    fleetAssignment = [line.strip().split(" ")[1:] for line in flines]

score = 0
for rideIds in fleetAssignment:
    time = 0
    current_position = (0, 0)
    for rideId in rideIds:
        rideInfo = ridesDict[rideId]
        print("picking up", rideId, " at time ", time)
        print("current position", current_position)
        print("ride is at", rideInfo['origin'])
        time += getDistance(current_position, rideInfo['origin'])
        current_position = rideInfo['origin']
        if time < int(rideInfo['start_time']):
            print("bonus!")
            score += bonus
            time = int(rideInfo['start_time'])
        time += getDistance(current_position, rideInfo['destination'])
        if time < int(rideInfo['finish_time']):
            print("ride success!")
            score += getDistance(current_position, rideInfo['destination'])
        else:
            print("too slow!")
        current_position = rideInfo['destination']
        # print(ridesDict[rideId])
print("Final score:", score)
