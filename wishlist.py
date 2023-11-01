def wishlist():
    wish_list = {'hamza': {'Shoes', 'Watch'}, 'affan': {'Shoes', 'Watch', 'Laptops'}, 'ahmad': {'Bikes', 'Cars'}}
    name = str(input('Enter Your Name For Select: '))
    if name not in wish_list:
        print('Wrong Key')
        return

    wishlist_current = wish_list[name]
    print(f'{name}\'s current wish list: {wishlist_current}')

    item = input(str('Enter Your Item For Add: '))
    wish_list[name].add(item)
    print(f'{name}\'s updated wish list: {wish_list[name]}')
wishlist()
