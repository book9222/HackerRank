import numpy as np

n, m = input().split()
# print(n,m)

mat = []
for i in range(int(n)):
    # mat.append(input().split())
    mat.append([int(i) for i in input().split()])
    
np_array = np.array(mat)
# print(np_array)
print(np.mean(np_array, axis = 1))
print(np.var(np_array, axis = 0))
print(round(np.std(np_array),11))
# axis=1 is row-wise operation 
# axis=0 is column-wise operation