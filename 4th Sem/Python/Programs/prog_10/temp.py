import numpy as np

arr = np.array([[-0.30565392, -0.96605562],
                [ 0.85331367, -2.62963495],
                [ 0.87839643, -0.28283675],
                [ 0.72676698,  0.93213482],
                [-0.52007354,  0.27752806],
                [-0.08701666,  0.22764316],
                [-1.78897817,  0.50737573],
                [ 0.62260038, -1.96012161],
                [-1.98231706,  0.36523876],
                [-1.07587382, -2.3022289 ]])
l = arr[arr[:, 1].argsort()]
print(l)