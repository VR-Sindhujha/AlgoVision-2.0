import heapq


class DijkstraEngine:

    def shortest_path(self, graph, start, end):

        distances = {

            node: float('inf')

            for node in graph
        }

        distances[start] = 0

        priority_queue = [

            (0, start)
        ]

        previous_nodes = {}

        while priority_queue:

            current_distance, current_node = heapq.heappop(

                priority_queue
            )

            if current_node == end:

                break

            for neighbor, weight in graph.get(

                current_node,
                []
            ):

                distance = current_distance + weight

                if distance < distances.get(

                    neighbor,
                    float('inf')
                ):

                    distances[neighbor] = distance

                    previous_nodes[neighbor] = current_node

                    heapq.heappush(

                        priority_queue,

                        (distance, neighbor)
                    )

        path = []

        current = end

        while current in previous_nodes:

            path.insert(0, current)

            current = previous_nodes[current]

        path.insert(0, start)

        return path, distances[end]