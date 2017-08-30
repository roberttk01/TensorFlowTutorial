from statistics import mean
import numpy as np
import random
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')


def create_dataset(hm, variance, step=2, correlation=False):
    '''
    :param hm: The value will be "how much" (i.e.- # of datapoints)
    :param variance: This will dictate how much each point can vary from the previous point
    :param step: This will be how far to step on average per point (default is 2)
    :param correlation: This will be either False, pos, or neg to indicate taht we want no correlation, positive
    correlation, or negative correlation
    :return:
    '''

    val = 1
    ys = []
    for i in range(hm):

        y = val + random.randrange(-variance, variance)
        ys.append(y)

        if correlation and correlation == 'pos':
            val += step
        elif correlation and correlation == 'neg':
            val -= step

    xs = [i for i in range(len(ys))]

    return np.array(xs, dtype=np.float64), np.array(ys, dtype=np.float64)


def best_fit_slope_and_intercept(xs, ys):
    m = ((mean(xs) * mean(ys)) - mean(xs * ys)) / (mean(xs)**2 - mean(xs**2))
    b = mean(ys) - m * mean(xs)
    return m, b


def squared_error(ys_orig, ys_line):
    return sum((ys_line - ys_orig) * (ys_line - ys_orig))


def coefficient_of_determination(ys_orig, ys_line):
    y_mean_line = [mean(ys_orig) for y in ys_orig]
    squared_error_regr = squared_error(ys_orig, ys_line)
    squared_error_y_mean = squared_error(ys_orig, y_mean_line)
    return 1 - (squared_error_regr/squared_error_y_mean)

xs, ys = create_dataset(40, 10, 2, correlation="pos")
m, b = best_fit_slope_and_intercept(xs, ys)
regression_line = [(m * x + b) for x in xs]

r_squared = coefficient_of_determination(ys, regression_line)
print(r_squared)

plt.scatter(xs, ys, color='#003F72', label='data')
plt.plot(xs, regression_line, label='regression line')
plt.legend(loc=4)
plt.show()