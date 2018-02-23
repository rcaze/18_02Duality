# A pet project I started with François to compute the dual of a Boolean
# function
import unittest
import numpy as np


def dual(in_function, dim):
    """compute the dual of a boolean function"""
    in_function = np.array([int(image) for i, image in enumerate(in_function)])
    in_function = in_function.tolist()
    in_function.reverse()
    out_function_tp = [str(int(0 == in_fct)) for i, in_fct in enumerate(in_function)]
    out_function = "".join(out_function_tp)
    return out_function
    """
    ants = [np.binary_repr(ant, dim) for i, ant in enumerate(range(2**dim))]
    inverted_ants = []
    for i, ant in enumerate(ants):
        inv_ant_tp = [int('0' == ant_in) for i, ant_in in enumerate(ant)]
        inverted_ant = "".join([str(strj) for strj in inv_ant_tp])
        inverted_ants.append(inverted_ant)
    """


class test_function(unittest.TestCase):
    def test_dual(self):
        # In
        ipt = ['00010000', '0001']
        # Arguments
        dim = [3, 2]
        # expected
        out_exp = ['11110111', '0111']
        # out
        for i in range(2):
            out = dual(ipt[i], dim[i])
            self.assertEqual(out_exp[i], out)

    def test_deux(self):
        self.assertEqual(0, 1)

if __name__ == "__main__":
    print(dual('0001', 2))
