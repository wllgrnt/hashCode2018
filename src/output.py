from vehicle import Car
from ride import Ride

def writeSolution(fleet, fname):
    with open(fname, 'w') as f:
        for car in fleet:
            f.write(str(len(car.assigned_rides)))
            for ride in car.assigned_rides:
                f.write(" " + str(ride.ride_id))
            f.write('\n');

