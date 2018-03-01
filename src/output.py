from vehicle import Car
from ride import Ride

def write_solution(fleet, fname):
    with open(fname, 'w') as f:
        for car in fleet:
            f.write(len(car.assigned_rides))
            for ride in car.assigned:
                f.write(" " + str(ride.id))
            f.write('\n');

