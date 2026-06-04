#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self._discount = 0
        self.discount = discount
        self.total = 0
        self.items = []
        self.previous_transactions = []

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        if isinstance(value, int) and 0 <= value <= 100:
            self._discount = value
        else:
            print("Not valid discount")
            self._discount = 0

    def add_item(self, item, price, quantity=1):
        transaction_amount = price * quantity
        self.total += transaction_amount
        self.previous_transactions.append({
            "item": item,
            "price": price,
            "quantity": quantity,
        })
        for _ in range(quantity):
            self.items.append(item)

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = (self.discount / 100) * self.total
            self.total -= discount_amount
            formatted_total = self._format_total(self.total)
            print(f"After the discount, the total comes to ${formatted_total}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        if not self.previous_transactions:
            print("There is no transaction to void.")
            return

        last_transaction = self.previous_transactions.pop()
        amount = last_transaction["price"] * last_transaction["quantity"]
        self.total -= amount
        self.total = max(self.total, 0)

        item = last_transaction["item"]
        quantity = last_transaction["quantity"]
        while quantity > 0 and self.items:
            for index in range(len(self.items) - 1, -1, -1):
                if self.items[index] == item:
                    self.items.pop(index)
                    quantity -= 1
                    break
            else:
                break

    @staticmethod
    def _format_total(amount):
        if amount == int(amount):
            return str(int(amount))
        return f"{amount:.2f}"
