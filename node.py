
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
# No link is considered to have been correctly reported unless the two ends agree; i.e., if one node reports that it
# is connected to another, but the other node does not report that it is connected to the first, there is a problem,
# and the link is not included on the map.



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
import threading
from random import randrange


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
		self.backbone_nodes = []		# List of all bnodes

		self.dhtEngine = DHT()

		self.threshold = {}
		self.threshold_value = 0

		# Only enodes
		self.associated_bnodes = []		# Contains a list of bnodes and id pair related

		# Only bnodes
		self.end_nodes = []				# Contains a list of its enodes that have a id key pair

		self._BACKBONE_INIT_DELAY = 0.0
		self._URL_BASE = 'http://127.0.0.1:'

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


@app.route("/setup")
def setup():

	with open('tables/node_info.json') as node_info:
		node_info_json = json.load(node_info)
		node.type = node_info_json[node.node_name]["node_type"]
		# node.ids = node_info_json[node.node_name]["node_ids"]

		print("Setup phase, node type: {}".format(node.type))

	# Setup associated nodes
	with open('tables/associated_bnode.json') as node_info:
		node_info_json = json.load(node_info)

		if node.type == 'end':

			node.associated_bnodes = node_info_json[node.node_name]

			for bnode in node.associated_bnodes:
				key = keygen()
				print("generated key: {}".format(key))
				node.ids.append({bnode: key})

			# node.id = node_info_json[node.node_name]["node_ids"][0]
		elif node.type == 'backbone':
			# node.id = None
			pass
		else:
			print("ERROR, no type found")
			return ""

	return "Setup!"


@app.route("/")
def backbone():

	print("Establishing backbones...")

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


	# send hello signal to neighbour to establish 2-way connection
	current_neighbours = []

	# if node.id is None:
		# generate id for self, send along
		# node.id = get_id()
		# node.id = get_random()
		# node.dht[get_key_from_id(node.id)] = node.id

	node.backbone_nodes.append(node.node_name)

	for neighbour in neighbours_list:
		payload = create_payload(node.ids, node.node_name, current_neighbours, "IRQ", node.dhtEngine.dht, node.type, node.backbone_nodes)
		ip = get_ip(neighbour)
		send(payload, ip)
		# time.sleep(0.1)
	# print("STOP")

	print("Starting LSA...")

	# timer = threading.Timer(node.BACKBONE_INIT_DELAY, double_lsa)
	# timer.start()

	# r = randrange(10)
	# time.sleep(r)
	# for _ in range(0, 10):
	# 	r2 = randrange(2)
	# 	time.sleep(r2)
	# 	lsa()
	lsa(False)
	lsa(True)


	return "DONE"


@app.route('/receive', methods=['POST'])
def receive():

	'''

	:return:

	# payload types:
	# IRQN - initial request neighbour - sends self id to neighbours
	# IRQNR - initial request neighbour reply - sends self id and known neighbours - R1 becomes 2way
	# CRQNR - confirm request neighbour reply - sends self id and known neighbours - R2 becomes 2way
	# LSA - linked state advertisement

	'''

	data = request.get_json()

	node_name_from = data['node_name']
	node_id_from = data['node_ids']
	node_name_from_arr = [node_name_from]


	# if 'dht' in data:
	# 	node_dht_from = data['dht']
		# combine received dht with known
		# node.dhtEngine.dht = merge_two_dht(node_dht_from, node.dhtEngine.dht)

	if 'node_type' in data:
		print("found node_type in data, is {}".format(data['node_type']))
		received_node_type = data['node_type']

	# add received id to dht (only add when neighbourship is established)
	# node.dhtEngine.dht[node_name_from] = get_key_from_id(node_name_from)
	if 'backbone_nodes' in data:
		received_backbone_nodes = data['backbone_nodes']

		if received_node_type == 'backbone':
			# node.backbone_nodes = merge_two_arrays(received_backbone_nodes, node.backbone_nodes)
			merge_into_backbone_nodes(received_backbone_nodes)
			node.dhtEngine.num_nodes = len(node.backbone_nodes)

	if 'type' in data:
		payload_type = data['type']

		if payload_type == 'IRQ':

			# node.dhtEngine.rebuild_dht(node.backbone_nodes)

			print("Received payload IRQ")
			# reply with IRQNR
			payload = create_payload(node.ids, node.node_name, node_name_from_arr, "IRQNR", node.dhtEngine.dht, node.type, node.backbone_nodes)
			ip = get_ip(node_name_from)
			send(payload, ip)
		if payload_type == 'IRQNR':
			print("Received payload IRQNR")

			# check if sender is end node
			if received_node_type and received_node_type == 'end':
				print("RECEIVED MESSAGE FROM END NODE {}".format(node_name_from))
				# check if doesnt already exist
				if node_name_from not in node.end_nodes:
					list_of_end_nodes = []
					for dicts in node_id_from:
						keys = dicts.keys()
						for key in keys:
							if key == node.node_name:
								list_of_end_nodes.append(dicts[key])

					node.end_nodes.append({node_name_from: list_of_end_nodes})

			# add to known neighbours
			add_neighbour(node_name_from)

			# dht_ip = get_dht_ip(node_name_from)
			# send(node.dhtEngine.dht, dht_ip)
			# node.dhtEngine.rebuild_dht(node.backbone_nodes)

			# reply with CRQNR
			payload = create_payload(node.ids, node.node_name, node_name_from_arr, "CRQNR", node.dhtEngine.dht, node.type, node.backbone_nodes)
			ip = get_ip(node_name_from)
			send(payload, ip)
		if payload_type == 'CRQNR':
			print("Received payload CRQNR")
			add_neighbour(node_name_from)

			# if node.type == "backbone":
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

