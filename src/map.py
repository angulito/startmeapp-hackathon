import osmnx as ox, geopandas as gpd, networkx as nx

# Legazpi 40.3911, -3.6948
# Atocha 40.4068, -3.6884

def get_surroundings_map(origin_lat, origin_long, dst_lat, dst_long):
	north = max(origin_lat, dst_lat) + 0.01
	south = min(origin_lat, dst_lat) - 0.01
	west = min(origin_long, dst_long) - 0.01
	east = max(origin_long, dst_long) + 0.01

	return ox.graph_from_bbox(north, south, east, west, network_type='bike')

"""
def get_surroundings_map(origin_lat, origin_long, dst_lat, dst_long):
	return ox.load_graphml('legazpiAtocha.graphml')
"""

def get_route(G, origin_lat, origin_long, dst_lat, dst_long):
	origin_node = ox.get_nearest_node(G, (origin_lat, origin_long))
	dst_node = ox.get_nearest_node(G, (dst_lat, dst_long))

	route = nx.shortest_path(G, origin_node, dst_node)

	return route

def calculate_route(origin_lat, origin_long, dst_lat, dst_long):
	G = get_surroundings_map(origin_lat, origin_long, dst_lat, dst_long)
	route = get_route(G, origin_lat, origin_long, dst_lat, dst_long)

	route_nodes = []

	for i in range(1, len(route)):
		node = G.node[route[i]]
		route_nodes.append((node['x'], node['y']))

	route_edges = []

	for i in range(1, len(route) - 1):
		edge = G[route[i]][route[i+1]][0]
		edge_name =  edge.get('name') 
		if edge_name is None:
			edge_name = 'Calle sin nombre'
			print(edge)
		edge_distance = edge['length']
		route_edges.append((edge_name, edge_distance))

	return { 'nodes' : route_nodes, 'edges' : route_edges }

def get_coordinates_from_address(name):
	G = ox.graph_from_address(name, distance=50)

	anynode = G.node[list(G.nodes)[0]]

	return (anynode['x'], anynode['y'])
