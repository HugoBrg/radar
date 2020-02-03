import numpy as np
import scipy as sp
import pylab as pl
import scipy.io as sio

data1_A = sio.loadmat('mesures_1.mat')
data1_B = data1_A['data'][0]

data2_A = sio.loadmat('mesures_2.mat')
data2_B = data2_A['data'][0]

data3_A = sio.loadmat('mesures_3.mat')
data3_B = data3_A['data'][0]

#data = data3_B - data2_B                #Choix du fichier, ici soustraction afin de voir le pic de l'objet
data = data3_B
data_size = np.size(data)               #Taille de notre mesure

fe = 6.25e6                             #Constantes, fréquence du radar
pente = 9762688661925.5703              #rad/s ???
c = 299792458                           #Vitesse de la lumière

FFT = np.fft.fft(data)                  #Transformation de Fourrier rapide

fif =fe*np.linspace(0, 1, data_size/2)  #Suppresion du duplicat
dist = (c/(2*pente))*fif                #Calcul de l'abscisses

FFT_abs = np.abs(FFT)                   #Calcul de la transformation de Fourrier
FFT_abs2 = FFT_abs[0:data_size/2]       #Division par 2 pour supprimer le duplicat

pl.plot(dist,FFT_abs2)                  #Tracage du graphique
pl.title('mesures 3')
#pl.xlabel('abscisses')
#pl.ylabel('ordonnee')
pl.show()                               #Affichage du graphique

