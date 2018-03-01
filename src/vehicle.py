class Car:

    def __init__(self):
        self.assigned_rides = []
        self.current_position = [0, 0]
        self.current_ride = None
        self.destination = [None, None]
        self.cumulative_score = 0
        self.laden = False
        self.time = 0

    def __repr__(self):
        return (('\nVehicle object:\nAt t={}, vehicle is at ({}, {}) with {} passenger{} '
                 'heading to ({}, {}).\n'
                 'Current score: {}.\n'
                 'Next rides: {}\n')
                .format(self.time,
                        self.current_position[0], self.current_position[1],
                        'a' if self.laden else '0',
                        '' if self.laden else 's',
                        self.destination[0], self.destination[1],
                        self.cumulative_score,
                        self.assigned_rides))

    def assign_ride(self, ride):
        self.assigned_rides.append(ride)

    def pass_time(self):
        if self.laden:
            self.destination = self.current_ride.destination
        else:
            self.destination = self.current_ride.origin

        # load up or unload as necessary
        if self.destination == self.current_position and self.current_ride.start_time >= self.time:
            self.laden = True

        # move towards destination
        x_to_travel = self.destination[0] - self.current_position[0]
        y_to_travel = self.destination[1] - self.current_position[1]
        if x_to_travel > 0:
            self.current_position[0] += 1
        elif x_to_travel < 0:
            self.current_position[0] -= 1
        elif y_to_travel > 0:
            self.current_position[1] += 1
        elif y_to_travel < 0:
            self.current_position[1] -= 1

        self.time += 1

    @property
    def num_rides(self):
        return len(self.assigned_rides)
