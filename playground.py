

import os
import hashlib
import random
import string
import base64

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


def keygen():
	for x in range(0,30):
		hasher = hashlib.md5(get_random())
		h1 = base64.urlsafe_b64encode(hasher.digest())
		# print("pre sub: " + h1)
		h1 = re.sub('[!@#$=-_-\\xe2]', '', h1)
		h1 = h1[:10]
		# ids.append(h1)
		print("post sub: " + h1)

def randrange():
	for _ in range(0,10):
		print(random.randrange(1,3))

	def increment(self, element):

		index = self.alpha_num_set.index(element)

		# Last element, we cant increment, but should not reach!
		if index == 35:
			print("Should not reach!! End of array")
		else:
			index += 1
			return self.alpha_num_set[index]

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

def gen_next_key(bf, k):

	key = list(k)

	buffer_size = bf
	final_key = ''
	print("startinb buffer size {}".format(buffer_size))

	for i, char in enumerate(key):
		current_buffer_index = pow(36, len(key) - i - 1)
		# print(current_buffer_index)
		print("at: {}".format(char))
	# index = i
	# while buffer_size > current_buffer_index:
	# 	increment(key[i])
	# 	bf =- current_buffer_index
	# 	index += 1
	# 	current_buffer_index = pow(36, index)
		index = i
		current_char = char
		while buffer_size > current_buffer_index:
			print("yes")
			print("current_buffer_index: {}".format(current_buffer_index))
			print("current_char: {}".format(current_char))
			print("original buffer size: {}".format(buffer_size))
			current_char = increment(current_char)
			buffer_size -= current_buffer_index
			print("current_buffer_size_after: {}".format(buffer_size))
			index += 1
			# current_buffer_index = pow(36, len(key) - index - 1)
			print("current_buffer_index_after: {}".format(current_buffer_index))

		final_key += current_char

	return final_key


def main():
	print("Starting")
	# rebalance_dht()
	# keygen()
	# randrange()
	# print(increment('9'))
	print(gen_next_key(35, 'abcd'))

if __name__ == "__main__":
	main()
