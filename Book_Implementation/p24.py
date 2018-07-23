#importa da pasta  kf_book o arquivo book_plots.py com o nome de book_plots
import kf_book.book_plots as book_plots
#importa a funcao do arquivo
from kf_book.book_plots import plot_errorbars
#plot_errorbars([(ponto, variacao_envolta_ponto,nome),...n valores], xlims = [x,x+y] tamanho de x)
plot_errorbars([(160, 8, 'A'), (170, 8, 'B')], xlims=(150, 180))
