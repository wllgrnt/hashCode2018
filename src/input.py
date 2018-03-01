import os


class Car():
    def __init__(self):
        pass


class Ryder():
    def __init__(self):
        pass


def processInputFile(inputFileName):
    """Read the input file, pull the data."""
    print("processing", os.path.basename(inputFileName))
    with open(inputFileName) as flines:
        inputData = [line.strip().split(" ") for line in flines]

    R, C, F, N, B, T = [int(x) for x in inputData[0]]

    # initialise the fleet
    fleet = [Car() for i in range(F)]

    rides = []
    for line in inputData[1:]:
        start_row, start_column, finish_row, finish_column, earliest_start, latest_finish = line
        ryder = Ryder(
            origin=(start_row, start_column),
            destination=(finish_row, finish_column),
            earliest_start=earliest_start,
            latest_finish=latest_finish)
        rides.append(ryder)

    return fleet, rides
