#####################################################
#O objetivo e descobrir a posição do trem no trilho
#####################################################


from numpy.random import randn
#import g_h_filter as filter
from g_h_filter import g_h_filter as filter
import matplotlib.pylab as pylab
import matplotlib.pyplot as plt
import kf_book.book_plots as book_plots
from kf_book.gh_internal import plot_g_h_results
import numpy as np

def compute_new_position(pos,vel,dt = 1):
    return pos + (vel * dt)


#o erro é de 500 metros
def measure_position(pos):
    return pos + (randn()*500)


#count =  tempo nesse caso
def get_train_data(pos, vel, count):
    zs = []
    for i in range(count):
        pos = compute_new_position(pos = pos, vel = vel)
        zs.append(measure_position(pos))

    return np.asarray(zs)

#caso o trem tenha aceleração
def gen_train_data_with_acc(pos, vel, count,accel):
    zs = []
    for t in range(count):
        pos = compute_new_position(pos, vel)
        vel += accel #aceleração
        zs.append(measure_position(pos))

    return np.asarray(zs)



pos,vel = 23*1000, 15
count = 100
accel = 0.2
#zs = get_train_data(pos = pos, vel = vel, count = count)
#zs = gen_train_data_with_acc(pos = pos, vel = vel, count count,accel = accel)

#olhando para a resposta vemos que a medição não é muito precisa portanto podemos
#escolher g pequeno para que ela nao tenho tanto peso no filtro
#sabe-se que um trem não pode acelerar nem desacelerar muito rápido
#o que nos permite a escolha de um h também razoavelmente pequeno

data = filter(data=zs, x0=pos, dx=15., dt=1., g= , h= )

plt.plot(zs / 1000.) # convert to km
book_plots.set_labels('Train Position', 'time(sec)', 'km')
plt.grid()
plt.show()
