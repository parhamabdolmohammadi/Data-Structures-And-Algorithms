
from numbers import Number
import sys
import heapq

from linked_list import LinkedList


class IllegalStateException(Exception):
    pass


class WeightedGraph:

    class Node:
        def __init__(self, word):
            self.__word = word

        def get_label(self):
            return self.__word

        def __str__(self):
            return self.__word

        def __repr__(self):
            return self.__word

        def __eq__(self, other):
            return isinstance(other, WeightedGraph.Node) and self.__word == other.__word

        def __hash__(self):
            return hash(self.__word)

    class Edge:
        def __init__(self, fromm, to, weight):
            self.__from_node = fromm
            self.__to_node = to
            self.__weight = weight

        def get_from_node(self):
            return self.__from_node

        def get_to_node(self):
            return self.__to_node

        def get_weight(self):
            return self.__weight

        def __str__(self):
            return f"{self.__from_node.get_label()} -> ({self.__to_node.get_label()})"

        def __eq__(self, other):
            return isinstance(other, WeightedGraph.Edge) and self.__from_node == other.__from_node and self.__to_node == other.__to_node and self.__weight == other.__weight

    def __init__(self):
        self.__nodes: dict[str, "WeightedGraph.Node"] = {}
        self.__adjacency_list: dict["WeightedGraph.Node",
                                    list: "WeightedGraph.Edge"] = {}

        # -----------------------------------------------------------
    # Add Node
    #
    # Average Time Complexity: O(1)
    # Worst Case Time Complexity: O(V)
    #
    # Space Complexity: O(1)
    #
    # Reason:
    #   - Dictionary insertion is average constant time.
    #   - Worst-case occurs during heavy hash collisions.
    # -----------------------------------------------------------
    def add_node(self, label):
        if label not in self.__nodes:
            node = WeightedGraph.Node(label)

            self.__nodes[label] = node
            self.__adjacency_list[node] = []

        # -----------------------------------------------------------
    # Add Edge
    #
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    #
    # Reason:
    #   - Appending to adjacency lists is constant time.
    #   - Since graph is undirected, two edges are added.
    # -----------------------------------------------------------
    def add_edge(self, fromm: str, to: str, weight: Number):
        from_node, to_node = self.get_from_and_to_node(fromm, to)

        self.__adjacency_list[from_node].append(
            WeightedGraph.Edge(from_node, to_node, weight))

        self.__adjacency_list[to_node].append(
            WeightedGraph.Edge(to_node, from_node, weight))

    def get_from_and_to_node(self, fromm, to):
        from_node = self.__nodes.get(fromm)
        to_node = self.__nodes.get(to)

        if not from_node and not to_node:
            raise IllegalStateException(
                f"Nodes {fromm} and {to} dont exist"
            )

        if not from_node:
            raise IllegalStateException(
                f"Node {fromm} doesnt exist"
            )

        if not to_node:
            raise IllegalStateException(
                f"Node {to} doesnt exist"
            )

        return from_node, to_node

    def get_shortest_path(self, fromm, to):
        """
        Return the shortest path from one node to another
        using Dijkstra's algorithm.

        Time Complexity:
            O((V + E) log V)

        Space Complexity:
            O(V + E)
        """
        distance, previous = self.__dijkstra(fromm, to)

        from_node, to_node = self.get_from_and_to_node(fromm, to)

        if distance == sys.maxsize:
            return None

        path = []
        current = to_node

        while current is not None:
            path.append(current.get_label())

            if current == from_node:
                break

            current = previous[current]

        path.reverse()

        return "->".join(path)

    def get_shortest_distance(self, fromm, to):
        """
        Return the shortest distance between two nodes.

        Time Complexity:
            O((V + E) log V)

        Space Complexity:
            O(V + E)
        """
        distance, _ = self.__dijkstra(fromm, to)

        return distance

    def __dijkstra(self, fromm, to):
        """
        Dijkstra's shortest path algorithm using a min-heap.

        Time Complexity:
            O((V + E) log V)

        Space Complexity:
            O(V + E)
        """

        from_node, to_node = self.get_from_and_to_node(
            fromm,
            to
        )

        # Shortest known distance to every node
        distances = {
            node: sys.maxsize
            for node in self.__nodes.values()
        }

        # Previous node in shortest path
        previous = {
            node: None
            for node in self.__nodes.values()
        }

        distances[from_node] = 0

        # (distance, label, node)
        #
        # label is used only as a tie-breaker when
        # two nodes have the same distance.
        min_heap = [
            (
                0,
                from_node.get_label().lower(),
                from_node
            )
        ]

        visited = set()

        while min_heap:

            current_distance, _, current_node = heapq.heappop(
                min_heap
            )

            # Node already completely processed
            if current_node in visited:
                continue

            visited.add(current_node)

            # We reached the destination.
            # No need to continue.
            if current_node == to_node:
                break

            for edge in self.__adjacency_list[current_node]:

                neighbor = edge.get_to_node()
                weight = edge.get_weight()

                if neighbor in visited:
                    continue

                new_distance = (
                    current_distance + weight
                )

                # Relax edge
                if new_distance < distances[neighbor]:

                    distances[neighbor] = new_distance
                    previous[neighbor] = current_node

                    heapq.heappush(
                        min_heap,
                        (
                            new_distance,
                            neighbor.get_label().lower(),
                            neighbor
                        )
                    )

        return distances[to_node], previous

        # -----------------------------------------------------------
    # DFS Cycle Detection (Undirected Graph)
    #
    # General Algorithm Complexity:
    #   Time  Complexity: O(V + E)
    #   Space Complexity: O(V)
    #
    # My Implementation Complexity:
    #   Time  Complexity: O(V + E)
    #   Space Complexity: O(V)
    #
    # Reason:
    #   - Each node is visited once.
    #   - Each edge is processed once/twice.
    #   - Visiting/visited sets and recursion stack
    #     require additional O(V) space.
    #
    # V = number of vertices
    # E = number of edges
    # -----------------------------------------------------------

    def has_cycle(self):
        visiting = set()
        visited = set()

        for node in self.__nodes.values():
            if node in visited:
                continue

            if self.__has_cycle(node, visiting, visited):
                return True

        return False

    def __has_cycle(self, node, visiting, visited, parent=None):
        visiting.add(node)

        for neighbor in self.__adjacency_list[node]:

            neighbor_node = neighbor.get_to_node()

            if neighbor_node == parent:
                continue

            if neighbor_node in visited:
                continue

            if neighbor_node in visiting:
                return True

            if self.__has_cycle(neighbor_node, visiting, visited, node):
                return True

        visiting.remove(node)
        visited.add(node)

        return False

        # -----------------------------------------------------------
    # Prim Minimum Spanning Tree Algorithm
    #
    # General Algorithm Complexity:
    #   Using Priority Queue (Heap):
    #       Time  Complexity: O((V + E) log V)
    #       Space Complexity: O(V + E)
    #
    # My Implementation Complexity:
    #   Time  Complexity: O(VE)
    #   Worst Dense Graph Case: O(V^3)
    #   Space Complexity: O(V + E)
    #
    # Reason:
    #   - I use linear scans to find the minimum edge.
    #   - Available edges are stored in a list instead of
    #     a priority queue.
    #   - Edge existence checks inside lists are linear.
    #
    # V = number of vertices
    # E = number of edges
    # -----------------------------------------------------------
    def min_span_tree(self):
        random_node = None

        try:
            random_node = next(iter(self.__nodes.values()))
        except StopIteration:
            print("Graph is Empty")

        list_of_unvisited_nodes = list(self.__nodes.values())
        list_of_visited_nodes = list()
        list_of_available_edges = list()
        list_of_picked_edges = list()

        self.__add_to_available_edges(random_node, list_of_available_edges)

        self.__min_span_tree_prim(
            random_node, list_of_visited_nodes, list_of_unvisited_nodes, list_of_available_edges, list_of_picked_edges)

    def __min_span_tree_prim(
            self, random_node, list_of_visited_nodes, list_of_unvisited_nodes, list_of_available_edges, list_of_picked_edges):

        list_of_unvisited_nodes.remove(random_node)
        list_of_visited_nodes.append(random_node)

        min_weight = sys.maxsize
        picked_edge = None

        for edge in list_of_available_edges:
            if edge.get_to_node() not in list_of_visited_nodes and edge.get_weight() < min_weight:
                min_weight = edge.get_weight()
                picked_edge = edge

        # disconnection
        if not picked_edge:

            if list_of_unvisited_nodes:
                # disconnection happened
                print("The graph is not connected")
            else:
                string = ""

                for edge in list_of_picked_edges:
                    string += str(edge)
                    string += " | "

                print(string[:len(string) - 3])
            return

        list_of_picked_edges.append(picked_edge)
        list_of_available_edges.remove(picked_edge)
        random_node = picked_edge.get_to_node()
        self.__add_to_available_edges(random_node, list_of_available_edges)

        self.__min_span_tree_prim(
            random_node,
            list_of_visited_nodes,
            list_of_unvisited_nodes,
            list_of_available_edges,
            list_of_picked_edges
        )

        # -----------------------------------------------------------
    # Add Candidate Edges for Prim's Algorithm
    #
    # Current Time Complexity:
    #   O(E) for iteration
    #   O(E) membership checks
    #
    # Overall Worst Case Contribution:
    #   O(E^2)
    #
    # Reason:
    #   - "edge not in list" performs linear search.
    #   - Using a set would improve membership checks
    #     to approximately O(1).
    # -----------------------------------------------------------
    def __add_to_available_edges(self, random_node, list_of_available_edges):
        for edge in self.__adjacency_list[random_node]:
            if edge not in list_of_available_edges:
                list_of_available_edges.append(edge)

    def min_span_tree_general(self):
        # General Prim with Priority Queue
        #
        # Time Complexity: O((V + E) log E)
        # Usually written as: O(E log V)
        #
        # Space Complexity: O(V + E)
        #
        # Reason:
        #   - Each edge may be pushed into the heap.
        #   - Heap push/pop costs O(log E).
        #   - visited stores up to V nodes.
        #   - mst_edges stores V - 1 edges.

        if not self.__nodes:
            print("Graph is Empty")
            return []

        start_node = next(iter(self.__nodes.values()))

        visited = set()
        min_heap = []
        mst_edges = []

        visited.add(start_node)

        # Add all edges from starting node
        for edge in self.__adjacency_list[start_node]:
            heapq.heappush(
                min_heap,
                (edge.get_weight(), edge.get_to_node().get_label(), edge)
            )

        while min_heap and len(visited) < len(self.__nodes):
            weight, _, edge = heapq.heappop(min_heap)

            to_node = edge.get_to_node()

            if to_node in visited:
                continue

            mst_edges.append(edge)
            visited.add(to_node)

            for next_edge in self.__adjacency_list[to_node]:
                if next_edge.get_to_node() not in visited:
                    heapq.heappush(
                        min_heap,
                        (
                            next_edge.get_weight(),
                            next_edge.get_to_node().get_label(),
                            next_edge
                        )
                    )

        if len(visited) != len(self.__nodes):
            print("The graph is not connected")
            return []

        for edge in mst_edges:
            print(edge)

        return mst_edges


if __name__ == "__main__":

    graph = WeightedGraph()
    graph.add_node("A")
    graph.add_node("B")
    graph.add_node("C")
    graph.add_node("D")
    graph.add_node("E")
    graph.add_edge("A", "D", 2)
    graph.add_edge("A", "B", 3)
    graph.add_edge("A", "C", 4)
    graph.add_edge("B", "D", 6)
    graph.add_edge("B", "E", 1)
    graph.add_edge("C", "D", 2)
    graph.add_edge("A", "D", 2)
    print(graph.get_shortest_distance("A", "E"))
    print(graph.get_shortest_path("A", "E"))
    graph.min_span_tree()
