# Ունենք ամբողջ թվերից բաղկացած մատրից, որի վրա պետք է իրականացնել transpose։ Transpose կատարել
# նշանակում է մատրիցի տողերը փոխադրել սյուներով:

ls = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
ls2 = []


for i in range(len(ls[0])):
	row = []
	for j in range(len(ls)):
		row.append(ls[j][i])
	ls2.append(row)
print(ls2)
