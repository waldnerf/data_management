# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# untar.py
# Created by J. Radoux, on: december 2012
# Modified by R. d'Andrimont on: 15 may 2013
# batch unzip tar file
# ---------------------------------------------------------------------------

# Import system modules
import os,  glob, tarfile, platform
from osgeo import gdal

##INPUT VAR##
dir_to_untar='GIOGL-ValdaitationWB' #subfolder of this dir will be untar
dir_untared='untared_all' #dir to store results (will be created if not exists)
##
if platform.system()=='Linux':
    directory_rapideye='/export/lw01/rapideye'
elif platform.system()=='Windows':
    directory_rapideye='\\\\eligeo01.enge.ucl.ac.be\\lw01\\rapideye\\'   
##

## 1 BuildVRT ##

# list the files and save as text file
file_to_vrt=glob.glob(os.path.normpath(os.path.join(directory_rapideye,dir_untared,'*','???????_2013-??-??_???_3A_??????.tif')))

if platform.system()=='Linux':
    f = open(os.path.normpath(os.path.join(directory_rapideye,dir_untared,"file_list_linux.txt")), "w")
    for i in file_to_vrt:
        f.write("%s\r\n" % i)    
    f.close()
elif platform.system()=='Windows':
    f = open(os.path.normpath(os.path.join(directory_rapideye,dir_untared,"file_list_windows.txt")), "w")
    for i in file_to_vrt:
        f.write("%s\n" % i)    
    f.close()
# save as text

gdalbuildvrt -allow_projection_difference -input_file_list file_list_linux.txt  test_index1.vrt
gdalbuildvrt -allow_projection_difference -b 1 2 3 -input_file_list file_list_linux.txt  test_index_rgb.vrt

gdalwarp -of VRT -t_srs EPSG:4326 test_index1.vrt superdataset.vrt

gdal2tiles.py -p geodetic -k superdataset.vrt



os.system(gdalbuildvrt test.vrt untared_all)



## 2 Gdal2Tiles ##
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
    
    
