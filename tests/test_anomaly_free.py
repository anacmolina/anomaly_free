from statistics import mean
import unittest
import pandas as pd
from anomaly_free import methods

inputs = {
    "n": 5,
    "m": 6,
    "N": 1000,
    "zmax": 30,
    "imax": 0,
    "output_name": "solution",
}

class Test_anomaly(unittest.TestCase):
    def test_working(self):
        sls = methods.find_several_set(**inputs).z.to_numpy()
        self.assertEqual(11, sls.shape[0], True)


if __name__ == "__main__":
    unittest.main()
