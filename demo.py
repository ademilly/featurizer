import featurize

if __name__ == '__main__':

    print "Let's featurize"

    var = [
        i for i in range(1, 10)
    ]

    fsvc = featurize.Featurizer()
    print fsvc.featurize(var=var)
