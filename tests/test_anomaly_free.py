import unittest
import pandas as pd
from anomaly_free import methods

inputs_5 = {
    "n": 5,
    "m": 6,
    "N": 10000,
    "zmax": 30,
    "imax": 0,
    "output_name": "solution",
    "SAVE_FILE": False,
}

inputs_6 = {
    "n": 6,
    "m": 9,
    "N": 500000,
    "zmax": 30,
    "imax": 0,
    "output_name": "solution",
    "SAVE_FILE": False,
}


class Test_anomaly(unittest.TestCase):
    def test_n5(self):
        sls_5 = methods.find_several_sets(**inputs_5).z.to_numpy()
        self.assertEqual(11, sls_5.shape[0], True)

    def test_n6(self):
        sls_6 = methods.find_several_sets(**inputs_6).z.to_numpy()
        self.assertEqual(112, sls_6.shape[0], True)


if __name__ == "__main__":
    unittest.main()