@app.route('/rebalance', methods=['GET'])
def manual_rebalance():

	node.dhtEngine.num_nodes = len(node.backbone_nodes)
	node.dhtEngine.rebuild_dht(node.backbone_nodes)
	return json.dumps({'success': 'rebalance'})

@app.route('/info', methods=['GET'])
def info():
	info = {"ids": node.ids, "nodename": node.node_name, "type": node.type, "neighbours": node.neighbours,
			"dht": node.dhtEngine.dht, "lsdb": node.lsdb, "end_nodes": node.end_nodes,
			"backbone_nodes": node.backbone_nodes, "associated_bnodes": node.associated_bnodes}
	return jsonify(info)

# @app.route('/lsa', methods=['GET'])
def lsa(direction):
	# begin linked state advertisement
	# dont advertise self if not backbone node

	# create payload,
	lsa_payload = {'node_ids': node.ids, 'node_name': node.node_name, 'neighbours': node.neighbours, 'type': "lsa", 'seqn': node.seqn, 'lsdb': node.lsdb, 'node_type': node.type, 'backbone_nodes': node.backbone_nodes}
	print("my neighbours {}".format(node.neighbours))
	# begin flooding

	if direction:
		for neighbour in node.neighbours:
			ip = get_ip(neighbour)
			print("LSDB sending to {} with payload {}".format(ip, lsa_payload))
			send(lsa_payload, ip)
	else:
		for neighbour in reversed(node.neighbours):
			ip = get_ip(neighbour)
			print("LSDB sending to {} with payload {}".format(ip, lsa_payload))
			send(lsa_payload, ip)
	return json.dumps({'success': 'lsa_send'})

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

def merge_into_backbone_nodes(y):
	for element in y:
		if element not in node.backbone_nodes:
			node.backbone_nodes.append(element)



def add_neighbour(potential_neighbour):

	if potential_neighbour not in node.neighbours:
		node.neighbours.append(potential_neighbour)



@app.route('/graph', methods=['GET', 'POST'])
def lsdb_to_graph():
	    # ("a", "b", 7),  ("a", "c", 9),  ("a", "f", 14), ("b", "c", 10),
	    # ("b", "d", 15), ("c", "d", 11), ("c", "f", 2),  ("d", "e", 6),
	    # ("e", "f", 9)])

	data = request.get_json()
	if data:
		# print("yeeeee: {}".format(json.dumps(data)))
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

	print("Data received: {}".format(data))

	destination = node.dhtEngine.get_key_from_node_id(data['dest'])
	origin =  data['dest']

	compare_dijk_length = []
	print("Destination calculated: {}".format(destination))

	payload = {'origin': data['origin'], 'dest': destination}


	# # Threadhold
	# print("node.threshold[origin] {}".format(node.threshold[origin]))
	# if origin in node.threshold:
	# 	if node.threshold[origin] < node.threshold_value:
	# 		node.threshold[origin] += 1
	# 	else:
	# 		raise ValueError("Threshold reached! Value of {} in node {}.".format(node.threshold[origin], origin))
	# else:
	# 	node.threshold[origin] = 1

	if destination == node.node_name:
		if origin in node.threshold:
			node.threshold[origin] += 1
		else:
			node.threshold[origin] = 1

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



def create_payload(node_ids, node_name, neighbours, rq, dht, type, backbone_nodes):
	payload = {'node_ids': node_ids, 'node_name': node_name, 'neighbours': neighbours, 'type': rq, 'dht': dht, 'node_type': node.type, 'backbone_nodes': backbone_nodes}
	return payload

def send(payload, ip):
	print("payload {}".format(payload))
	print("ip {}".format(ip))
	headers = {'Content-type': 'application/json'}
	r = requests.post(ip, headers=headers, data=json.dumps(payload))
	print("callback {}".format(r.status_code))
	return ""
	#TODO do we need this return?

def get_ip(node_id):
	# print("node id is: " + node_id)
	with open('tables/ips.json') as json_file:
		data = json.load(json_file)
		if node_id in data:
			return node._URL_BASE + str(data[node_id]) + '/receive'

def get_routing_ip(node_id):
	# print("node id is: " + node_id)
	with open('tables/ips.json') as json_file:
		data = json.load(json_file)
		if node_id in data:
			return node._URL_BASE + str(data[node_id]) + '/find'

def get_dht_ip(node_id):
	# print("node id is: " + node_id)
	with open('tables/ips.json') as json_file:
		data = json.load(json_file)
		if node_id in data:
			return node._URL_BASE + str(data[node_id]) + '/receive/dht'

def double_lsa():

	timer = threading.Timer(node._BACKBONE_INIT_DELAY, lsa)
	timer.start()

	lsa()


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

	print("Setting up node...")
	setup()

	print("Establishing network...")
	app.run(host='localhost', port=int(args.ip), threaded=True)
