# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# untar.py
# Created by J. Radoux, on: december 2012
# Modified by R. d'Andrimont on: 15 may 2013
# batch unzip tar file
# ---------------------------------------------------------------------------

# Import system modules
import os,  glob, tarfile, platform
##INPUT VAR##
dir_to_untar='GIOGL-ValdaitationWB' #subfolder of this dir will be untar
dir_untared='untared_all' #dir to store results (will be created if not exists)
##
if platform.system()=='Linux':
    directory_rapideye='/export/lw01/rapideye'
elif platform.system()=='Windows':
    directory_rapideye='\\\\eligeo01.enge.ucl.ac.be\\lw01\\rapideye\\'   
##
directory=os.path.normpath(os.path.join(directory_rapideye,dir_to_untar))

if os.path.isdir(os.path.normpath(os.path.join(directory_rapideye,dir_untared)))==0:
    os.mkdir(os.path.normpath(os.path.join(directory_rapideye,dir_untared)))

gzfiles = glob.glob(os.path.normpath(os.path.join(directory_rapideye,dir_to_untar,'*','RE*.tar')))# loop on gz files

while gzfiles:
    asc = gzfiles.pop()
    print asc
    #create a dir per tar
    dir_to_save=os.path.join(directory_rapideye,dir_untared,os.path.split(os.path.split(asc)[1])[1][:-8]+'_'+os.path.split(os.path.dirname(asc))[1])
    if os.path.isdir(dir_to_save)==0:    
        os.mkdir(dir_to_save)
    tar = tarfile.TarFile(asc)
    tar.extractall(dir_to_save)
    tar.close()

gzfiles = glob.glob(os.path.normpath(os.path.join(directory_rapideye,dir_untared,'*','*.tar')))# loop on gz files
while gzfiles:
    asc = gzfiles.pop()
    print asc
    tar = tarfile.TarFile(asc)
    tar.extractall(os.path.dirname(asc))
    tar.close()
    os.remove(asc)
    
    
