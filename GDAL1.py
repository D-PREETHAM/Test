# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 01:07:30 2023

@author: acer
"""

import netCDF4

# Open the NetCDF file
nc_file = netCDF4.Dataset('E:\\GPM_IMERG\\Jan\\3B-DAY-L.MS.MRG.3IMERG.20210101-S000000-E235959.V06.nc4', 'r')

# Extract geotransform and projection if available in the NetCDF attributes
if 'geotransform' in nc_file.ncattrs():
    geotransform = nc_file.geotransform
else:
    geotransform = None

if 'projection' in nc_file.ncattrs():
    projection = nc_file.projection
else:
    projection = None

# Close the NetCDF file
nc_file.close()

print("Geotransform:", geotransform)
print("Projection:", projection)
