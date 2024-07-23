# Գրել ծրագիր, որը քառակուսային մատրիցը շրջում է 180 աստիճան։

ls = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

ls2 = []
for i in range(len(ls) - 1, -1, -1):
	row = []
	for j in range(len(ls) - 1, -1, -1):
		row.append(ls[i][j])
	ls2.append(row)

for i in ls2:
	print(i)
