import numpy as np
import Sources_waves as Swav

H=3
L=120
h=50
k=2*np.pi/L
w=Swav.Wave_disp_Stokes_kin_wout(k,h)
T=2*np.pi/w
print(T)
# Test of a github commit