import argparse
from anomaly.methods import find_several_set
from anomaly.args import args

inputs = {"n": 5, "m": 6, "N": 1000, "zmax": 30, "imax": 0, "output_name": "solution"}

for arg in args.__dict__:
    if args.__dict__[arg] is not None:
        inputs[arg] = args.__dict__[arg]

N_unique = (2 * inputs["m"] + 1) ** (inputs["n"] - 2)

if args.suggested_N:

    print("N={}*10 for n={} and m={}".format(N_unique, inputs["n"], inputs["m"]))

else:
    del inputs["suggested_N"]

    df = find_several_set(**inputs)

    print(
        "U(1) SOLUTIONS FOR n={}, m={}, zmax={}\n".format(
            inputs["n"], inputs["m"], inputs["zmax"]
        )
    )

    print(df)