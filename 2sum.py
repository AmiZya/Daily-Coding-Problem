import os
def sum(l, k):
	for i in l:
		if l.get(k-i, None):
			print(f"{k} = {i} + {k-i}")
			
if __name__ == "__main__":
	l = {10:10, 15:15, 3:3, 7:7}
	sum(l, 17)