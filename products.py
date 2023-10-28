products = []
with open('products.csv', 'r', encoding='utf-8') as f:
	for line in f:
		name, price = line.strip().split(',')
		products.append([name, price])
print(products)

while True:
	name = input('輸入商品名稱:')
	if name == 'q':
		break
	price = input('輸入商品價格:')
	products.append([name, price])
print(products)

for p in products:
	print(p[0], '的價格是', p[1])

with open('products.csv', 'w', encoding = 'utf-8') as f:
	f.write('商品,價格' + '\n')
	for d in products:
		f.write(p[0] + ',' + p[1] + '\n')