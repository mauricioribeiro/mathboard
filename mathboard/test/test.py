from mathboard.module import Term

if __name__ == '__main__':
    price = Term('Price', 100)
    discount = Term('Discount', 20)

    print(price)

    price = price - discount
    print(price)

    price.subtract(discount)
    print(price)

    price = price + 20
    print(price)

    price.add(1).add(2).subtract(discount)

    print(price.history())
    print(price)