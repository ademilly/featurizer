from inspect import getmembers, isfunction

import functions


class Featurizer(object):

    def __init__(self, var_dict={}):

        self.func_list = [
            _ for _ in getmembers(functions) if isfunction(_[1])
        ]
        self.var_dict = {}

    def featurize(self, var):

        new_X = [
            f[1](var) for f in self.func_list
        ]

        return new_X
