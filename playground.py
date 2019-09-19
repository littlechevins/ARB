

import os
import hashlib
import random
import string
import base64
from random import randrange

import re

import math
def rebalance_dht():

	backbone_nodes = ["1", "2", "3", "4"]
	dht = {}

	alpha_num_set = "abcdefghijklmnopqrstuvwxyz0123456789"

	# dht_count = len(node.dht)
	dht_count = len(backbone_nodes)

	equal_share = int(math.ceil((36 / dht_count)))		#36 for ALPHA + NUMERIC

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

		# if node in node.dht:
		dht[node] = key
		# else:
		# 	raise ValueError("Could not locate {} node in dht table.".format(node))

	# print(dht)
	print("1: " + dht["1"])
	print("2: " + dht["2"])
	print("3: " + dht["3"])
	print("4: " + dht["4"])

def get_random():
	# random_data = os.urandom(128)
	# return hashlib.md5(random_data).hexdigest()[:8]
	x = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(8))
	return x


def keygen(key_range, rb):

	while True:
		hasher = hashlib.md5(get_random())
		h1 = base64.urlsafe_b64encode(hasher.digest())
		# print("pre sub: " + h1)
		h1 = re.sub('[!@#$=-_-\\xe2]', '', h1)
		h1 = h1[:10]
		# ids.append(h1)
		# print("post sub: " + h1)
		print("measng key rb {}".format(h1[:rb]))
		if in_key_range(key_range, h1[:rb]):
			return h1



def in_key_range(range, k):

	lower, upper = k.split('-')
	key = base36decode(k)
	lower_decoded = base36decode(lower)
	upper_decoded = base36decode(upper)

	if lower_decoded <= key <= upper_decoded:
		return True
	else:
		return False


def keygen2():

	hasher = hashlib.md5(get_random())
	h1 = base64.urlsafe_b64encode(hasher.digest())
	# print("pre sub: " + h1)
	h1 = re.sub('[!@#$=-_-\\xe2]', '', h1)
	h1 = h1[:10]
	# ids.append(h1)
	print("post sub: " + h1)


# def randrange():
# 	for _ in range(0,10):
# 		print(random.randrange(1,3))
#
# 	def increment(self, element):
#
# 		index = self.alpha_num_set.index(element)
#
# 		# Last element, we cant increment, but should not reach!
# 		if index == 35:
# 			print("Should not reach!! End of array")
# 		else:
# 			index += 1
# 			return self.alpha_num_set[index]

def increment(element):

	alpha_num_set = list("abcdefghijklmnopqrstuvwxyz0123456789")

	index = alpha_num_set.index(element)

	# Last element, we cant increment, but should not reach!
	if index == 35:
		# print("Should not reach!! End of array")
		return 'a'
	else:
		index += 1
		return alpha_num_set[index]

# def gen_next_key(bf, k):
#
# 	key = list(k)
#
# 	buffer_size = bf
# 	final_key = ''
# 	print("startinb buffer size {}".format(buffer_size))
#
# 	for i, char in enumerate(key):
# 		current_buffer_index = pow(36, len(key) - i - 1)
# 		# print(current_buffer_index)
# 		print("at: {}".format(char))
# 	# index = i
# 	# while buffer_size > current_buffer_index:
# 	# 	increment(key[i])
# 	# 	bf =- current_buffer_index
# 	# 	index += 1
# 	# 	current_buffer_index = pow(36, index)
# 		index = i
# 		current_char = char
# 		while buffer_size >= current_buffer_index:
# 			print("yes")
# 			print("current_buffer_index: {}".format(current_buffer_index))
# 			print("current_char: {}".format(current_char))
# 			print("original buffer size: {}".format(buffer_size))
# 			current_char = increment(current_char)
# 			buffer_size -= current_buffer_index
# 			print("current_buffer_size_after: {}".format(buffer_size))
# 			index += 1
# 			# current_buffer_index = pow(36, len(key) - index - 1)
# 			print("current_buffer_index_after: {}".format(current_buffer_index))
#
# 		final_key += current_char
#
# 	return final_key

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


def gen_next_key(bf, k, rb):
	key = base36decode(k)
	encoded = base36encode(key+bf)
	# if len(encoded) > len(k):
	# 	return 'z' * rb
	# else:
	return encoded

def rebuild_dht(rb, backbone_nodes, num_nodes):

	buffer = int(pow(36, rb) / num_nodes) - 1

	next_key = '0' * rb
	print(next_key)

	dht_array = []
	dht_array.append(next_key)

	switch = True

	for n in range(num_nodes*2 - 1):
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

	dht_array[-1] = 'z' * rb

	print(dht_array)

	dht = {}

	key_count = 0
	for index in range(0, len(dht_array) - 1, 2):
		key = dht_array[index] + '-' + dht_array[index+1]
		dht[key] = backbone_nodes[key_count]
		key_count += 1

	print(dht)
	return dht

def get_key_from_node_id(id, rb, dht):

	id = base36decode(id[:rb])

	for key in dht.keys():

		lower, upper = key.split('-')

		lower_decoded = base36decode(lower)
		upper_decoded = base36decode(upper)

		if lower_decoded <= id <= upper_decoded:
			return dht[key]

	return "ERROR"

def restructure_backbone(backbone_nodes):
	backbone_nodes.sort(key=int)
	return backbone_nodes


def main():
	print("Starting")
	# rebalance_dht()
	# keygen()
	# randrange()
	# print(increment('9'))
	# print(gen_next_key(35, 'abcd'))

	# 1234

	# print(base36encode(481261+35))
	# print(base36decode('abcd'))
	# print(gen_next_key(1000, 'abcd'))
	# key = 'a' * 3
	# if ('aaa' == key):
	# 	print("true")
	# arr = ["A", "B", "C", "D", "E", "F", "G", "F", "A", "B", "C", "D", "E", "F", "G", "F", "A", "B", "C", "D", "E", "F", "G", "F", "A", "B", "C", "D", "E", "F", "G", "F"]
	# rebuild_dht(1, arr, 12)

	# lower = 20
	# upper = 29
	# if lower <= 27 <= 29:
	# 	print("TRUEEEE")
	#
	# print(get_key_from_node_id("g5", 2, rebuild_dht(2)))
	# my_list = ["5", "7", "4", "11", "1"]
	# my_list = ["node_5", "node_7", "node_4", "node_11", "node_1"]
	# my_list = [1, 5, 6, 7, 11,3, 5,7, 2, 8]
	# print(restructure_backbone(my_list))

	# dht = {'x-z': u'Zerind', 'u-w': u'Timisoara', '6-8': u'Drobeta', '0-2': u'Arad', 'r-t': 'Sibiu', '3-5': u'Craiova', 'i-k': u'Oradea', 'l-n': u'Pitesti', '9-b': u'Fagaras', 'f-h': u'Mehadia', 'c-e': u'Lugoj', 'o-q': u'Rimnicu_Vilcea'}
	# print(get_key_from_node_id(u'Drobeta', 1, dht)

	# key_range = '0-r'
	# rb = 1
	# key = keygen(key_range, rb)
	# print(key)

	print(keygen2())


if __name__ == "__main__":
	main()
