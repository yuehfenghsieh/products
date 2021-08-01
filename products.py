import os

#讀取檔案
def read_file(filename):
	products = []
	with open(filename, 'r', encoding='utf-8') as f:
		for line in f:
			if '商品, 價格' in line:
				continue
			name, price = line.strip().split(',')
			products.append([name, price])
	print(products)
	return products

#使用者輸入
def user_input(products):
	while True:
		name = input('輸入商品名稱')
		if name == 'q':
			break
		price = input('輸入商品價格')
		products.append([name, price])
	print(products)
	return products

#列印購買紀錄
def file_print(products):
	for p in products:
		print(p[0], '的價格是', p[1])

#寫入檔案
def file_write(filename,products):
	with open(filename, 'w', encoding='utf-8') as f:
		f.write('商品, 價格\n')
		for p in products:
			f.write(p[0] + ',' + p[1] + '\n')

def main():
	filename = 'products.csv'
	if os.path.isfile(filename):
		print('找到檔案')
		products = read_file(filename)
		products = user_input(products)
		file_print(products)
		file_write(filename,products)
	else:
		print('檔案不存在')
main()