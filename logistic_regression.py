import numpy as np
import matplotlib.pyplot as plt


class LogisticRegression:
    def __init__(self):

        self.n_plot = 0

        r = lambda x, y: np.random.randint(x, y)
        self.x = [[r(1, 10), r(1, 10)] for _ in range(25)]
    
    def visualize(self, title='Logistic Regression', show=False):

        x_cor = [x[0] for x in self.x]
        y_cor = [y[1] for y in self.x]

        plt.figure(self.n_plot)
        plt.scatter(x_cor, y_cor)

        plt.xlabel = 'X'
        plt.ylabel = 'Y'
        plt.title = title

        if show:
            plt.show()

        self.n_plot += 1

if __name__ == '__main__':
    lr = LogisticRegression()
    lr.visualize(show=True)
