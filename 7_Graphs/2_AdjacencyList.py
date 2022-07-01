def add_node(node):
    if node in graph:
        print(node, "is already present in the graph")
    else:
        # Adding node with key and val to dictionary
        graph[node] = []


def add_edge_directed(node1, node2, cost=None):
    if node1 not in graph:
        print(node1, "is not present in the graph")
    elif node2 not in graph:
        print(node2, "is not present in the graph")
    else:
        if cost:
            # Adding Adjacency nodes with cost to dictionary
            # "A" : ["B",5]
            node1Connections = [node2, cost]
            graph[node1].append(node1Connections)
        else:
            # Adding Adjacency nodes to dictionary
            # "A" : ["B"]
            node1Connections = [node2]
            graph[node1].append(node1Connections)


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
            node1Connections = [node2]
            node2Connections = [node1]
            graph[node1].append(node1Connections)
            graph[node2].append(node2Connections)


def delete_node(node, cost=None):
    if node not in graph:
        print(node, "is not present in the graph ")
    else:
        # Deleting the node from the dictionary/graph
        graph.pop(node)

        # Delete that node from all other nodes
        for keyNode in graph:
            # Getting the value of each key and storing it as list
            connectedNodes = graph[keyNode]
            if cost:
                # Inner List : [[B,5],[C,78]]
                for nodeWithCost in connectedNodes:
                    # nodeCost[0] is B/C/D
                    # nodeCost[1] is 45/89/78 (costs)
                    # Checking if node present in 0th pos
                    if node == nodeWithCost[0]:
                        connectedNodes.remove(nodeWithCost)
            else:
                # Checking if node is present in above list
                if node in connectedNodes:
                    connectedNodes.remove(node)


def delete_edge_undirected(node1, node2, cost=None):
    if node1 not in graph:
        print(node1, "is not present in the graph")
    elif node2 not in graph:
        print(node2, "is not present in the graph")
    else:
        if cost:
            # If there is an edge between A to D with cost 5
            # We are taking list as
            # temp1 = A,5
            # temp2 = D,5
            # Checking if [D,5] is present in graph[A]
            # Removing [D,5] from A
            # Removing [A,5] from D
            temp1 = [node1, cost]
            temp2 = [node2, cost]
            if temp2 in graph[node1]:
                graph[node1].remove(temp2)
                graph[node2].remove(temp1)
        else:

            # Checking if there is adjacency or  having an edge between them
            if node2 in graph[node1]:
                # Removing Values(adjacency) from both keys(nodes)
                graph[node1].remove(node2)
                graph[node2].remove(node1)


def delete_edge_directed(node1, node2, cost=None):
    if node1 not in graph:
        print(node1, "is not present in the graph")
    elif node2 not in graph:
        print(node2, "is not present in the graph")
    else:
        if cost:
            # If there is an edge between A to D with cost 5
            # We are taking list as
            # temp2 = D,5
            # Checking if [D,5] is present in graph[A]
            # Removing [D,5] from A
            temp2 = [node2, cost]
            if temp2 in graph[node1]:
                graph[node1].remove(temp2)
        else:
            # Checking if there is adjacency or  having an edge between them
            if node2 in graph[node1]:
                # Removing Value(adjacency) from key(node)
                graph[node1].remove(node2)


graph = {}
print("Before Adding Nodes")
print(graph)

print()
print("After Adding Nodes")
add_node("A")
add_node("A")
add_node("C")
add_node("D")
add_node("E")
print(graph)

# Adding Undirected Weighted and Unweighted Edges
add_edge_undirected("A", "E")
add_edge_undirected("A", "D", 45)

# Adding Directed Weighted and Unweighted Edges
add_edge_directed("D", "C")
add_edge_directed("D", "C", "78")

print()
print("After Adding Edges")
print(graph)


# Deleting Node
delete_node("A")
print(graph)
delete_node("C", 78)

print()
print("After Deleting Node")
print(graph)
