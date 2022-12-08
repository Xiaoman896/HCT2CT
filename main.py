# helical converter development - version1.1: it is the HCT converter program
# Author: Xiaoman Duan
# Contact: xid896@usask.ca
# Date: 2022-12-07

import shutil
import os, time
from hct2ct import hct2ct
import tifffile

def main():
    Np = 3000
    Nr = 3
    linear_step = 0.001
    pixel_size = 0.013
    inputpath ='tomo/'
    outputpath = 'tomo-converted/'
    if os.path.isdir(outputpath):
        shutil.rmtree(outputpath)
    os.mkdir(outputpath) # to save temp output

    mispixels = 18 # allow to maunally correct the mispixels horizontally
    corrpixelsv = 20 # corret the error of white line; if there are missing lines appear, change the number bigger

    for k1 in range(int(Np/2)):
        time_git_st = time.time()
        Convertedproj = hct2ct(Np, Nr, linear_step, pixel_size, inputpath, mispixels, k1, corrpixelsv)
        projname = outputpath + "tomo_" + str("%05d" % (k1)) + ".tif"
        tifffile.imsave(projname, Convertedproj)  # save a image from a result
        print('Elapse: %.4fs' % (time.time() - time_git_st))

    print("It's done!")

if __name__ in ['__builtin__', '__main__']:
    main()