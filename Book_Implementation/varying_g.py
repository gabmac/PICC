
#import g_h_filter as filter
from g_h_filter import g_h_filter as filter
import matplotlib.pylab as pylab
import matplotlib.pyplot as plt
import kf_book.book_plots as book_plots
from kf_book.gh_internal import plot_g_h_results
from white_noise import gen_data as gen_data
import numpy as np


g = [0.1, 0.4, 0.8]
noise_factor = 50
dx = 5
count = 50
x0 = 5
dt = 1
h = 0.01


#re-seed the generation
np.random.seed(100)
vector = gen_data(x0 = x0, dx = dx, count = count, noise_factor = noise_factor)
data = range(3*len(vector))
data = np.reshape(data,(3,len(vector)))

for i in range(len(g)):
    data[i] = filter(data=vector, x0=0., dx=5., dt=1., g=g[i], h=0.01)

with book_plots.figsize(y=4):
    book_plots.plot_measurements(vector, color='k')
    book_plots.plot_filter(data[0], label='g=0.1', marker='s', c='C0')
    book_plots.plot_filter(data[1], label='g=0.4', marker='v', c='C1')
    book_plots.plot_filter(data[2], label='g=0.8', c='C2')
    plt.legend(loc=4)
    book_plots.set_limits([20, 40], [50, 250])
    plt.grid()
    plt.show()




zs = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
for i in range(50):
    zs.append(14)

data1 = filter(data=zs, x0=4., dx=1., dt=1., g=0.1, h=0.01)
data2 = filter(data=zs, x0=4., dx=1., dt=1., g=0.5, h=0.01)
data3 = filter(data=zs, x0=4.,      dx=1., dt=1., g=0.9, h=0.01)
with book_plots.figsize(y=4):
    book_plots.plot_measurements(zs)
    book_plots.plot_filter(data1, label='g=0.1', marker='s', c='C0')
    book_plots.plot_filter(data2, label='g=0.5', marker='v', c='C1')
    book_plots.plot_filter(data3, label='g=0.9', c='C3')
    plt.legend(loc=4)
    plt.ylim([6, 20]);
    plt.show()
