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
#ja dado, porém com uma aceleracao
#IMPORTANTE: o filto implementado nao responde
#bem a variação de aceleracao e por isso
# a resposta desse código não estará perto
# do esperado
#############################################
def gen_data(x0, dx, count, noise_factor, accel = 0):
    vector = []
    for i in range(count):
        vector.append(x0 + dx*i + randn()*noise_factor)
        dx += accel

    return vector

#############################################
#exemplo do livro
#############################################

#predictions = []
#zs = gen_data(x0=10., dx=0., count=20, noise_factor=0, accel=2.)
#data = filter(data=zs, x0=10., dx=0., g=0.2, h=0.02, dt = 1.0)
#plt.xlim([0, 20])
#plot_g_h_results(measurements=zs, filtered_data=data)
#plt.show()
