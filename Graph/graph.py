import sys

from linked_list import LinkedList
from collections import deque


class IllegalStateException(Exception):
    pass


class Graph:

    class Node:

        def __init__(self, label):
            self.__label = label

        def get_label(self):
            return self.__label

        def __hash__(self):
            return hash(self.__label)

        def __eq__(self, other):
            return self.__label == other.__label

        def __str__(self):
            return f"{self.__label}"

        def __repr__(self):
            return self.__label

    def __init__(self):
        self.__nodes: dict[str, Graph.Node] = {}
        self.__adjacency_list: dict["Graph.Node", LinkedList] = {}

        # -----------------------------------------------------------
    # Add Node
    #
    # General Graph Complexity:
    #   Average Time Complexity: O(1)
    #   Worst Case Time Complexity: O(V)
    #
    # My Implementation Complexity:
    #   Average Time Complexity: O(1)
    #   Worst Case Time Complexity: O(V)
    #
    # Space Complexity: O(1)
    #
    # Reason:
    #   - Dictionary insertions are average constant time.
    #   - Worst case occurs because of hash collisions.
    #
    # V = number of vertices/nodes
    # -----------------------------------------------------------

    def add_node(self, label):
        node = Graph.Node(label)

        self.__nodes[label] = node
        self.__adjacency_list[node] = LinkedList()

        # -----------------------------------------------------------
    # Add Edge (Directed Graph)
    #
    # General Adjacency List Complexity:
    #   Time Complexity: O(1)
    #   Space Complexity: O(1)
    #
    # My Implementation Complexity:
    #   Time Complexity: O(1)
    #   Space Complexity: O(1)
    #
    # Reason:
    #   - Edge insertion appends a node into the adjacency list.
    #   - LinkedList add_last operation is constant time.
    # -----------------------------------------------------------

    def add_edge(self, fromm: str, to: str):
        from_node, to_node = self.get_from_and_to_node(fromm, to)

        self.__adjacency_list[from_node].add_last(to_node)

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

        # -----------------------------------------------------------
    # Remove Node
    #
    # General Adjacency List Complexity:
    #   Time Complexity: O(V + E)
    #   Space Complexity: O(1)
    #
    # My Implementation Complexity:
    #   Time Complexity: O(V + E)
    #   Space Complexity: O(1)
    #
    # Reason:
    #   - Must scan all adjacency lists to remove references
    #     to the target node.
    #   - Every edge may potentially be checked once.
    #
    # V = number of vertices
    # E = number of edges
    # -----------------------------------------------------------
    def remove_node(self, label):
        node = self.__nodes.get(label)

        if not node:
            raise IllegalStateException("Node doesnt exist")

        adj_list = self.__adjacency_list

        for current_node, neighbors in adj_list.items():
            if current_node == node:
                continue

            if neighbors.contains(node):
                self.remove_edge(current_node.get_label(), label)

        adj_list.pop(node)
        self.__nodes.pop(label)

        # -----------------------------------------------------------
    # Remove Edge
    #
    # General Adjacency List Complexity:
    #   Time Complexity: O(E)
    #   Space Complexity: O(1)
    #
    # My Implementation Complexity:
    #   Time Complexity: O(E)
    #   Space Complexity: O(1)
    #
    # Reason:
    #   - LinkedList removal requires traversal
    #     to locate the target node.
    # -----------------------------------------------------------
    def remove_edge(self, fromm, to):
        from_node, to_node = self.get_from_and_to_node(fromm, to)

        self.__adjacency_list[from_node].remove_value(to_node)

        # -----------------------------------------------------------
    # Recursive Depth First Search (DFS)
    #
    # General DFS Complexity:
    #   Time Complexity: O(V + E)
    #   Space Complexity: O(V)
    #
    # My Implementation Complexity:
    #   Time Complexity: O(V^2 + E)
    #   Space Complexity: O(V)
    #
    # Reason:
    #   - DFS traversal itself is O(V + E).
    #   - However, "node in visited_nodes" uses a list,
    #     producing linear membership checks.
    #   - Sorting neighbors also adds extra overhead.
    #
    # Better Optimization:
    #   - Use a set for visited nodes.
    #
    # V = number of vertices
    # E = number of edges
    # -----------------------------------------------------------

    def depth_first_traversal_recursive(self, label):
        """
        Perform recursive Depth-First Search starting from the given node.

        Args:
            label (str): Label of the starting node.

        Returns:
            list: Nodes in DFS traversal order.

        Time Complexity:
            Without sorting: O(V + E)

            With alphabetical neighbor sorting:
            O(V + E + sorting cost)

        Space Complexity:
            O(V)

            The visited set, result list, and recursive call stack
            can each contain up to V nodes.

        V = number of vertices
        E = number of edges
        """

        # Find the starting node.
        # Average dictionary lookup: O(1)
        current_node = self.__nodes.get(label)

        # Starting node does not exist.
        if not current_node:
            return []

        # Set gives average O(1) membership checking.
        visited = set()

        # Stores nodes in the order they are visited.
        result = []

        # Start recursive DFS.
        self.__dfs_recursive(
            current_node,
            visited,
            result
        )

        return result

    def __dfs_recursive(self, node, visited, result):
        """
        Recursive helper method for DFS.

        Time Complexity:
            Without sorting: O(V + E)

        Space Complexity:
            O(V) because of recursion and visited nodes.
        """

        # Mark the current node as visited.
        # Average: O(1)
        visited.add(node)

        # Save the node in traversal order.
        # Amortized: O(1)
        result.append(node)

        # Get all neighbors of the current node.
        neighbors = list(self.__adjacency_list[node])

        # Sort neighbors alphabetically by their labels.
        # This is optional and only controls traversal order.
        neighbors.sort(
            key=lambda n: n.get_label().lower()
        )

        # Visit each neighbor.
        for neighbor in neighbors:

            # Set membership check is average O(1).
            if neighbor not in visited:

                # Recursion acts as our DFS stack,
                # so we do NOT need a separate stack.
                self.__dfs_recursive(
                    neighbor,
                    visited,
                    result
                )

    def depth_first_traversal_iterative(self, label):
        """
        Iterative Depth-First Search.

        Time Complexity:
            O(V + E) without neighbor sorting.

        Space Complexity:
            O(V)
        """

        current_node = self.__nodes.get(label)

        if not current_node:
            return []

        stack = [current_node]
        visited = set()
        result = []

        while stack:
            cur_node = stack.pop()

            if cur_node in visited:
                continue

            visited.add(cur_node)
            result.append(cur_node)

            neighbors = list(self.__adjacency_list[cur_node])

            neighbors.sort(
                key=lambda n: n.get_label().lower()
            )

            # Reverse so alphabetically smaller nodes
            # are popped from the stack first.
            for neighbor in reversed(neighbors):
                if neighbor not in visited:
                    stack.append(neighbor)

        return result

    def breadth_first_traversal(self, label):
        """
        Breadth-First Search.

        Time Complexity:
            O(V + E) without neighbor sorting.

        Space Complexity:
            O(V)
        """

        current_node = self.__nodes.get(label)

        if not current_node:
            return []

        queue = deque([current_node])
        visited = set()
        result = []

        while queue:
            cur_node = queue.popleft()

            if cur_node in visited:
                continue

            visited.add(cur_node)
            result.append(cur_node)

            neighbors = list(self.__adjacency_list[cur_node])

            neighbors.sort(
                key=lambda n: n.get_label().lower()
            )

            for neighbor in neighbors:
                if neighbor not in visited:
                    queue.append(neighbor)

        return result
        # -----------------------------------------------------------
    # Topological Sort (DFS-Based)
    #
    # General Algorithm Complexity:
    #   Time Complexity: O(V + E)
    #   Space Complexity: O(V)
    #
    # My Implementation Complexity:
    #   Time Complexity: O(V + E)
    #   Space Complexity: O(V)
    #
    # Reason:
    #   - DFS visits every node once.
    #   - Every edge is processed once.
    #   - Stack and visited set require O(V) space.
    #
    # Requirement:
    #   - Graph must be acyclic (DAG).
    # -----------------------------------------------------------

    def topological_sort(self):

        if self.has_cycle():
            raise IllegalStateException(
                "Topological Sort Not possible the graph has cycle")

        visited = set()
        stack = []

        for node in self.__nodes.values():
            if node not in visited:
                self.__topological_sort(node, visited, stack)

        stack.reverse()
        return stack

    def __topological_sort(self, node, visited, stack):
        visited.add(node)

        neighbors = self.__adjacency_list[node]

        for neighbor in neighbors:
            if neighbor not in visited:
                self.__topological_sort(neighbor, visited, stack)

        # add AFTER visiting neighbors
        stack.append(node)

        # -----------------------------------------------------------
    # Cycle Detection (Directed Graph)
    #
    # General DFS Cycle Detection Complexity:
    #   Time Complexity: O(V + E)
    #   Space Complexity: O(V)
    #
    # My Implementation Complexity:
    #   Time Complexity: O(V + E)
    #   Space Complexity: O(V)
    #
    # Reason:
    #   - Each node is visited once.
    #   - Each edge is checked once.
    #   - visiting and visited sets require O(V) space.
    #
    # V = number of vertices
    # E = number of edges
    # -----------------------------------------------------------
    def has_cycle(self):
        visiting = set()
        visited = set()

        for node in self.__nodes.values():
            if node not in visited:
                if self.__has_cycle(node, visiting, visited):
                    return True

        return False

    def __has_cycle(self, node, visiting, visited):
        visiting.add(node)

        neighbors = self.__adjacency_list[node]

        for neighbor in neighbors:
            if neighbor in visited:
                continue

            if neighbor in visiting:
                return True

            if self.__has_cycle(neighbor, visiting, visited):
                return True

        visiting.remove(node)
        visited.add(node)

        return False


if __name__ == "__main__":
    graph = Graph()
    graph.add_node("A")
    graph.add_node("B")
    graph.add_node("C")
    graph.add_node("D")
    graph.add_node("E")
    graph.add_node("F")
    graph.add_edge("A", "B")
    graph.add_edge("A", "E")
    graph.add_edge("B", "E")
    graph.add_edge("C", "A")
    graph.add_edge("C", "B")
    graph.add_edge("C", "D")
    graph.add_edge("D", "E")
    print(graph.breadth_first_traversal("C"))
    print(graph.topological_sort())
