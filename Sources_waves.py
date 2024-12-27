## Dispersion relation solving
def Wave_disp_Stokes_kin_wout(k,h,g=9.81):
    import numpy as np
    w2=g*k*np.tanh(k*h)
    w=np.sqrt(w2)

    return w



### Creation of Jonswap spectrum components using Stokes stheory





### Testing Nest

