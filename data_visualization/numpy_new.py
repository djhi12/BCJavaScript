import numpy as np

a = np.arange(6)

a2 = a[np.newaxis, :]

print(a2.shape)
