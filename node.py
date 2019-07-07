import json
from flask import jsonify
from flask import Flask
app = Flask(__name__)



'''
Let backbone nodes be bnodes
'''

# @app.route("/")
# def hello():
# 	return "Node 1!"


# def __init__():


# @app.route('db/route', methods=['GET'])
# def crawl():
# 	for i in 5001 to 5010:

@app.route("/")
def backbone():
	# create the backbone nodes

	# gets all neighbours, reads from table
	with open('tables/node1_me.json') as json_file_me:
		my_id = json.load(json_file_me)
		# return me_data

	with open('tables/backbone.json') as json_file_backbone:
		backbone_data = json.load(json_file_backbone)
		# return jsonify(backbone_data)

	if my_id in backbone_data:
		neighbours_list = backbone_data[my_id]
		return jsonify(neighbours)
	else:
		return "No"
	# 	return "yes"

	# send hello signal to neighbour to establish 2-way connection
	my_rid = my_id
	curren_neighbours = []
	type = "hello"

	send(payload, ip)




def read_table():
	with open('finger_table_node_1.txt') as json_file:
		data = json.load(json_file)
		return json.dumps(data)

def contains(key):
	keys = read_table()
	if key in keys:
		return node_id

@app.route('/ping', methods=['GET'])
def ping():
	# node = (self.node_id, self.node_ip)
	# str = ','.join(node)
	# return str
	return read_table()

def keys():
	'''
	Returns all keys in all nodes
	'''

@app.route('/db/<key>', methods=['GET'])
def get(key):
	'''
	Returns value stored at key
	'''

	'''
	get(k)
	check if node has key return,
	for all keys in my finger table
		find closest key(ck) to k
		query with find(ck)

	'''

	return key

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
