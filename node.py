import json

def main():
	print("Starting client")

if __name__ == "__main__":
	main()

class Node:

	def __init__():
		self.node_id = None
		self.node_ip = None

		self.sucessor_id = None

		self.data_dict = dict()

		self.finger_table = None

	def init():
		print("init node")

	def keys():
		'''
		Returns all keys in all nodes
		'''

	def get(key):
		'''
		Returns value stored at key
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
