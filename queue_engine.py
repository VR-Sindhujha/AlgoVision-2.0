from collections import deque


class QueueEngine:

    def __init__(self):

        self.queue = deque()


    def enqueue(self, product, timestamp):

        self.queue.append(

            (product, timestamp)

        )


    def dequeue(self):

        if self.queue:

            return self.queue.popleft()

        return None


    def get_queue(self):

        return list(self.queue)