class Checkout:
    class Discount:
        def __init__(self, nbr_items, price):
            self.nbr_items = nbr_items
            self.price = price

    def __init__(self):
        self.prices = {}
        self.discounts = {}
        self.items = {}  # count

    def add_discount(self, item, nbr_of_items, price):
        discount = Checkout.Discount(nbr_of_items, price)
        self.discounts[item] = discount

    def add_item_price(self, item, price):
        self.prices[item] = price

    def add_item(self, item):
        if item not in self.prices:
            raise Exception(f"Bad item: {item}")
        if item in self.items:
            self.items[item] += 1
        else:
            self.items[item] = 1

    def calculate_total(self):
        total = 0
        for item, cnt in self.items.items():
            total += self.calculate_item_total(item, cnt)
        return total

    def calculate_item_total(self, item, cnt):
        total = 0
        if item in self.discounts:
            discount = self.discounts[item]
            if cnt >= discount.nbr_items:
                total += self.calculate_item_discount_total(item, cnt, discount)
            else:
                total += self.prices[item] * cnt
        else:
            total += self.prices[item] * cnt
        return total

    def calculate_item_discount_total(self, item, cnt, discount):
        total = 0
        discounts_nbr = cnt // discount.nbr_items
        total += discounts_nbr * discount.price
        remaining = cnt % discount.nbr_items
        total += remaining * self.prices[item]
        return total
