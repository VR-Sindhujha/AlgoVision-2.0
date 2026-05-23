import heapq


class HeapEngine:

    def __init__(self):

        self.heap = []


    def add_order(

        self,
        priority,
        timestamp,
        product

    ):

        heapq.heappush(

            self.heap,

            (
                -priority,
                timestamp,
                product
            )
        )


    def get_highest_priority(self):

        if self.heap:

            return self.heap[0]

        return None


    def dispatch_order(self):

        if self.heap:

            return heapq.heappop(self.heap)

        return None


    def get_all_orders(self):

        return self.heap