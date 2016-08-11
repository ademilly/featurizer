import math
import numpy as np

from sample_generator import Generator


class Quadratic(Generator):

    def __init__(self):
        pass

    def generate(self, sample_size, radius=0.0, width=1.0):
        r = np.random.normal(loc=radius, scale=width, size=sample_size)
        theta = np.random.uniform(0.0, 2.0 * math.pi, size=sample_size)

        return [
            [x, y] for x, y in zip(r * np.cos(theta), r * np.sin(theta))
        ]
