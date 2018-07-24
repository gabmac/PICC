#diferente do exemplo anterior ao inves de tentar advinhar o novo peso, tenta-se advinhar a nova variacao de peso

from kf_book.book_plots import figsize
#importa a biblioteca com o nome de plt
import matplotlib.pyplot as plt
from kf_book.gh_internal import plot_hypothesis1
import kf_book.gh_internal as gh

#pesos medidos
weights = [158.0, 164.2, 160.3, 159.9, 162.1, 164.6,
169.6, 167.4, 166.4, 171.0, 171.2, 172.6]


weight = 160. # initial guess
gain_rate = -1.0 # initial guess (nesse caso imagina-se perda de peso)
time_step = 1.
weight_scale = 4./10
gain_scale = 1./3
estimates = [weight]
predictions = []

for z in weights:
# prediction step
    weight = weight + gain_rate*time_step
    gain_rate = gain_rate
    predictions.append(weight)
    # update step
    residual = z - weight
    gain_rate = gain_rate + gain_scale * (residual/time_step)
    weight = weight + weight_scale * residual
    estimates.append(weight)

gh.plot_gh_results(weights, estimates, predictions)
plt.grid(True)
plt.show()
