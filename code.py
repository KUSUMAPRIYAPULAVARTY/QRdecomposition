import numpy as np
Q=np.array([[0.316,0.949],[0.949,-0.316]])
R=np.array([[3.162,1.581],[0,1.581]])
A=Q@R
I=Q.T@Q
print('matrixA:',A)
print('QtransposeQ:',I)
