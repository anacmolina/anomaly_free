from methods import find_several_set
from args import args

inputs = {"n": 5, "m": 6, "N": 1000, "zmax": 30, "imax": 0, "output_name": "solution"}

for arg in args.__dict__:
    if args.__dict__[arg] is not None:
        inputs[arg] = args.__dict__[arg]

N_unique = (2 * inputs["m"] + 1) ** (inputs["n"] - 2)


df = find_several_set(**inputs)

print(
    "SOLUTIONS FOR n={}, m={}, zmax={}\n".format(
        inputs["n"], inputs["m"], inputs["zmax"]
    )
)

print(df)
