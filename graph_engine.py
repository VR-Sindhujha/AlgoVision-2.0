class GraphEngine:

    def __init__(self):

        self.graph = {}


    def add_edge(self, source, destination, distance):

        if source not in self.graph:

            self.graph[source] = []

        self.graph[source].append(

            (destination, distance)

        )


    def get_graph(self):

        return self.graph