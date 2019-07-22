
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

class Node:


	# Node types
	# backbone - DR node, broadcasters
	# normal

	def __init__(self, node_name, type):
		# self.id = self.get_id()
		self.id = None
		self.node_name = node_name
		self.neighbours = []
		self.type = type
		self.dht = {}
		self.seqn = 0 				# sequence number for lsa
		self.lsdb = {}

		self.end_nodes = {}			# {Node_ID, NODE_IP}



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
parser.add_argument("-id", "--id", help="The id of node to spawn")
parser.add_argument("-ip", "--ip", help="The ip of node to spawn")
args = parser.parse_args()
if args.type is None:
	node = Node(args.id, "backbone")
else:
	node = Node(args.id, args.type)



@app.route("/tester")
def tester():
	return node.id


def get_id():
	# random_data = os.urandom(128)
	# return hashlib.md5(random_data).hexdigest()[:8]
	x = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(8))
	return x

def get_key_from_id(id):
	print("TYPE!!!")
	print(type(id))
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


# def manual_assign(self):
# 	# key_ranges = ['0-9', 'a-f', 'g-l', 'm-z']
# 	random_assign = random.randint(0,3)
#
# 	if random_assign == 0:
# 		id = str(get_id())
# 		if id.index(0)

@app.route("/setup")
def setup():
	if(node.type == 'end'):
		node.id = get_id()
	elif(node.type == 'backbone'):
		node.id = get_id()
	else:
		print("ERROR, no type found")
		return ""


	# Here we also setup the end nodes to their parent

	return node.id


@app.route("/")
def backbone():
	# create the backbone nodes

	# gets all neighbours, reads from table
	with open('tables/backbone.json') as json_file_backbone:
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

	if node.id is not None:
		# generate id for self, send along
		# node.id = get_id()
		node.dht[get_key_from_id(node.id)] = node.id

	for neighbour in neighbours_list:
		payload = create_payload(node.id, node.node_name, current_neighbours, "IRQ", node.dht, node.type)
		ip = get_ip(neighbour)
		send(payload, ip)
	print("STOP")
	return "DONE"


@app.route('/receive', methods=['POST'])
def receive():


	data = request.get_json()
	print("yeeeee: {}".format(json.dumps(data)))

	received_node_name = data['node_name']
	# node_id_from = data['node_id']
	node_name_from_arr = [received_node_name]
	print("print data contents{}".format(data))
	received_node_type = data['node_type']

	if 'dht' in data:
		node_dht_from = data['dht']
		# combine received dht with known
		node.dht = merge_two_dicts(node_dht_from, node.dht)

	# add received id to dht (only add when neighbourship is established)
	# node.dht[node_name_from] = get_key_from_id(node_name_from)



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
				# node.dht[get_key_from_id(node.id)] = node.id
	# 			break

	# if node.key not in node_dht_from:
	# node.dht[get_key_from_id(node.id)] = node.id

	if 'msg_type' in data:
		payload_type = data['msg_type']

		if payload_type == 'IRQ':

			# Received a neighbour request, if node.type is end node, then reply differently

			print("Received payload IRQ")
			# reply with IRQNR
			payload = create_payload(node.id, node.node_name, node_name_from_arr, "IRQNR", node.dht, node.type)
			ip = get_ip(received_node_name)
			send(payload, ip)
		if payload_type == 'IRQNR':
			print("Received payload IRQNR")

			# check for node type, if end node

			# add to known neighbours, excluding end node
			# if received_node_type != 'end':
			add_neighbour(received_node_name)


			# dht_ip = get_dht_ip(received_node_name)
			# send(node.dht, dht_ip)

			# reply with CRQNR
			payload = create_payload(node.id, node.node_name, node_name_from_arr, "CRQNR", node.dht, node.type)
			ip = get_ip(received_node_name)
			send(payload, ip)
		if payload_type == 'CRQNR':
			print("Received payload CRQNR")
			# if received_node_type != 'end':
			add_neighbour(received_node_name)
			# dht_ip = get_dht_ip(received_node_name)
			dht_ip = get_ip(received_node_name)
			send(node.dht, dht_ip)
			return ''

		if payload_type == 'lsa':
			# received lsa
			# build lsdb
			# add node_name_from to lsdb, add neighbours
			received_lsdb = data['lsdb']

			# check if exists, if not then add, if it does then append
			if received_node_name not in node.lsdb:
				node.lsdb[received_node_name] = data['neighbours']
			else:
				node.lsdb[received_node_name] = merge_two_arrays(node.lsdb[received_node_name], data['neighbours'])

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
	info = {"id": node.id, "nodename": node.node_name, "type": node.type, "neighbours": node.neighbours, "dht": node.dht, "lsdb": node.lsdb}
	return jsonify(info)

@app.route('/lsa', methods=['GET'])
def lsa():
	# begin linked state advertisement
	# dont advertise self if not backbone node


	# Remove later since we only cull at creation time
	# remove_end_nodes_from_lsdb()


	# create payload,
	lsa_payload = {'node_id': node.id, 'node_name': node.node_name, 'neighbours': node.neighbours, 'type': "lsa", 'seqn': node.seqn, 'lsdb': node.lsdb, 'node_type': node.type}

	# begin flooding
	for neighbour in node.neighbours:
		ip = get_ip(neighbour)
		print("sending to {}".format(ip))
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

def remove_end_nodes_from_lsdb():

	for enode in node.end_nodes.keys():
		node.lsdb.pop(enode, None)


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

@app.route('/graph', methods=['POST'])
def lsdb_to_graph():
	    # ("a", "b", 7),  ("a", "c", 9),  ("a", "f", 14), ("b", "c", 10),
	    # ("b", "d", 15), ("c", "d", 11), ("c", "f", 2),  ("d", "e", 6),
	    # ("e", "f", 9)])
	data = request.get_json()
	print("dijkstra request{}".format(json.dumps(data)))

	keys = node.lsdb.keys()
	graph_array = []

	for key in keys:
		node_array = node.lsdb[key]
		for n in node_array:
			graph_array.append((key, n, 1))


	import dijkstra2

	graph = dijkstra2.Graph(graph_array)
	shortest_path = graph.dijkstra(data[0], data[1])

	return jsonify(shortest_path)


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

def create_payload(node_id, node_name, neighbours, rq, dht, node_type):
	payload = {'node_id': node_id, 'node_name': node_name, 'neighbours': neighbours, 'msg_type': rq, 'dht': dht, 'node_type': node_type}
	return payload

def send(payload, ip):
	print("payload {}".format(payload))
	print("ip {}".format(ip))
	headers = {'Content-type': 'application/json'}
	r = requests.post(ip, headers=headers, data=json.dumps(payload))
	print("callback {}".format(r.status_code))
	return ""

def get_ip(node_id):
	print("node id is: " + node_id)
	with open('tables/ips.json') as json_file:
		data = json.load(json_file)
		if node_id in data:
			return 'http://127.0.0.1:' + str(data[node_id]) + '/receive'

def get_dht_ip(node_id):
	print("node id is: " + node_id)
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
	parser.add_argument("-id", "--id", help="The id of node to spawn")
	parser.add_argument("-ip", "--ip", help="The ip of node to spawn")
	args = parser.parse_args()
	if args.type is None:
		node = Node(args.id, "normal")
	else:
		node = Node(args.id, args.type)

	app.run(host='localhost', port=int(args.ip), threaded=True)
