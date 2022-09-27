import unittest
import pandas as pd

inputs = {
    "n": 5,
    "m": 6,
    "N": 1000,
    "zmax": 30,
    "imax": 0,
    "output_name": "solution",
}

sls_5 = pd.DataFrame(columns=["z"])
data_5 = [
    [10, -9, -7, 4, 2],
    [26, -25, -14, 9, 4],
    [28, -25, -23, 18, 2],
    [20, -18, -17, 14, 1],
    [26, -22, -20, 9, 7],
    [22, -21, -12, 6, 5],
    [9, -8, -7, 5, 1],
    [27, -25, -17, 8, 7],
    [27, -26, -14, 8, 5],
    [28, -26, -18, 11, 5],
    [25, -22, -18, 8, 7],
]

sls_5.z = data_5

print(sls_5)


class Test_anomaly(unittest.TestCase):
    def test_working(self):
        self.assertEqual(1, 1, True)


if __name__ == "__main__":
    unittest.main()
