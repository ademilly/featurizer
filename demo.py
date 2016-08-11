import numpy as np
import random

import featurize


if __name__ == '__main__':

    print "Let's featurize"

    r, theta = np.random.normal(size=1000), np.random.uniform(
        low=0.0,
        high=2.0 * np.pi
    )
    x_0, y_0 = r * np.cos(theta), r * np.sin(theta)
    X_0 = list(zip(x_0, y_0))
    t_0 = [0 for _ in x_0]

    r, theta = np.random.normal(loc=2.0, size=1000), np.random.uniform(
        low=0.0,
        high=2.0 * np.pi
    )
    x_1, y_1 = r * np.cos(theta), r * np.sin(theta)
    X_1 = list(zip(x_1, y_1))
    t_1 = [1 for _ in x_0]

    X = X_0 + X_1
    y = t_0 + t_1

    data = zip(X, y)
    random.shuffle(data)

    X[:], y[:] = zip(*data)

    print X[0], y[0]

    fsvc = featurize.Featurizer()
    fsvc.supervised_featurization(X, y)
