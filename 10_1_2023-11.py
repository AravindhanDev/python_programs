def calculateBill(products):
    total = 0
    for product in products:
        total += product['quantity'] * product['mrp']
    return total

products = [
    {
        "name": "Pencil",
        "quantity": 2,
        "mrp": 10
    },
    {
        "name": "Ball point pen",
        "quantity": 3,
        "mrp": 15
    },
    {
        "name": "Ink pen",
        "quantity": 1,
        "mrp": 30
    },
    {
        "name": "Eraser",
        "quantity": 1,
        "mrp": 5
    }
]

print('Amount To Pay', calculateBill(products))

