import numpy as np

def number_1(temps_F):
    temps_C=[]
    for num in temps_F:
        F=num
        #(F-32)*5/9
        C=(F-32)*5/9
        temps_C.append('{:0.2f}'.format(C))
    return temps_C

temps_F = np.array([0, 100, 99.1, 32, 44, 241, 10, 15, 20])

print(', '.join(number_1(temps_F)))
