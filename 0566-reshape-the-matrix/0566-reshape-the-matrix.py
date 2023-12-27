import numpy as np
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = np.shape(mat)
        if m * n != r * c:
            print("Reshape operation not possible.")
            return mat
        reshaped_mat = np.reshape(mat, (r, c))
        return reshaped_mat