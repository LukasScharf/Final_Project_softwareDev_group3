import osmnx as ox
import folium
import networkx as nx
import math
import plotFunctions as pf

# Starting coordinates by user
def starting_coord_by_user():
    """Allows user to input their own coordinates for the starting point of a route

    Returns: list
    User-defined coordinates as a list.
    """
    print("Please enter your starting coordinates here:")
    lat = float(input("Enter latitude: "))
    long = float(input("Enter longitude: "))
    coordinates = [lat,long]
    print("Your starting coordinates: " + str(coordinates))
    
    return coordinates


# Länge zwischen 2 Koordinatenpunkten berechnen
def haversine(lat1, lon1, lat2, lon2):
    # Konvertiere Grad in Radian
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    # Differenz der Längen- und Breitengrade
    dlat = lat2 - lat1
    dlon = lon2 - lon1

    # Haversine-Formel
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))

    # Erdradius in Kilometern
    radius = 6371

    # Entfernung berechnen
    distance = radius * c

    return distance

# über die gesamte Route aufsummieren
def calculate_route_length(route):
    total_distance = 0

    for i in range(len(route)-1):
        lat1, lon1 = route[i]
        lat2, lon2 = route[i+1]
        distance = haversine(lat1, lon1, lat2, lon2)
        total_distance += distance

    return total_distance

# create list of all coordinaten of all nodes, that are part of the route
def get_route_coord(route, graph_type):
    route_coordinates = []
    for node in route:
        route_coordinates.append((graph_type.nodes[node]['y'], graph_type.nodes[node]['x']))
    return(route_coordinates)

# kürzeste Route zwischen 2 Punkten berechnen
def calculate_route(map, start_coords, end_coords, graph_type):

    # get nearest start node 
    start_node = ox.distance.nearest_nodes(graph_type, start_coords[1], start_coords[0]) # (graph, lon, lat)

    # get nearest end node
    end_node = ox.distance.nearest_nodes(graph_type, end_coords[1], end_coords[0])

    # calculate shortest path between them
    route = nx.shortest_path(graph_type, start_node, end_node, weight='length')

    # add a Marker at the start_coords to the map
    pf.add_point_to_map(map=map, coord=start_coords, popup = 'This is your chosen starting point', 
                        tooltip = 'starting point', fa_icon_name='location-dot', fa_icon_color='black')

    # get a list of all the node-coordinates that are part of the route
    route_coordinates = get_route_coord(route=route, graph_type=graph_type)

    folium.PolyLine(locations=route_coordinates, color='darkblue', weight=5).add_to(map)

    # Calculate the length of the route
    length = calculate_route_length(route_coordinates)
    print("The length of your route is ", round(length, 2), "km")
    return(map)