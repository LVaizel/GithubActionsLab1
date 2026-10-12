def calculateTotal(_price, _quantity):
    return _price * _quantity

PRICE = 25
QUANTITY = 4
TOTAL = calculateTotal(PRICE, QUANTITY)

print(f"Price: ${PRICE}")
print(f"Quantity: {QUANTITY}")
print(f"Total: ${TOTAL}")
