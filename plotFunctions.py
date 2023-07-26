"""Adding point data from a dataframe as Markers to map

This script defines functions that allow the user to add many points to a map at one time.
These functions have some quite strict restrictions on the design of the dataframe you want to use.
There has to be following columns:
    - 'name'
    - 'coordinates'
    - 'sport-type'
    - 'description'
If this is given it is possible to add Markers to a map at once, where each Marker has a certain icon and colour depending on 
'sport-type'. The assingment is defined in two dictionaries that have to be updated in case there are new sport-types in the dataframe.
If there is an undefined sport-type in the dictionary there will be a default marker in red.

This script requires that `folium` be installed within the Python
environment you are running this script in.

This file can also be imported as a module and contains the following
functions:

    * add_point_to_map - adds a point with a marker to your map
    * add_all_points - adds all points of your dataframe to your map with certain Markers depending on sport-type

"""
import folium 

def add_point_to_map(map, coord, popup, tooltip, fa_icon_name='location-dot', fa_icon_color='red'):
    """ add data point to a folium map with styling options for icons and icon color
    Parameters:
    ------------------
    map: folium.folium.Map
        The map you want to add Markers to
    coord: [float, float]
        The coordiantes of the point of interest
    popup: str
        text that you want to show in the popup
    tooltip: str
        text that you want to shwo in the tooltip
    fa_icon_name: str
        must be a icon name of the icon family fa
    fa_icon_color: str
        must be an exceptable color name

    Returns:
    ---------------
    folium.folium.Map
        Map with the added Marker

    """
    m = map
    folium.Marker(coord, popup = folium.Popup(popup, min_width=300, max_width=300), 
                  tooltip = tooltip, icon = folium.Icon(color = fa_icon_color, icon = fa_icon_name, prefix = 'fa')
    ).add_to(m)

    return()


def getIcon(sport_type):
    """function that returns adequate icon for a specific sport-type
    Parameters:
    -----------------
    sport_type: str
        Enter the sport_type you want an icon for

    Returns:
    -----------------
    icon: str
    Two cases:
        1. Your sport-type is listed in the dictionary: it returns the respective icon-name
        2. Your sport-type is not listed in the dictionary: it returns 'location-dot'-icon as default
    """
    icons = {'Calisthenics': 'dumbbell',
         'Beach-Volleyball': 'volleyball',
         'Table-Tennis': 'table-tennis-paddle-ball',
         'Climbing': 'mountain'}
    try:
        icon = icons[sport_type]
    except:
        icon = 'location-dot'
    return(icon)

    
def getColor(sport_type):
    """function that returns adequate icon-color for a specific sport-type
    Parameters:
    -----------------
    sport_type: str
        Enter the sport_type you want an icon for

    Returns:
    -----------------
    icon: str
    Two cases:
        1. Your sport-type is listed in the dictionary: it returns the respective icon-color
        2. Your sport-type is not listed in the dictionary: it returns 'red' as default color
    """
    icon_colors= {'Calisthenics': 'darkred',
              'Beach-Volleyball': 'darkblue',
              'Table-Tennis': 'green',
              'Climbing': 'gray'}
    try:
        icon_color = icon_colors[sport_type]
    except:
        icon_color = 'red'
    return(icon_color)


def add_all_points(map, df):
    """fuction that adds all point data of your dataframe to the map

    Parameters:
    ---------------
    map: folium.folium.Map
        the map you want to add the points to 
    df: dataframe 
        point dataframe with columns 'name', 'coordinates', 'sport-type', 'description'

    Return:
    ---------------
    map: folium.folium.Map
        Map with all points added with different markers

    """
    for row in range(0,len(df)):
            add_point_to_map(map = map, coord = df['coordinates'][row],
                    popup = df['description'][row], tooltip = df['name'][row],
                    fa_icon_color=getColor(df['sport_type'][row]), 
                    fa_icon_name=getIcon(df['sport_type'][row]))
    return(map)















