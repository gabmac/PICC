#importa a biblioteca numpy com o nome de np
import numpy as np

#Primeiro exemplo: parte do principio que as leituras feitas tem a mesma chance de acontecerem tanto perto
#quanto longe da realidade, isso e menos proximo da realidade

#devolve amostras distribuidas de forma uniforme com valores entre 160 e 170, 10000 amostras
measurement = np.random.uniform(160,170, size = 10000)
#media aritmetica
mean = measurement.mean()
#{:.4f} formato do float a ser printado
print('Avareage of measurement is {:.4f}'.format(mean))

#Segundo exemplo: parte do principio que a distribuicao das leituras e uma gaussiana, ou seja existirao mais
#leituras proximas do real valor, isso e mais proximo da realidade

#amostras distribuidas na forma de uma gaussina com media em 165, desvio de 5 e 10000 amostras
measurement = np.random.normal(165,5,size = 10000)

#media aritmetica
mean = measurement.mean()

print('Avareage of Measurement is {:.4f}'.format(mean))
