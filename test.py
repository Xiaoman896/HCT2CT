# helical converter development - version1.1: it is the HCT check program
# Author: Xiaoman Duan
# Contact: xid896@usask.ca
# Date: 2022-12-07

import shutil
import os, time
from hct2ct import hct2ct
import tifffile

def main():
    Np = 3000 ## number of projection per rotation (360 degrees)
    Nr = 3 ## number of rotation
    linear_step = 0.001 ## linear step, uint of mm
    pixel_size = 0.013 ## linear step, uint of mm
    inputpath ='tomo/'
    outputpath = 'tomo-converted/'
    if os.path.isdir(outputpath):
        shutil.rmtree(outputpath)
    os.mkdir(outputpath) # to save output

    mispixels = 18 # allow to maunally correct the mispixels horizontally, uint of pixel
    corrpixelsv = 20 # corret the white line (due to white edge of HCT projection); if there are white lines present, change the number bigger or smaller, uint of pixel
    k1 = 10 # test projection index of virtual CT

    time_git_st = time.time()
    Convertedproj = hct2ct(Np, Nr, linear_step, pixel_size, inputpath, mispixels, k1, corrpixelsv)
    projname = outputpath + "tomo_" + str("%05d" % (k1)) + ".tif"
    tifffile.imsave(projname, Convertedproj)  # save a image from a result

    print('Elapse: %.4fs' % (time.time() - time_git_st))
    print("It's done!")

if __name__ in ['__builtin__', '__main__']:
    main()
