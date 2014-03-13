#!/usr/bin/python2
# -*- coding: utf-8 -*-
from PIL import Image
import random
from numpy import array
from pylab import plot, show, ones, savefig
import subprocess
import argparse

parser = argparse.ArgumentParser(description='Extract Imagedata from a cropped picture.')
parser.add_argument('-f','--file',    help='Filename', default='occu.jpeg')
parser.add_argument('-o','--out',     help='Name of the created file', default='extracted.pdf')
parser.add_argument('-x','--xrange',  help='Units in x-direction', default=60)
parser.add_argument('-y','--yrange',  help='Units in y-direction', default=22.5)
args = parser.parse_args()

theFile = args.file
xorig = float(args.xrange)
yorig = float(args.yrange)
outFile = args.out

data=[]
img = Image.open(theFile)
for i in range(img.size[0]):
    temp = []
    for j in range(img.size[1]):
        if img.getpixel((i,j))[0]<1 : temp.append(img.size[1]-j)
    if temp : data.append((i, sum(temp)/float(len(temp))))

xvals = [float(x[0])/img.size[0]*xorig for x in data]
yvals = [float(x[1])/img.size[1]*yorig for x in data]

plot(xvals,yvals)

savefig(outFile)
subprocess.call(["pdfcrop", outFile, outFile])

show()
