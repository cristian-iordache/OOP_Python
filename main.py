import csv


class Item:
    pay_rate = 0.8  # the pay rate after 20% discount
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the received arguments
        assert price >= 0, f'Price {price} is not greater than 0.'
        assert quantity >= 0, f'Quantity {quantity} is not greater than 0.'

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod  # decorator - change the behavior
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

            for item in items:
                Item(
                    name=item.get('name'),
                    price=float(item.get('price')),
                    quantity=int(item.get('quantity'))
                )

    @staticmethod
    def is_integer(num):
        # We will count out the floats that are point zero
        # For i.e: 5.0, 10.0
        if isinstance(num, float):
            # Count out the floarts that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"


# item1 = Item('Phone', 100, 1)
# # item1.apply_discount()
# # print(item1.price)

# item2 = Item('Laptop', 1000, 3)
# # item2.pay_rate = 0.7
# # item2.apply_discount()
# # print(item2.price)

# # print(Item.__dict__)  # All the atributes for Class level
# # print(item1.__dict__)  # all the atributes for instance level
# item3 = Item("Phone", 10, 5)
# item4 = Item("Mouse", 50, 5)
# item5 = Item("Keyboard", 75, 5)

# print(Item.all)
# Item.instantiate_from_csv()
# print(Item.all)

# print(Item.is_integer(7.0))

class Phone(Item):
    pass


phone1 = Phone("jscPhonev10", 500, 5)
phone1.broken_phones = 1
phone2 = Phone("jscPhonev20", 700, 5)
phone2.broken_phones = 1
