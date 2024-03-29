import os


def read_file(filename, products):
	with open(filename, 'r', encoding='utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue
			name, price = line.strip().split(',')
			products.append([name, price])
	return products


def user_input(products):
	while True:
		name = input('請輸入商品名稱: ')
		if name == 'q':
			break
		price = input('請輸入價格: ')
		products.append([name, price])
	return products	


def print_products(products):
	for p in products:
		print(p[0], '的價格是', p[1])


def write_file(products, filename):
	with open(filename, 'w', encoding='utf-8') as f:
		f.write('商品,價格\n')
		for p in products:
			f.write(p[0] + ',' + p[1] + '\n')


def main(filename):
	products = []
	if os.path.isfile(filename):
		print('yeah! 找到檔案')
		products = read_file(filename, products)
	else:
		print('沒有找到.....')
	products = user_input(products)
	print_products(products)
	write_file(products, filename)

main('products2.csv')
