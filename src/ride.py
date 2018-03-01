from grid import getDistance


class Ride:
    def __init__(self, ride_id, origin, destination, start_time, finish_time):
        self.ride_id = int(ride_id)
        self.origin = origin
        self.destination = destination
        self.start_time = int(start_time)
        self.finish_time = int(finish_time)
        self.length = int(getDistance(self.origin, self.destination))

    def __repr__(self):
        return f""""(ride_id: {self.ride_id},
    origin: {self.origin},
    destination: {self.destination},
    start time: {self.start_time},
    finish time: {self.finish_time}
)\n"""
