# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# untar.py
# Created by J. Radoux, on: december 2012
# batch unzip tar file
# ---------------------------------------------------------------------------

# Import system modules
import sys, string, os,  glob, tarfile
i = 0
gzfiles = glob.glob('RE*.tar')# loop on gz files
while gzfiles:
    i = i +1
    a = str(i)
    asc = gzfiles.pop()
    print asc
    tar = tarfile.TarFile(asc)
    tar.extractall()
    tar.close()
    os.remove(asc)
i = 0
gzfiles = glob.glob('20*.tar')# loop on gz files
while gzfiles:
    i = i +1
    a = str(i)
    asc = gzfiles.pop()
    print asc
    tar = tarfile.TarFile(asc)
    tar.extractall()
    tar.close()
    os.remove(asc)
    
    
