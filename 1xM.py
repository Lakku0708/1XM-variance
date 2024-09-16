import numpy as np
M = 8
vec1 = np.random.rand(1, M)
vec2 = np.random.rand(1, M)
# Compute the covariance between the two vectors
covar_matrix = np.cov(vec1, vec2)
# Since we're interested in the covariance between the two vectors, we look at the off-diagonal element
covar = covar_matrix[0, 1]
# Output
print("Vector 1:", vec1)
print("Vector 2:", vec2)
print("Covariance of Vector 1 and Vector 2 is:", covar)
