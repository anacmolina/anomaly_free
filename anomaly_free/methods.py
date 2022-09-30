import os

import numpy as np
import pandas as pd

import multiprocessing as multiprocessing
import dask.array as da
import time as time


def generate_lk(n, m, N):
    """Generates a set of N vectors of integers l and k

    Eack element of l and k is minor or equal to absolute value of m

    Parameters
    ----------
    n : int
        Number z values for each solution that uses an l and k vector
    m : int
        Highest (or lowest) value that l or k element can be
    N : int
        Number of l and k vectors generated

    Returns
    -------
    array-like of ints
        a numpy array of integers with shape (N, n-2)
    """

    assert n >= 5

    lk = da.random.randint(-m, m + 1, (N, n - 2))
    lk = lk.to_dask_dataframe().drop_duplicates().to_dask_array()

    lk = lk.compute()

    return lk


def sorted_absval(x):
    """Sorts a vector according to the absolute value, from the highest to the lowest

    Eack element of l and k is minor or equal to absolute value of m
    The argument `x` must be a numpy array

    Parameters
    ----------
    x : array-like of ints
        Vector to be sorted

    Returns
    -------
    array-like of ints
        'x' numpy array sorted
    """
    return np.array(sorted(x, key=abs, reverse=True))


def linear_combination(x, y):
    """Compute the operation 'x + y' accordin to arXiv:1905.13729

    Parameters
    ----------
    x : array-like of ints
        Vectorlike
    y : array-like of ints
        Vectorlike

    Returns
    -------
    array-like
        Result of the operation
    """

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
    """Compute the operation 'up + um' (or 'vp + vm') according to arXiv:1905.13729

    Parameters
    ----------
    lk : array-like of ints
        Vectorlike with l and k vector concat in one vector

    Returns
    -------
    array-like
        Result of the operation
    """

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


class Anomaly:
    """
    Class that save the info of one solution set
    ...

    Attributes
    ----------
    l : array-like of ints
        vector l
    k : array-like of ints
        vector k
    z : array-like of ints
        solution set of U(1)
    gcd : int
        greates common divisor of z

    Methods
    -------
    __call__(lk)
        Computes z and save all the atributes values
    """

    def __call__(self, lk):
        """Computes the function vectorlike_sum

        Parameters
        ----------
        lk : array-like of ints
            Vectorlike with l and k vector concat in one vector

        """

        n = 2 + lk.shape[0]
        dim_l = int((n - 2) / 2)

        self.l = lk[:dim_l].flatten()
        self.k = lk[dim_l:].flatten()
        self.z, self.gcd = vectorlike_sum(lk)


class Valid_Set:
    """
    A class that filters if the solution is correct
     ...

    Attributes
    ----------
    zmax : int
        absoulte maximum value that z_i can be

    Methods
    -------
    __call__(lk)
        Filters all the solutions with:
            0 on z
            z_i > |zmax|
            z with trivial solution like z_i and -z_i
    """

    zmax = 30

    def __call__(self, lk):
        """Filters all valid sets

        Parameters
        ----------
        lk : array-like of ints
            Vectorlike with l and k vector concat in one vector

        Returns
        -------
        dict or {}
            {} when z is not a solution
            dict with the values of the solution: z, l, k, and gcd
        """

        data = Anomaly()
        data(lk)

        if (
            (0 in data.z)
            or (np.abs(data.z).max() > self.zmax)
            or np.unique(np.abs(data.z)).shape != np.unique(data.z).shape
        ):
            return {}

        else:

            results = {
                "z": data.z.tolist(),
                "l": data.l.tolist(),
                "k": data.k.tolist(),
                "gcd": data.gcd,
            }

            return results


def find_several_sets(n, m, N, zmax, imax, output_name, SAVE_FILE):
    """Compute the operation vectorlike_sum operation for N lk sets

    Parameters
    ----------
    n : int
        number of z values of each solution
    m : int
        max (min) value that l or k might take
    N: int
        max (min) value that l or k might take
    zmax: int
        max (min) value that z might take
    imax:
        maximum iterations to find z set from N the lk vectors
    output_name: str
        output file with the solutions
    SAVE_FILE: bool


    Returns
    -------
    array-like
        Result of the operation
    """

    Valid_Set.zmax = zmax

    filename = output_name + "_{}.csv".format(n)
    RELOAD = os.path.exists(filename)

    if RELOAD:
        df = pd.read_csv(filename)
        SAVE_FILE = True
    else:
        df = pd.DataFrame(columns=["z", "l", "k", "gcd"])

    ti = time.time()
    for i in range(imax + 1):

        lk = generate_lk(n, m, N)
        pool = multiprocessing.Pool()

        valid_set = Valid_Set()
        results = pool.map(valid_set, lk)
        results = [set for set in results if set]

        pool.close()

        del lk

        df = pd.concat([df, pd.DataFrame(results)])
        df = df.sort_values(by=["gcd"], ignore_index=True)

        df["copy"] = df["z"].astype(str)
        df = (
            df.drop_duplicates("copy")
            .drop("copy", axis="columns")
            .reset_index(drop=True)
        )

    ts = time.time()
    print("Time: {:.2f}s".format(ts - ti))
    print("# Solutions: {}".format(df.shape[0]))

    if SAVE_FILE:
        print("Solutions save in -> " + filename)
        df.to_csv(filename, index=False)
    else:
        print("U(1) SOLUTIONS FOR n={}, m={}, zmax={}\n".format(n, m, zmax))
        print(df)

    return df
