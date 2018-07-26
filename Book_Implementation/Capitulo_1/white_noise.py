#importa a funcao para criar o white noise
from numpy.random import randn
#import g_h_filter as filter
from g_h_filter import g_h_filter as filter
import matplotlib.pylab as pylab
import matplotlib.pyplot as plt
import kf_book.book_plots as book_plots
from kf_book.gh_internal import plot_g_h_results


#############################################
#cria um vetor em cima do seu valor inicial
#e os proximos valores sao gerados com passos
#ja dado
#############################################
def gen_data(x0, dx, count, noise_factor):
    return [x0 + dx*i + randn()*noise_factor for i in range(count)]



#############################################
#exemplo do livro
#############################################

#measurements = gen_data(0, 1, 30, 1)
#data = filter(data=measurements, x0=0., dx=1., dt=1., g=.2, h=0.02)
#plot_g_h_results(measurements, data)
#plt.show()
