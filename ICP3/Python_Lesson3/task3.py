import numpy as np


# create random vector of size 15 having only Integers in the range 1-20.

sampl = np.random.randint(20, size=15)
print(sampl)

# reshape the array to 3 by 5
b = sampl.reshape((3,5))
print(b)


# replace the max in each row by 0
row_maxes = b.max(axis=1).reshape(-1, 1)
print(row_maxes)
np.where(b == row_maxes, 1, 0)
b[:] = np.where(b == row_maxes, 0, b)
print(b)

# np.where(b == row_maxes).astype(int)
# print(b)


