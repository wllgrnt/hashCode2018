#!/usr/bin/env python
import argparse
from input import processInputFile
from output import writeSolution

parser = argparse.ArgumentParser()
parser.add_argument("inputfile")
args = parser.parse_args()
fleet, rides = processInputFile(args.inputfile)

print('Fleet:', fleet)
print('Rides:', rides)


writeSolution(fleet, "out.txt")
