class Item:
    cost_increment = 0.05

    def __init__(self, name="", cost=0.0, price=0.0, vendor="", weight=1.0, taxable: bool = True) -> None:
        self.name = name
        self.cost = round(cost, 2)
        self.price = round(price, 2)
        self.vendor = vendor
        self.weight = round(weight, 2)
        self.taxable = taxable

    def increase_cost(self):
        self.cost = self.cost + self.cost * Item.cost_increment

    def profit(self):
        return self.price - self.cost

    def __str__(self) -> str:
        return f"{self.name}, {self.cost}, {self.price}"


class ShopingCart:
    GST = 1.17

    def __init__(self, items: list = []) -> None:
        self.items = items

    def addItem(self, item: Item):
        self.items.append(item)

    def __str__(self) -> str:
        return f"{self.get_receipt()}"

    def get_receipt(self):
        recipt = []
        for i in self.items:
            item = {}
            item['name'] = i[0].name
            item['price'] = i[0].price
            item['Quantity'] = i[1]
            item['Tax'] = ShopingCart.GST if i[0].taxable else 0
            item['Total'] = round((i[0].price * i[1]) * item['Tax'], 2)
            recipt.append(item)
        return recipt

    def cart_total(self):
        total = 0
        for i in self.items:
            total += (i[0].price * i[1]) * \
                ShopingCart.GST if i[0].taxable else 0
        return total

    def cartTaxAmount(self, tax):
        total = 0
        for i in self.items:
            total += round((i[0].price * i[1]) *
                           tax if i[0].taxable else (i[0].price * i[1]), 2)
        return total


# -------------- Phase 1 --------------
chair = Item("Desk Chair", 30, 55)
# increase cost 3 times, due to inflation.
chair.increase_cost()
chair.increase_cost()
chair.increase_cost()
# //display the profit
# print("The chair’s profit is now ", chair.profit())
# set the chair’s weight to 7 lb
chair.weight = 7
table = Item("Picnic Table", 70, 88)
# print("The table’s profit is now ", table.profit())

# -------------- Phase 2 --------------


# def get_details(items):
#     total_weight = 0
#     highest_price = None
#     count_taxable = 0
#     for i in items:
#         total_weight += i.weight
#         highest_price = i.price if highest_price == None else i.price if highest_price < i.price else highest_price
#         count_taxable += 1 if i.taxable else 0
#     return (total_weight, highest_price, count_taxable)


# print(chair)
# items = [chair, table]
# print(get_details(items))

# -------------- Phase 3 --------------
items = [(chair, 2), (table, 3)]
cart1 = ShopingCart(items=items)
print(cart1.get_receipt())
print("Cart Total: ", cart1.cart_total())
print("Total Tax Amount: ", cart1.cartTaxAmount(0.17))
