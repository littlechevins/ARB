
# # TODO:
# Make non blocking requests
# https://stackoverflow.com/questions/27021440/python-requests-dont-wait-for-request-to-finish



# Fix bug of null dht keys
# Start building the LSA - linked state advertisement - ROUTING ALGO!! :)

# Steps
# Create backbone
# Assign each backbone node a range of keys
	# Go to a random node and assign a key range based on closest node id
	# Broadcast this to other nodes (global dht)
	# Must go to next node to repeat
# Create node map

# Bugs:
# Proper reporting
# No link is considered to have been correctly reported unless the two ends agree; i.e., if one node reports that it is connected to another, but the other node does not report that it is connected to the first, there is a problem, and the link is not included on the map.



'''
Let backbone nodes be bnodes
'''

import os
import hashlib
import random
import string
import base64
from dhtEngine import DHT
import re

import math

class Node:


	# Node types
	# backbone - DR node, broadcasters
	# normal

	def __init__(self, node_name, type):
		# self.id = self.get_id()
		self.ids = []
		self.node_name = node_name
		self.neighbours = []
		self.type = type
		self.seqn = 0 				# sequence number for lsa
		self.lsdb = {}

		self.end_nodes = {}

		self.backbone_nodes = []
		self.associated_bnode = None	# String name of bnode, only applies for normal node

		self.dhtEngine = DHT()



import json
from flask import jsonify
from flask import Flask
from flask import request
import time
import requests
import argparse
app = Flask(__name__)


parser = argparse.ArgumentParser()
parser.add_argument("-t", "--type", help="The type of node to spawn")
parser.add_argument("-n", "--name", help="The name of node to spawn")
parser.add_argument("-id", "--id", help="The id of node to spawn")
parser.add_argument("-ip", "--ip", help="The ip of node to spawn")
args = parser.parse_args()

if args.type is None:
	node = Node(args.name, "backbone")
else:
	node = Node(args.name, args.type)



def get_random():
	# random_data = os.urandom(128)
	# return hashlib.md5(random_data).hexdigest()[:8]
	x = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(8))
	return x

def get_key_from_id(id):
	# print("TYPE!!!")
	# print(type(id))
	rb = id[0]

	if rb.isdigit():
		return '0-9'
	elif ord(rb) in range(ord('a'), ord('f')+1):
		return 'a-f'
	elif ord(rb) in range(ord('g'), ord('l')+1):
		return 'g-l'
	elif ord(rb) in range(ord('m'), ord('z')+1):
		return 'm-z'
	else:
		print('bad key from id: {}'.format(rb))
		return 'BAD'



# def add_to_dht(self, node_id):
#
#
# 	# add the key/node just to the first matching key, then rebalance dht
# 	key = self.dhtEngine.get_key_from_node_id(node_id)
#
# 	return key

def keygen():
	hasher = hashlib.md5(get_random())
	h1 = base64.urlsafe_b64encode(hasher.digest())
	h1 = re.sub('[!@#$=-_-\\xe2]', '', h1)
	h1 = h1[:10]
	return h1


# def manual_assign(self):
# 	# key_ranges = ['0-9', 'a-f', 'g-l', 'm-z']
# 	random_assign = random.randint(0,3)
#
# 	if random_assign == 0:
# 		id = str(get_id())
# 		if id.index(0)

@app.route("/setup")
def setup():


	with open('tables/node_info.json') as node_info:
		node_info_json = json.load(node_info)
		node.type = node_info_json[node.node_name]["node_type"]
		# node.ids = node_info_json[node.node_name]["node_ids"]

		print("Setup phase, node type: {}".format(node.type))

		if(node.type == 'end'):
			# Let node have a random amount of pk's, or take from file?
			num_pk = random.randrange(1,3)

			for x in range(0, num_pk):
				key = keygen()
				print("generated key: {}".format(key))
				node.ids.append(key)

			# node.id = node_info_json[node.node_name]["node_ids"][0]
		elif(node.type == 'backbone'):
			# node.id = None
			pass
		else:
			print("ERROR, no type found")
			return ""

	return "Setup!"


