import matplotlib.pyplot as plt
from scipy import signal as sign
import numpy as np
#Sen signal generator
def EntradaSin(Vmax,t,f):
  x=[]
  for i in range(len(t)):
    x.append( Vmax*np.sin(2*np.pi*f*t[i]) )
  return x

#Donde X es la entrada,t los puntos en el tiempo y Yn la salida
def SigmaDelta(X,t):
    Xd=[];
    Xp=[];
    Yn=[];
    for i in range(len(X)):
        if(i == 0):
            #Sumatoria
            Xd.append(X[i]);
            #Integracion
            Xp.append(Xd[i]);
            #Cuantizador Y D/A
        else:
            #Sumatoria
            Xd.append(X[i]-Yn[i-1]);
            #Integracion
            Xp.append(Xd[i]+Xp[i-1]);
        #Cuantizador Y D/A
        if(Xp[i] < 0):
            Yn.append(-1);
        else:
            Yn.append(+1);
    return Yn

def main():
    #Variables
    f=500;
    L=30;
    fs=f*25*L;
    T=1/f;
    t=np.arange(0,1*T+1/fs,1/fs)
    X=EntradaSin(0.8,t,f)
    #Test
    Yn=SigmaDelta(X,t)
    plt.plot(t,Yn)
    plt.plot(t,X)
    Yd=sign.decimate(Yn,L,ftype="fir")
    td=np.arange(0,1*T+L/fs,L/fs)
    plt.plot(td,Yd)
    plt.show()

if __name__ == "__main__":
    main()