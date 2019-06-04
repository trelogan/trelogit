#!/bin/bash
for f in *.tif
do
	gdal_translate -co compress=LZW $f $f_c.tif
done