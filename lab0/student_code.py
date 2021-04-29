def order(data):
	final = []

	while len(data)>0:
		min = 100000
		index = -1
		for i in range(len(data)):
			if min > data[i]:
				min = data[i]
				index = i
		data.pop(index)
		final.append(min)
	print("FINAL")
	print(final)

	return final
