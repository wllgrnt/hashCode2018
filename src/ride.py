class Ride:
    def __init__(self, ride_id, origin, destination, start_time, finish_time):
        self.ride_id = ride_id
        self.origin = origin
        self.destination = destination
        self.start_time = start_time
        self.finish_time = finish_time

    def __repr__(self):
        return f""""(ride_id: {self.ride_id},
    origin: {self.origin},
    destination: {self.destination},
    start time: {self.start_time},
    finish time: {self.finish_time}
)\n"""
