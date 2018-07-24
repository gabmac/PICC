import numpy as np
from kf_book.gh_internal import plot_g_h_results
import matplotlib.pylab as pylab
import matplotlib.pyplot as plt
import kf_book.book_plots as book_plots
###############################################################
#Performs g-h filter on 1 state variable with a fixed g and h.
#'data' contains the data to be filtered.
#'x0' is the initial value for our state variable
#'dx' is the initial change rate for our state variable
#'g' is the g-h's g scale factor
#'h' is the g-h's h scale factor
#'dt' is the length
##############################################################

##############################################################
#detalhe importante as atualizacoes pelos residuaias nada mais
#e do que apenas media aritmetica, entre o medido e o valor que
#se tem.
#a todo momento o ganho muda e se obtem uma nova estimativa
##############################################################

#lembrando que um filtro g-h tenta estimar usando variacao do ganho e pela variacao da medicao
#com o ganho eu prevejo
#com a previsao e a medicao eu estimo
def g_h_filter(data, x0, dx, g, h, dt):
    actual_value = x0
    estimates = []

    for z in data:
        #previsao
        #atualizar o valor atual, somando ele proprio com o ganho atual
        actual_value = actual_value + dx * dt


        #atualizacao
        #
        residual = z - actual_value

        dx = dx + h * (residual/dt)
        actual_value = actual_value + g * residual
        estimates.append(actual_value)

    return np.array(estimates)

################
#teste do livro
###############

weights = [158.0, 164.2, 160.3, 159.9, 162.1, 164.6,
169.6, 167.4, 166.4, 171.0, 171.2, 172.6]
book_plots.plot_track([0, 11], [160, 172], label='Actual weight')
data = g_h_filter(data=weights, x0=160., dx=1., g=6./10, h=2./3, dt=1.)
plot_g_h_results(weights, data,0)
plt.grid(True)
plt.show()
