import math


'''
If a node is overloaded, it can request a reconstruction of the DHT and update the RB to a larger value
'''

class DHT:

	def __init__(self):
		self.dht = {}					# DHT table for PK and IP addresses
		self.rb = 1						# Routing bytes, influenced by total number of backbone nodes and total load
		self.alpha_num_set = list("0123456789abcdefghijklmnopqrstuvwxyz")
		self.num_nodes = 0

	@property
	def _get_dht(self):
		return self.dht

	@staticmethod
	def base36encode(number, alphabet='0123456789abcdefghijklmnopqrstuvwxyz'):
		"""Converts an integer to a base36 string."""

		base36 = ''
		sign = ''

		if number < 0:
			sign = '-'
			number = -number

		if 0 <= number < len(alphabet):
			return sign + alphabet[number]

		while number != 0:
			number, i = divmod(number, len(alphabet))
			base36 = alphabet[i] + base36

		return sign + base36

	@staticmethod
	def base36decode(number):
		return int(number, 36)

	def gen_next_key(self, bf, k):
		key = self.base36decode(k)
		encoded = self.base36encode(key + bf)
		return encoded

	def rebuild_dht(self, backbone_nodes):

		if len(backbone_nodes) == 0:
			return {}

		num_nodes = self.num_nodes

		buffer = int(pow(36, self.rb) / num_nodes) - 1

		next_key = '0' * self.rb

		dht_array = []
		dht_array.append(next_key)

		switch = True

		for n in range(num_nodes * 2 - 1):
			if switch:
				next_key = self.gen_next_key(buffer, next_key)
				switch = False
			else:
				next_key = self.gen_next_key(1, next_key)
				switch = True
			dht_array.append(next_key)

		dht_array[-1] = 'z' * self.rb

		dht = {}
		key_count = 0
		for index in range(0, len(dht_array) - 1, 2):
			key = dht_array[index] + '-' + dht_array[index + 1]
			dht[key] = backbone_nodes[key_count]
			key_count += 1
		self.dht = dht


	# Rebalanced everytime a new node joins
	def rebalance_dht(self, dht, backbone_nodes):

		alpha_num_set = "0123456789abcdefghijklmnopqrstuvwxyz"

		dht_count = len(backbone_nodes)

		equal_share = int(math.ceil((36 / dht_count)))  # 36 for ALPHA + NUMERIC

		string_start = 0
		string_end = equal_share

		for node in backbone_nodes:
			key = alpha_num_set[string_start:string_end]

			string_start += equal_share
			string_end = string_start + equal_share

			if string_end > len(alpha_num_set):
				string_end = 35

			if node in node.dht:
				dht[node] = key
			else:
				raise ValueError("Could not locate {} node in dht table.".format(node))

	def get_key_from_node_id(self, id):

		id = self.base36decode(id[:self.rb])

		for key in self.dht.keys():

			lower, upper = key.split('-')

			lower_decoded = self.base36decode(lower)
			upper_decoded = self.base36decode(upper)

			if lower_decoded <= id <= upper_decoded:
				return self.dht[key]

		return "NO KEY FOUND IN DHT"

	def get_assigned_key(self, node_name):
		for key in self.dht.keys():
			if self.dht[key] == node_name:
				return key

	def in_key_range(self, range, k):
		range = range.replace('"', '')
		k = k.replace('"', '')
		lower, upper = range.split('-')
		key = self.base36decode(k)
		lower_decoded = self.base36decode(lower)
		upper_decoded = self.base36decode(upper)

		if lower_decoded <= key <= upper_decoded:
			return True
		else:
			return False

