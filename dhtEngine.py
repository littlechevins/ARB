import math


'''
If a node is overloaded, it can request a reconstruction of the DHT and update the RB to a larger value
'''

class DHT:

	def __init__(self):
		self.dht = {}					# DHT table for PK and IP addresses
		self.rb = 1						# Routing bytes, influced by total number of backbone nodes and total load
		self.alpha_num_set = list("abcdefghijklmnopqrstuvwxyz0123456789")
		self.num_nodes = 0

	def base36encode(number, alphabet='0123456789abcdefghijklmnopqrstuvwxyz'):
		"""Converts an integer to a base36 string."""
		# if not isinstance(number, (int, long)):
		# 	raise TypeError('number must be an integer')

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

	def base36decode(number):
		return int(number, 36)

	def gen_next_key(bf, k):
		key = base36decode(k)
		return (base36encode(key + bf))

	def gen_next_key(self, bf, k):

		key = base36decode(k)
		return (base36encode(key + bf))

	def rebuild_dht(rb):

		num_nodes = 4

		buffer = int(pow(36, rb) / num_nodes)

		next_key = '0' * rb
		print(next_key)

		once_off = True
		dht_array = []
		dht_array.append(next_key)

		switch = True

		for n in range(num_nodes * 2 - 1):
			# print(buffer)
			# print(next_key)
			if switch:
				next_key = gen_next_key(buffer, next_key, rb)
				switch = False
			else:
				next_key = gen_next_key(1, next_key, rb)
				switch = True
			print(next_key)
			dht_array.append(next_key)

		print(dht_array)

		dht = {}

		for index in range(0, len(dht_array) - 1, 2):
			key = dht_array[index] + '-' + dht_array[index + 1]
			dht[key] = 'NODE_X'

		print(dht)



	# Rebalanced everytime a new node joins
	def rebalance_dht(dht, backbone_nodes):

		alpha_num_set = "abcdefghijklmnopqrstuvwxyz0123456789"

		# dht_count = len(node.dht)
		dht_count = len(backbone_nodes)

		equal_share = int(math.ceil((36 / dht_count)))  # 36 for ALPHA + NUMERIC

		# loop all bnodes and assign them its equal share from the pool,
		# recalcualte dht baased on that
		# broadcast a reassign

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
