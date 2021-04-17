import unittest
from stockbot.investor.model.bayesian_optimizer import BayesianOptimizer, Acquisition
from sklearn.gaussian_process.kernels import Matern
import numpy as np


class TestBayesianOptimizer(unittest.TestCase):

    def test_fit(self):
        X = np.linspace(0, 20, 50).reshape(-1, 1)
        y = np.sin(X) / 2 - ((10 - X) ** 2) / 50 + 30 * (np.random.random() - 0.5)
        optimizer = BayesianOptimizer(
            kernel=Matern(length_scale=3.0),
            acquisition=Acquisition.EI
        )
        optimizer.fit_samples(X, y)


if __name__ == '__main__':
    unittest.main()