@app.route("/")
def backbone():
	# create the backbone nodes

	# gets all neighbours, reads from table
	with open('tables/backboneAndNormal.json') as json_file_backbone:
		backbone_data = json.load(json_file_backbone)
		# return jsonify(backbone_data)

	if node.node_name in backbone_data:
		neighbours_list = backbone_data[node.node_name]
		# return jsonify(neighbours_list)
	else:
		return "No"
	# 	return "yes"


	# payload types:
	# IRQN - initial request neighbour - sends self id to neighbours
	# IRQNR - initial request neighbour reply - sends self id and known neighbours - R1 becomes 2way
	# CRQNR - confirm request neighbour reply - sends self id and known neighbours - R2 becomes 2way

	# LSA - linked state adver

	# send hello signal to neighbour to establish 2-way connection
	current_neighbours = []

	# if node.id is None:
		# generate id for self, send along
		# node.id = get_id()
		# node.id = get_random()
		# node.dht[get_key_from_id(node.id)] = node.id

	for neighbour in neighbours_list:
		payload = create_payload(node.ids, node.node_name, current_neighbours, "IRQ", node.dhtEngine.dht, node.type)
		ip = get_ip(neighbour)
		send(payload, ip)
	print("STOP")
	return "DONE"

@app.route('/receive', methods=['POST'])
def receive():


	data = request.get_json()
	print("yeeeee: {}".format(json.dumps(data)))

	node_name_from = data['node_name']
	node_id_from = data['node_ids']
	node_name_from_arr = [node_name_from]

	if 'dht' in data:
		node_dht_from = data['dht']
		# combine received dht with known
		node.dhtEngine.dht = merge_two_dicts(node_dht_from, node.dhtEngine.dht)

	if 'node_type' in data:
		print("found node_type in data, is {}".format(data['node_type']))
		received_node_type = data['node_type']

	# add received id to dht (only add when neighbourship is established)
	# node.dhtEngine.dht[node_name_from] = get_key_from_id(node_name_from)

	if received_node_type == 'backbone':
		node.backbone_nodes.append(node_name_from)
		node.dhtEngine.num_nodes += 1

	# # generate own id (check if backbone phase)
	# if node.id is None:
	# 	# get all keys in list, compare
	# 	# can infinite loop
	# 	guard = 10000
	# 	while True:
	# 		new_id = get_id()
	# 		new_key = get_key_from_id(new_id)
	# 		guard =- 1
	# 		if guard <= 0:
	# 			print("Cant generate unique id")
	# 			break
	# 		if new_key not in node_dht_from:
	# 			node.id = new_id
	# 			node.dhtEngine.dht[get_key_from_id(node.id)] = node.id
	# 			break

	if 'type' in data:
		payload_type = data['type']

		if payload_type == 'IRQ':
			print("Received payload IRQ")
			# reply with IRQNR
			payload = create_payload(node.ids, node.node_name, node_name_from_arr, "IRQNR", node.dhtEngine.dht, node.type)
			ip = get_ip(node_name_from)
			send(payload, ip)
		if payload_type == 'IRQNR':
			print("Received payload IRQNR")

			# check if sender is end node
			if received_node_type and received_node_type == 'end':
				print("RECEVIED MESSAGE FROM END NODE {}".format(node_name_from))
				# check if doesnt already exist
				if node_name_from not in node.end_nodes:
					node.end_nodes[node_name_from] = node_id_from

			# add to known neighbours
			add_neighbour(node_name_from)

			# dht_ip = get_dht_ip(node_name_from)
			# send(node.dhtEngine.dht, dht_ip)

			# reply with CRQNR
			payload = create_payload(node.ids, node.node_name, node_name_from_arr, "CRQNR", node.dhtEngine.dht, node.type)
			ip = get_ip(node_name_from)
			send(payload, ip)
		if payload_type == 'CRQNR':
			print("Received payload CRQNR")
			add_neighbour(node_name_from)

			if node.type == "backbone":
				node.dhtEngine.rebuild_dht(node.backbone_nodes)


			# dht_ip = get_dht_ip(node_name_from)
			# send(node.dhtEngine.dht, dht_ip)
			# send final ok
			#TODO
			return ''

		if payload_type == 'lsa':
			# received lsa
			# build lsdb
			# add node_name_from to lsdb, add neighbours
			received_lsdb = data['lsdb']

			# check if exists, if not then add, if it does then append
			if node_name_from not in node.lsdb:
				node.lsdb[node_name_from] = data['neighbours']
			else:
				node.lsdb[node_name_from] = merge_two_arrays(node.lsdb[node_name_from], data['neighbours'])

			# now take lsdb of received and merge with own lsdb
			for key in received_lsdb:
				if key in node.lsdb.keys():
					node.lsdb[key] = merge_two_arrays(node.lsdb[key], received_lsdb[key])
				else:
					node.lsdb[key] = received_lsdb[key]
	return ''

