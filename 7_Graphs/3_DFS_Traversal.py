# Using Adjacency List

def add_node(node):
    if node in graph:
        print(node, "is already present in the graph")
    else:
        # Adding node with key and val to dictionary
        graph[node] = []


def add_edge_undirected(node1, node2, cost=None):
    if node1 not in graph:
        print(node1, "is not present in the graph")
    elif node2 not in graph:
        print(node2, "is not present in the graph")
    else:
        if cost:
            node1Connections = [node2, cost]
            node2Connections = [node1, cost]
            graph[node1].append(node1Connections)
            graph[node2].append(node2Connections)
        else:
            graph[node1].append(node2)
            graph[node2].append(node1)


def DFS_Recursion(node, visitedNodes, graph):
    # Visit Starting Node (A)
    # Search Adjacent Node of A
    # Visit the one of the unvisted node of A (B)
    # Keep Digging and repeating the above steps

    # Checking if node is is present in graph
    if node not in graph:
        print("Node is not present in graph")
        return

    # Checking if node is already visited
    if node not in visitedNodes:
        print(node)
        visitedNodes.add(node)  # Adding node to visited Node

        # Getting all the adjacent nodes of a partular Node
        # A: [B,C,D]
        for nodeAdjacency in graph[node]:
            # Recursively calling for all the nodes
            DFS_Recursion(nodeAdjacency, visitedNodes, graph)
            # DFS(i[0], visitedNodes, graph)  If using Undirected Weighted Graph


def DFS_Iterative(node, graph):
    visitedNodes = set()

    # Checking if node is present in graph
    if node not in graph:
        print("Node is not present in graph")
        return

    # Using Stack to implement DFS
    # Push Starting Node to Stack
    # Pop Starting Node
    # Check if the node is visited
    # If not visited, visit(Print) and add it in visted nodes(set)
    # Add adjacent nodes of element to stack and repeat above steps until stack becomes empty

    stack = []
    stack.append(node)
    while stack:
        currentNode = stack.pop()
        if currentNode not in visitedNodes:
            print(currentNode)
            visitedNodes.add(currentNode)

            for nodeAdjacency in graph[currentNode]:
                stack.append(nodeAdjacency)


visitedNodes = set()
graph = {}


print("Before Adding Nodes")
print(graph)
add_node("A")
add_node("B")
add_node("C")
add_node("D")
add_node("E")

add_edge_undirected("A", "B")
add_edge_undirected("B", "E")
add_edge_undirected("A", "C")
add_edge_undirected("A", "D")
add_edge_undirected("B", "D")
add_edge_undirected("C", "D")
add_edge_undirected("E", "D")
print(graph)

print("\nVisiting all the nodes using DFS_Recursion\n")
DFS_Recursion("B", visitedNodes, graph)

print("\nVisiting all the nodes using DFS_Iterative")
DFS_Iterative("B", graph)
