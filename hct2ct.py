# helical converter function
# Author: Xiaoman Duan
# Contact: xid896@usask.ca
# Date: 2022-12-07
# Latest revised  date: 2023-01-18

import numpy as np
import tifffile


def hct2ct(Np, Nr, linear_step, pixel_size, path, mispixels, k1):
    print("Generating virtual projection of --->",k1)
    ## k1 --> k
    k = np.zeros(Nr * 2, dtype = np.int16)
    for i in range (Nr * 2):
        k[i] = k1 + i * Np / 2
    ## Read HCT projections
    Usedproj =  []
    for i in range (Nr*2):
        Rawproj = tifffile.Tifffile (os.path. join(path, imprefix+ str(k[i]).zfill(imzeropad)+".tif")).asarray()
        Rawproj = np.flipud(Rawproj)
        Usedproj.append (Rawproj)

    Usedproj = np.array(Usedproj)
    D_travel = np.floor(k * linear_step / pixel_size) ## unit of pixels
    w = k * linear_step / pixel_size - D_travel
    Rows_virtual = int(np.floor(Np * Nr * linear_step / pixel_size + np.shape(Rawproj)[0])) ## unit of pixels
    I_virtal = Usedproj.min() * np.ones([Rows_virtual, np.shape(Rawproj)[1]])

    for kk in range (np.shape(k)[0]):
        for i in range (np.shape(Rawproj)[0]-1):
            i1 = int(i + D_travel[kk])
            if np.mod(np.floor((k[kk]) / (Np / 2)), 2) == 0:
               I_virtal[i1][:] = w[kk] * Usedproj[kk,i,:] + (1 - w[kk]) * Usedproj[kk,i + 1,:]
            else:
                for j in range(np.shape(Rawproj)[1]):
                    j1 = np.shape(Rawproj)[1] - 1 - j
                    if ((j1 + mispixels) >= 0) & ((j1 + mispixels) < np.shape(Rawproj)[1]):
                        I_virtal[i1][j1 + mispixels] = w[kk] * Usedproj[kk,i, j] + (1 - w[kk]) * Usedproj[kk,i + 1, j]

    I_virtal = np.flipud(I_virtal.astype(np.uint16))

    return I_virtal
