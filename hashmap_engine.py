class HashMapEngine:

    def __init__(self):

        self.orders = {}


    def add_order(self, order_id, order_data):

        self.orders[order_id] = order_data


    def get_order(self, order_id):

        return self.orders.get(order_id)

    def get_all_orders(self):

        return self.orders