@app.route('/neighbours', methods=['GET'])
def neighbours():
	return jsonify(node.neighbours)


@app.route('/info', methods=['GET'])
def info():
	info = {"ids": node.ids, "nodename": node.node_name, "type": node.type, "neighbours": node.neighbours, "dht": node.dhtEngine.dht, "lsdb": node.lsdb, "end_nodes": node.end_nodes}
	return jsonify(info)

@app.route('/lsa', methods=['GET'])
def lsa():
	# begin linked state advertisement
	# dont advertise self if not backbone node

	# create payload,
	lsa_payload = {'node_ids': node.ids, 'node_name': node.node_name, 'neighbours': node.neighbours, 'type': "lsa", 'seqn': node.seqn, 'lsdb': node.lsdb, 'node_type': node.type}

	# begin flooding
	for neighbour in node.neighbours:
		ip = get_ip(neighbour)
		send(lsa_payload, ip)
	return ''

def merge_two_dicts(x, y):
    z = x.copy()   # start with x's keys and values
    z.update(y)    # modifies z with y's keys and values & returns None
    return z

def merge_two_arrays(x, y):
	in_first = set(x)
	in_second = set(y)

	in_second_but_not_in_first = in_second - in_first
	result = x + list(in_second_but_not_in_first)
	return result

def add_neighbour(potential_neighbour):

	# my_neighbours = []
	#
	# for n in node.neighbours:
	# 	key = n.keys()[0]
	# 	my_neighbours.append(key)

	if potential_neighbour not in node.neighbours:
		node.neighbours.append(potential_neighbour)


def read_table():
	with open('finger_table_node_1.txt') as json_file:
		data = json.load(json_file)
		return json.dumps(data)

def contains(key):
	keys = read_table()
	if key in keys:
		return node_id

# @app.route('/ping', methods=['GET'])
# def ping():
# 	# node = (self.node_id, self.node_ip)
# 	# str = ','.join(node)
# 	# return str
# 	return read_table()

@app.route('/graph', methods=['GET', 'POST'])
def lsdb_to_graph():
	    # ("a", "b", 7),  ("a", "c", 9),  ("a", "f", 14), ("b", "c", 10),
	    # ("b", "d", 15), ("c", "d", 11), ("c", "f", 2),  ("d", "e", 6),
	    # ("e", "f", 9)])

	data = request.get_json()
	if data:
		print("yeeeee: {}".format(json.dumps(data)))
		start = data[0]
		dest = data[1]

	if data:
		shortest_path = dijkstra(start, dest)
		return jsonify(shortest_path)
	else:
		return ""

