from pyDeltaRCM import BmiDelta
import numpy as np

if __name__ == '__main__':
    delta = BmiDelta()
    delta.initialize('deltaRCM.yaml')
    
    print 'Qw0:', delta._delta.Qw0, ' m-3/s'
    print 'Qs0:', delta._delta.Qs0, ' m-3/s'
    print 'Timestep:', delta._delta.dt, ' s'

    for time in range(0,2):
        
        delta.update()    
