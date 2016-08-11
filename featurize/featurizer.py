import numpy as np
from inspect import getmembers, isfunction
from sklearn.naive_bayes import GaussianNB

import functions


class Featurizer(object):

    def __init__(self, var_dict={}):

        self.func_list = [
            _ for _ in getmembers(functions) if isfunction(_[1])
        ]
        self.var_dict = {}
        self.clf = GaussianNB()

    def featurize(self, var):

        new_X = [
            f[1](var) for f in self.func_list
        ]

        return new_X

    def supervised_featurization(self, X, y):

        for new_X, function_name in (
            ([f[1](x) for x in X], f[0]) for f in self.func_list
        ):
            self.clf.fit(np.array(new_X).reshape(-1, 1), y)
            print function_name, self.clf.score(
                np.array(new_X).reshape(-1, 1), y
            )
