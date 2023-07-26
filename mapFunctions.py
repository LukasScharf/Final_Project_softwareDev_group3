"""Creating a Map with certain properties

This script allows you to calculate the center (mean) coordinates of many different point data coodinates.
These coordinates then can be used to create a map.

This script requires that `folium` and 'numpy' be installed within the Python
environment you are running this script in.

This file can also be imported as a module and contains the following
functions:

    * getCenterCoordinates - returns the mean coordinates all your point data
    * createMap - return a map with a certain zoom-level, control-scale and layer-control of two different tiles (OSM and ESRI Imagery)
    
"""


import folium as fl
import numpy as np


def getCenterCoordinates(col_coord):
    """calculates mean of coordinates of point data

    Parameters:
    -----------
    col_coord: [float, float]
        Column of your dataframe that describes the coordinates of the points

    Return:
    ----------
    list ([float, float])
        center (mean) coordinates

    """
    lat = []
    long = []
    for i in range(0, len(col_coord)):
        lat.append(col_coord[i][0])
        long.append(col_coord[i][1])
    center_coord = [np.average(lat), np.average(long)]

    return(center_coord)


def create_Map(coordinates, zoom_start, control_scale = True):
    """create a basemap with layer control of two different tiles (OSM and ESRI imagery)

    Parameters: 
    -------------
    coordinates: list ([float, float])
        coordinates of the center your map should have
    zoom_start: int
        defines at which level the zoom starts 
    
    Returns: folium.folium.Map
        Map with 2 tiles, control_scale and layer control
    """
    m = fl.Map(location = coordinates, zoom_start = zoom_start, control_scale = True)
    tile = fl.TileLayer(tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
                            attr='Esri', name = 'Esri Satellite',
                            overlay = False, control = True
    ).add_to(m)
    fl.LayerControl().add_to(m)

    return(m)










