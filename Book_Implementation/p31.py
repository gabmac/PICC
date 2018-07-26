#a previsao e que o inidividuo ganhe 1 lb por dia, quanto ele realmente ganha?
#fator de escala de 4/10 para relacionar a previsao com a medicao

#importa uma funcao especifica
from kf_book.book_plots import figsize
#importa a biblioteca com o nome de plt
import matplotlib.pyplot as plt
from kf_book.gh_internal import plot_hypothesis1
import kf_book.gh_internal as gh

#pesos medidos
weights = [158.0, 164.2, 160.3, 159.9, 162.1, 164.6,
169.6, 167.4, 166.4, 171.0, 171.2, 172.6]

time_step = 1.0 # day
scale_factor = 4.0/10

#define uma funcao
def predict_using_gain_guess(weight, gain_rate, do_print=False):
    #armazena valores filtrados
    estimates, predictions = [weight],[]

    #percorre o vetor weights, e z assume o valor atual
    for z in weights:

        #fazendo a predicao
        prediction = weight + gain_rate * time_step

        #atualizando o filtro, estimativa do novo peso
        weight = prediction + scale_factor * (z - prediction)

        #salvando valores

        #adiciona valor(no caso, weight) ao final da lista(no caso estimates)
        estimates.append(weight)
        predictions.append(prediction)

        if do_print:
            gh.print_results(estimates,prediction,weight)

    return estimates, predictions


initial_guess = 160

estimates,predictions = predict_using_gain_guess(weight = initial_guess, gain_rate = 1, do_print = True)
#transforma em um grafico a medicao, as previsoes e as estimativas
gh.plot_gh_results(weights, estimates, predictions,0)# o 0 esta faltando no livro o que faz código nao funcionar
#codigo que indica que e para mostra os graficos
plt.show()#falta em todos os plots para que o código funcione.
