import argparse

parser = argparse.ArgumentParser(description="Anomaly free package")

parser.add_argument(
    "n",
    type=int,
    action="store",
    help="number z values for each solution",
)

parser.add_argument(
    "--N",
    type=int,
    required=False,
    action="store",
    help="number of l and k vectors",
)

parser.add_argument(
    "--m",
    type=int,
    required=False,
    action="store",
    help="max (min) value that l or k might take",
)

parser.add_argument(
    "--zmax",
    type=int,
    required=False,
    action="store",
    help="max (min) value that z might take",
)

parser.add_argument(
    "--imax",
    type=int,
    required=False,
    action="store",
    help="maximum iterations to find z set from N the lk vectors",
)

parser.add_argument(
    "--output_name",
    nargs="?",
    help="optional output file with all the solutions",
)

args = parser.parse_args()
