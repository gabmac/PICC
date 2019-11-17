import subprocess
import sys


#instala as libs
def install(packages=['numpy','matplotlib','scipy','control','pandas']):
    for package in packages:
        subprocess.call([sys.executable, "-m", "pip", "install", package])
        

install()

import numpy as np
from numpy.linalg import inv
from matplotlib.pyplot import *
from scipy.signal import lfilter
from control import StateSpace
import pandas as pd
import time
        
#tensao = [10,12,14,16]
tensao = [16]


for V in tensao:
    #variaveis encontradas por meio dos experimentos
    b = 6.465e-4
    J = 2.2e-3
    K=3.12e-2
    L=3.72e-2
    R=5.9084
    
    Tc = 0.0021
    
    dt = 0.01#tempo de discretizacao para o motor real
    
    #Velocidade Real
    df = pd.read_csv(str(V)+'V.csv',sep=';')
    
    
    
    #modelo do sistema
    A = np.array([[-R/L,-K/L],[K/J,-b/J]])
    B = np.array([[1/L , 0],[0 ,-1/J]])
    C = np.array([0,1])
    D = np.array([0,0])
    
    sys = StateSpace(A,B,C,D)
    
    #discretizando o modelo
    dsys = sys.sample(dt)
    
    #Setando os dados que serao usados
    Samples = len(df)
    tempo = np.arange(0,(Samples)*dt,dt)
    
    medida = []
    #converte Dataframe para um lista de matrizes
    for i in range(0,Samples):
        medida.append(np.array([[df.iloc[i]['Corrente']],[df.iloc[i]['Velocidade']]]))
    
    P = np.array([[1,0],[0,1]])
    
    
    #Sendo Q a covariancia do ruido do preocesso. O que representa a incerteza do modelo
    Q = np.array([[1, 0],[0,1]])
    
    
    #Sendo R ruido na medicao
    R =  np.array([[5,0],[0,5]])
    
    
    #Imagina-se os estados iniciais como 0
    
    Xk_prev = np.array([[0],[0]])
    
    
    #inicializando o estado atual
    
    
    #Entradas do Sistema
    u = np.array([[V],[Tc]])
    
    
    
    
    #matriz com o os valores medidos
    H = np.array([[1, 0],[0,1]])
    F = dsys.A
    prev = []
    filtro = []
    for i in range(0,Samples):
        
        #Predict
        Xk_prev = F@Xk_prev + dsys.B@u
        prev.append(Xk_prev)
        P = F @ P @ F.transpose() + Q
        
        
        #Update
        y = medida[i]-H @Xk_prev
        S = H @ P @ H.transpose() + R
        K = P @ H.transpose() @ inv(S)
        
        P = P - K @ H @ P
        
        Xk_prev = Xk_prev + K @ y
        filtro.append(Xk_prev)
       
        
    corFiltro = []
    velFiltro = []
    
    corPrev = []
    velPrev = []
    
    corMedida = []
    velMedida = []
        
    for i  in range(0,len(tempo)):
        corFiltro.append(float(filtro[i][0]))
        velFiltro.append(float(filtro[i][1]))
        
        corPrev.append(float(prev[i][0]))
        velPrev.append(float(prev[i][1]))
        
        corMedida.append(float(medida[i][0]))
        velMedida.append(float(medida[i][1]))
    
    
    
    figure()
    plot(tempo,velMedida,tempo,velFiltro,tempo,velPrev)
    title('Comparação entre os valores da velocidade Angular Medida, obtido pelo Filtro de Kalman e Modelada para {}V'.format(V))
    ylabel('Velocidade (rad/s)')
    xlabel('Tempo (s)')
    legend(['Velocidade Medida','Velocidade Kalman','Velocidade Modelada'])
    mng = get_current_fig_manager()
    savefig(str(V)+'VVelocidade.png',orientation='landscape')
    
    
    figure()
    plot(tempo,corMedida,tempo,corFiltro,tempo,corPrev)
    title('Comparação entre os valores da Corrente Medida, obtido pelo Filtro de Kalman e Modelada para {}V'.format(V))
    ylabel('Velocidade (rad/s)')
    xlabel('Tempo (s)')
    legend(['Corrente Medida','Corrente Kalman','Corrente Modelada'])
    mng = get_current_fig_manager()
    savefig(str(V)+'VCorrente.png',orientation='landscape')
