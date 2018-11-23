#!/usr/bin/python

class Node:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right
		
	def __repr__(self):
		return f"{self.val}"
		
def serialize(node):
	
	if node.left: serialize(node.left)
	l+=node.val
	if node.right: serialize(node.right)
	
	
	return 
	
def deserialize(node):
	return node
		
if __name__ == "__main__":
	l=""
	node = Node('root', Node('left', Node('left.left')), Node('right'))
	print(serialize(node))
	#assert deserialize(serialize(node)).left.left.val == 'left.left'