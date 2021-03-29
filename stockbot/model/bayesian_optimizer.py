from sklearn.gaussian_process import GaussianProcessRegressor as GP
from sklearn.gaussian_process.kernels import Kernel
from modAL import acquisition as acquisitions
from modAL.models import BayesianOptimizer as BayesOpt
from enum import Enum
import matplotlib.pyplot as plt


class Acquisition(Enum):
    EI = 1
    PI = 2
    UCB = 3


class BayesianOptimizer(BayesOpt):

    def __init__(self, kernel: Kernel, acquisition: Acquisition):
        """

        Args:
            kernel:
            acquisition:
        """
        super(BayesianOptimizer, self).__init__(
            estimator=GP(kernel=kernel),
            query_strategy=getattr(acquisitions, f"max_{acquisition.name}")
        )
        self._y_predict, self._y_std = None, None

    @property
    def y_predict(self):
        return self._y_predict.ravel()

    @property
    def y_std(self):
        return self._y_std.ravel()

    def fit_samples(self, X, y):
        for i in range(len(y)):
            query_idx, query_inst = self.query(X)
            self.teach(X[query_idx].reshape(1, -1), y[query_idx].reshape(1, -1))

        y_pred, y_std = self.predict(X, return_std=True)
        y_pred, y_std = y_pred.ravel(), y_std.ravel()
        X_max, y_max = self.get_max()
        with plt.style.context('seaborn-white'):
            plt.figure(figsize=(10, 5))
            plt.scatter(self.X_training, self.y_training, c='k', s=50, label='Queried')
            plt.scatter(X_max, y_max, s=100, c='r', label='Current optimum')
            plt.plot(X.ravel(), y, c='k', linewidth=2, label='Function')
            plt.plot(X.ravel(), y_pred, label='GP regressor')
            plt.fill_between(X.ravel(), y_pred - y_std, y_pred + y_std, alpha=0.5)
            plt.title('First five queries of Bayesian optimization')
            plt.legend()
            plt.show()
