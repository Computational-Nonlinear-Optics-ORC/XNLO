import struct
import numpy as np
from matplotlib import pyplot as plt

# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Wed Feb  1 14:50:42 2017

@author: sms1n16
"""

N_row_ = 621
N_col_ = 20

fileName = "./output/A_w_R.bin"
f = open(fileName, mode='rb')
content = f.read(8*N_row_*N_col_)

data = struct.unpack("d"*(len(content) // (8)), content)
# N = np.fromfile(fileName, dtype=np.float64)

A_w_R = np.zeros([N_col_, N_row_])
for i in range(N_col_):
    A_w_R[i, :] = data[i*N_row_:i*N_row_+N_row_]

plt.figure()
plt.plot(A_w_R.T)
plt.show()


fileName = "./output/A_w_I.bin"
f = open(fileName, mode='rb')
content = f.read(8*N_row_*N_col_)

data = struct.unpack("d"*(len(content) // (8)), content)
# N = np.fromfile(fileName, dtype=np.float64)

A_w_I = np.zeros([N_col_, N_row_])
for i in range(N_col_):
    A_w_I[i, :] = data[i*N_row_:i*N_row_+N_row_]

plt.figure()
plt.plot(A_w_I.T)
plt.show()


fileName = "./output/w_active.bin"
f = open(fileName, mode='rb')
content = f.read(8*N_row_*1)

data = struct.unpack("d"*(len(content) // (8)), content)
# N = np.fromfile(fileName, dtype=np.float64)

w_active = np.zeros([1, N_row_])
w_active[0, :] = data[0:N_row_]

plt.figure()
plt.plot(w_active[0])
plt.show()
