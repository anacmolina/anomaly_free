import unittest
import pandas as pd
from anomaly_free import methods

inputs = {
    "n": 5,
    "m": 6,
    "N": 10000,
    "zmax": 30,
    "imax": 0,
    "output_name": "solution",
    "SAVE_FILE": False,
}


class Test_anomaly(unittest.TestCase):
    def test_working(self):
        sls = methods.find_several_sets(**inputs).z.to_numpy()
        self.assertEqual(11, sls.shape[0], True)


if __name__ == "__main__":
    unittest.main()
