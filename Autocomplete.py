def autocomplete(dict, word):
	for l in dict:
		if l.startswith(word):
			yield l
	
if __name__ == "__main__":
	word = "de"
	assert list(autocomplete(['dog', 'deer', 'deal'], word)) == ['deer', 'deal']