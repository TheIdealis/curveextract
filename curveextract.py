#!/usr/bin/python2
# -*- coding: utf-8 -*-
from PIL import Image
import random
from numpy import array, linspace, log, exp, savetxt, column_stack
from pylab import plot, show, ones, savefig,semilogy
import subprocess
import argparse
import re

parser = argparse.ArgumentParser(description='Extract Imagedata from a cropped picture.')
parser.add_argument('-f','--file',    help='Filename', default='occu.jpeg')
parser.add_argument('-l','--log',     help='Filename', default=False)
parser.add_argument('-o','--out',     help='Name of the created file', default='extracted')
parser.add_argument('-x','--xrange',  help='Units in x-direction', default='0 60')
parser.add_argument('-y','--yrange',  help='Units in y-direction', default='0 22.5')
args = parser.parse_args()

theFile = args.file

xorig = tuple(float(x) for x in re.findall('[-+]?\d*\.\d+|\d+', args.xrange))
yorig = tuple(float(x) for x in re.findall('[-+]?\d*\.\d+|\d+', args.yrange))

logscale = args.log
outFile = args.out

data=[]
img = Image.open(theFile)
for i in range(img.size[0]):
    temp = []
    for j in range(img.size[1]):
        if img.getpixel((i,j))[0]<1 : temp.append(img.size[1]-j)
    if temp : data.append((i, sum(temp)/float(len(temp))))
data = array(data)

if logscale:
    xvals = array([float(x[0])/img.size[0]*(xorig[1]-xorig[0])+xorig[0] for x in data])
    ylog = array([exp(x) for x in linspace(log(yorig[0]),log(yorig[1]),img.size[1])])
    yvals= ylog[data[:,1].astype('int')] 
    semilogy(xvals,yvals)
else:
    xvals = array([float(x[0])/img.size[0]*(xorig[1]-xorig[0])+xorig[0] for x in data])
    yvals = array([float(x[1])/img.size[1]*(yorig[1]-yorig[0])+yorig[0] for x in data])
    plot(xvals,yvals)


savetxt(outFile, column_stack([
    xvals.view(float).reshape(-1),
    yvals.view(float).reshape(-1),
]))

show()
