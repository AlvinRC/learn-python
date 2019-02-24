def prettify(value, count=5):
    deco = '~' * count
    return deco + str(value) + deco

if __name__ == '__main__':
    print(prettify(123))
    print(prettify(1.4142, 2))
    print(prettify('hello!', 0))
