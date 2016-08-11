from sklearn.naive_bayes import GaussianNB
import matplotlib.pyplot as plt

from random import shuffle

import featurize
import sample_generator


if __name__ == '__main__':

    print "Let's featurize"

    quadratic_gen = sample_generator.Quadratic()

    N = 1000
    X_0 = quadratic_gen.generate(N, radius=5, width=2)
    X_1 = quadratic_gen.generate(N, radius=10, width=2)

    show = False

    plt.scatter([_[0] for _ in X_0], [_[1] for _ in X_0], color='blue')
    plt.scatter([_[0] for _ in X_1], [_[1] for _ in X_1], color='red')

    if show:
        plt.show()

    fsvc = featurize.Featurizer()

    pop_0 = [(0, _) for _ in X_0]
    pop_1 = [(1, _) for _ in X_1]

    pop = pop_0 + pop_1
    shuffle(pop)

    X, y = [_[1] for _ in pop], [_[0] for _ in pop]

    clf = GaussianNB()
    clf.fit(X, y)
    print clf.score(X, y)

    fsvc.supervised_featurization(X, y)
