import numpy as np

a = np.array([1, 2, 3, 4])
print(np.where(a > 3))
print(len(np.where(a > 3)))
# Output:
#   (array([2, 3], dtype=int64),)
#   1

import numpy as np

a = np.array([1, 2, 3, 4])
print(np.where(a > 2)[0])
print(len(np.where(a > 2)[0]))
# Output:
#   [2 3]
#   2
# this is due to the fact that np.where returns a tuple of arrays, one for each dimension of a.
