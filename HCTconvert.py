# helical converter development - version1.2: it is the HCT converter program
# Author: Xiaoman Duan
# Contact: xid896@usask.ca
# Create date: 2022-12-07
# Last edit date: 2023-02-07

import shutil
import os, time
from hct2ct import hct2ct
import tifffile
import argparse
parser = argparse.ArgumentParser(description='HCT2CT, for conversion from helical CT projection to CT projection for  parallel beam')
parser.add_argument('-Np', type=int, default=3000, help='number of projection per rotation (360 degrees)')
parser.add_argument('-Nr', type=int, default=3, help='number of rotations')
parser.add_argument('-linear_step', type=float, default=0.001, help='linear step (i.e., traveling distance per projectio), uint of mm')
parser.add_argument('-pixel_size', type=float, default=0.013, help='pixel size, uint of mm')
parser.add_argument('-inputpath', type=str, default='tomo/', help='input folder path: HCT projections')
parser.add_argument('-outputpath', type=str, default='tomo-converted-test/', help='output folder path: virtual CT projections')

args, unparsed = parser.parse_known_args()
if len(unparsed) > 0:
    print('Unrecognized argument(s): \n%s \nProgram exiting ... ... ' % '\n'.join(unparsed))
    exit(0)

if os.path.isdir(args.outputpath):
    shutil.rmtree(args.outputpath)
os.mkdir(args.outputpath)  # to save output

def main():

    for k1 in range(int(args.Np / 2)):
        time_git_st = time.time()
        imprefix = 'proj_'
        imzeropad = 5
        Convertedproj = hct2ct(args.Np, args.Nr, args.linear_step, args.pixel_size, args.inputpath, k1, imprefix, imzeropad)
        projname = args.outputpath + "tomo_" + str("%05d" % (k1)) + ".tif"
        tifffile.imsave(projname, Convertedproj)  # save an image from a result
        print('Elapse: %.4fs' % (time.time() - time_git_st))

    print("It's done!")


if __name__ in ['__builtin__', '__main__']:
    main()
