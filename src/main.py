import argparse
from input import processInputFile


parser = argparse.ArgumentParser()
parser.add_argument("inputfile")
args = parser.parse_args()
fleet = processInputFile(args.inputfile)

print(fleet)