@app.route('/find', methods=['POST'])
def find():
	# this should find the next node to send, if we are at a end node, use dijkstra, pass it go next node


	print("Received routing request")

	data = request.get_json()
	destination = node.dhtEngine.get_key_from_node_id(data['dest'])
	compare_dijk_length = []

	payload = {'dest': destination}

	# TODO change to node.id after intergration of dht
	if destination == node.node_name:
		# destination in node.ids
		print("Received full package")
		return "Received full package!"

	# first check if end node is connected to this

	if destination in node.end_nodes:
		# send
		ip = get_routing_ip(destination)
		send(payload, ip)
		return "Dijkstra routing complete!"

	# method 1
	# for neighbour in node.neighbours:
	# 	sp = dijkstra(neighbour, destination)
		# compare this to the next
		# len(sp.split(","))

	# --------------

	if node.type != 'end':
		# method 2
		shortest_path = dijkstra(node.node_name, destination)
		print("Using node.node_name")
	else:
		print("Using node.neighbours[0]")
		shortest_path = dijkstra(node.neighbours[0], destination)


	print("Calculated shortest path {}".format(shortest_path))

	shortest_path = shortest_path.split(',')
	next_node = shortest_path[0]
	print("next node is {}".format(next_node))
	# we have reached a path of two nodes
	if next_node == node.node_name:
		print("next_node == node.node_name")
		next_node = shortest_path[1]


	ip = get_routing_ip(next_node)
	print("Routing to {} with payload: {}".format(ip, payload))
	send(payload, ip)
	return jsonify(next_node)





def dijkstra(start, dest):
	keys = node.lsdb.keys()
	graph_array = []

	for key in keys:
		node_array = node.lsdb[key]
		for n in node_array:
			graph_array.append((key, n, 1))

	import dijkstra2

	graph = dijkstra2.Graph(graph_array)
	shortest_path = graph.dijkstra(start, dest)
	return shortest_path

def keys():
	'''
	Returns all keys in all nodes
	'''

# @app.route('/db/<key>', methods=['GET'])
# def get(key):
# 	'''
# 	Returns value stored at key
# 	'''
#
# 	'''
# 	get(k)
# 	check if node has key return,
# 	for all keys in my finger table
# 		find closest key(ck) to k
# 		query with find(ck)
#
# 	'''
#
# 	return key

# TODO



def create_payload(node_ids, node_name, neighbours, rq, dht, type):
	payload = {'node_ids': node_ids, 'node_name': node_name, 'neighbours': neighbours, 'type': rq, 'dht': dht, 'node_type': node.type}
	return payload

def send(payload, ip):
	print("payload {}".format(payload))
	print("ip {}".format(ip))
	headers = {'Content-type': 'application/json'}
	r = requests.post(ip, headers=headers, data=json.dumps(payload))
	print("callback {}".format(r.status_code))
	return ""

def get_ip(node_id):
	# print("node id is: " + node_id)
	with open('tables/ips.json') as json_file:
		data = json.load(json_file)
		if node_id in data:
			return 'http://127.0.0.1:' + str(data[node_id]) + '/receive'

def get_routing_ip(node_id):
	# print("node id is: " + node_id)
	with open('tables/ips.json') as json_file:
		data = json.load(json_file)
		if node_id in data:
			return 'http://127.0.0.1:' + str(data[node_id]) + '/find'

def get_dht_ip(node_id):
	# print("node id is: " + node_id)
	with open('tables/ips.json') as json_file:
		data = json.load(json_file)
		if node_id in data:
			return 'http://127.0.0.1:' + str(data[node_id]) + '/receive/dht'

def put(key):
	'''
	Inserts key into DHT, returns True/False for error handling
	'''

def delete(key):
	'''
	Deletes key from DHT, returns True/False for error handling
	'''

def peers():
	'''
	Displays all peers
	'''

def create_finger_table():
	'''
	Creates the lookup table for each node
	'''

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument("-t", "--type", help="The type of node to spawn")
	parser.add_argument("-n", "--name", help="The name of node to spawn")
	parser.add_argument("-id", "--id", help="The id of node to spawn")
	parser.add_argument("-ip", "--ip", help="The ip of node to spawn")
	args = parser.parse_args()
	if args.type is None:
		node = Node(args.name, "normal")
	else:
		node = Node(args.name, args.type)

	app.run(host='localhost', port=int(args.ip), threaded=True)
