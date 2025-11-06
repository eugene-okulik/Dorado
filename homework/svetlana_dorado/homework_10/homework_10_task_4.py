PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''


def parse_line(line):
    name, price = line.split()
    price = price.replace('р', '')
    return name, int(price)


lines = PRICE_LIST.split('\n')

parsed_data = [parse_line(line) for line in lines]

price_dict = {name: price for name, price in parsed_data}

print(price_dict)
