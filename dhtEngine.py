import math


'''
If a node is overloaded, it can request a reconstruction of the DHT and update the RB to a larger value
'''

class DHT:

	def __init__(self):
		self.dht = {}					# DHT table for PK and IP addresses
		self.rb = 1						# Routing bytes, influced by total number of backbone nodes and total load


	def recursive_bytes(self, rb):

		for rr in rb:

			for index in alpha:

	def alphaget(self, number, start_point):

		# "216", "ax"
		# = "gx"

		# "10", "ax"
		# "8", "az"
		# "0", "a7"

		# "14, "ax"
		# "12", "az"
		# "2", "a9"
		# "0", "ba"
		## "+13", "bx
		
		# "+0", "ax"
		# "+13", "ba"
		# "+23", "bx

		'''
		1. look at last char and its position, calculate the number it would take to get to the next flip
		
		1. work out what it would take to flip x values, if that number is less than the given num then flip
		eg. "ax", given "200", "ax", it would take 13 to flip to "ba", we minus 200-13 and if that number is still 
		greater, we do again until its not. Then we go to next char, so we look at "a"
		
		to flip bit we do 36^x
		
		''''''

		 for a in alpha:


	# Forumula

	# (36^rb) / num nodes

	# 6 nodes

	# rb 1
	#["node1" : "q8gl2nvsrt"] = abcde|fghijk|lmnopq|rstuvw|xyz012|3456789

	# rb 2
	#["node1": "q8gl2nvsrt"] = [abcdefghijklmnopqrstuvwxyz0123456789][abcdefghijklmnopqrstuvwxyz0123456789]
	# = [q8-q9, ]






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
