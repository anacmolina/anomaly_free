import numpy as np
import pandas as pd

import multiprocessing as multiprocessing
import dask.array as da

from inputs import inputs


def generate_lk(n, m, N):

    assert n >= 5

    # Add how to use this function

    lk = da.random.randint(-m, m + 1, (N, n-2))
    lk = lk.to_dask_dataframe().drop_duplicates().to_dask_array()

    lk = lk.compute()

    return lk


def sorted_absval(x):
    return np.array(sorted(x, key=abs, reverse=True))


def linear_combination(x, y):

    result = np.sum(x * (y**2)) * x - np.sum((x**2) * y) * y

    result = sorted_absval(result).astype(int)

    if result[0] < 0:
        result = result * (-1)

    gcd = np.gcd.reduce(result)

    if gcd != 0:
        result = result / gcd
    else:
        result = result

    return result.astype(int), gcd


def vectorlike_sum(lk):

    n = 2 + lk.shape[0]
    dim_l = int((n - 2) / 2)

    l, k = lk[:dim_l].flatten(), lk[dim_l:].flatten()

    if (n % 2) == 0:

        vp = np.hstack([l[0], k, (-1) * l[0], (-1) * k])
        vm = np.hstack([np.zeros(2), l, (-1) * l])

        return linear_combination(vp, vm)

    elif (n % 2) != 0:

        up = np.hstack([np.zeros(1), k, (-1) * k])
        um = np.hstack([l, k[0], np.zeros(1), (-1) * l, (-1) * k[0]])

        return linear_combination(up, um)


def valid_set(lk, zmax=inputs["zmax"]):

    data = Anomaly()
    data.compute(lk)

    if (
        (0 in data.z)
        or (np.abs(data.z).max() > zmax)
        or np.unique(np.abs(data.z)).shape != np.unique(data.z).shape
    ):
        return {}

    else:

        results = {
            "z": data.z.tolist(),
            "lk": data.lk.tolist(),
            "gcd": data.gcd,
        }

        return results


class Anomaly:
    def compute(self, lk):

        self.lk = lk
        self.z, self.gcd = vectorlike_sum(self.lk)


def find_several_set(n=inputs["n"], m=inputs["m"], N=inputs["N"]):

    lk = generate_lk(n, m, N)
    pool = multiprocessing.Pool()

    results = pool.map(valid_set, lk)
    results = [set for set in results if set]

    del lk

    df = pd.DataFrame(results)
    df = df.sort_values(by = ['gcd'], ignore_index=True)

    df['copy'] = df['z'].astype(str)
    df = df.drop_duplicates('copy').drop('copy', axis='columns').reset_index(drop=True)

    return df
