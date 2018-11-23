#!/usr/bin/python


def multiply(l):
	ll = []
	for i in l:
		mul = 1
		for j in l:
			if i == j:
				continue
			else:
				mul*=j
		ll.append(mul)
	return ll

if __name__ == "__main__":
	l = [3, 2, 1]
	ll = [1, 2, 3, 4, 5]
	print(multiply(l))
	print(multiply(ll))