def add_node(node):
    # Adding global because nodeCount is defined outside the function
    global nodeCount

    if node in nodesList:
        print(node, "is already present in the graph")
    else:
        # Increment Node Count
        nodeCount = nodeCount + 1
        # Add Node in nodeList
        nodesList.append(node)

        # Add a column for this node and insert zero to all cells
        for row in graph:   # Adding Zero to each row at last column
            row.append(0)

        # Adding additional Row
        additionalRow = []
        for col in range(nodeCount):  # Add 0 to all columns in the last row
            additionalRow.append(0)

        # Meging last added row with prev matrix
        graph.append(additionalRow)


def add_edge_undirected(node1, node2, cost=None):
    if node1 not in nodesList:
        print(node1, "is not present in the graph")
    elif node2 not in nodesList:
        print(node2, "is not present in the graph")
    else:
        # Since the nodes are stored in list
        # So we cant access the nodes directly, we get the index of nodes from list then proceed further
        index1 = nodesList.index(node1)
        index2 = nodesList.index(node2)

        # Replacing 0 to costVal where is there a edge from node1 to node2 and vice-versa
        if cost:
            graph[index1][index2] = cost
            graph[index2][index1] = cost
        else:
            # Replacing 0 to 1 where is there a edge from node1 to node2 and vice-versa
            graph[index1][index2] = 1
            graph[index2][index1] = 1


def add_edge_directed(node1, node2, cost=None):
    if node1 not in nodesList:
        print(node1, "is not present in the graph")
    elif node2 not in nodesList:
        print(node2, "is not present in the graph")
    else:
        # Since the nodes are stored in list
        # We cant access the nodes directly, we get the index of nodes from list & then proceed further
        index1 = nodesList.index(node1)
        index2 = nodesList.index(node2)

        # Replacing 0 to costval where there is a edge from node1 to node2
        if cost:
            graph[index1][index2] = cost
        else:
            # Replacing 0 to 1 where is there a edge from node1 to node2
            graph[index1][index2] = 1


def delete_node(node):
    global nodeCount
    if node not in nodesList:
        print(node, "is not present in the graph")
    else:
        # Get the index value of the node from nodeList
        nodeIndex = nodesList.index(node)

        # Decrement NodeCount
        nodeCount -= 1

        # Deleting node from nodesList
        nodesList.remove(node)

        # Delete row and col from adjacency matrix for the given node
        # Deleting Row
        graph.pop(nodeIndex)
        # Deleting that node's col from all rows like remove 3rd column from all rows
        for row in graph:
            row.pop(nodeIndex)


def delete_edge_undirected(node1, node2):
    if node1 not in nodesList:
        print(node1, "is not present in the graph")
    elif node2 not in nodesList:
        print(node2, "is not present in the graph")
    else:
        # Getting index of given 2 nodes
        node1Index = nodesList.index(node1)
        node2Index = nodesList.index(node2)

        # Replacing graph[node1][node2] = 1 to graph[node1][node2] = 0
        # Also for [node2][node1]
        graph[node1Index][node2Index] = 0
        graph[node2Index][node1Index] = 0


def delete_edge_directed(node1, node2):
    if node1 not in nodesList:
        print(node1, "is not present in the graph")
    elif node2 not in nodesList:
        print(node2, "is not present in the graph")
    else:
        # Getting index of given 2 nodes
        node1Index = nodesList.index(node1)
        node2Index = nodesList.index(node2)

        # Replacing graph[node1][node2] = cost to graph[node1][node2] = 0
        graph[node1Index][node2Index] = 0


def print_graph():
    for row in range(nodeCount):
        for col in range(nodeCount):
            print(format(graph[row][col], "<3"), end=" ")
        print()


nodesList = []
graph = []
nodeCount = 0

# Printing Statements before Onserting Nodes & Edges
print("Before Adding Nodes")
print("Nodes Present in the Graph", nodesList)
print("Adjacency Matrix")
print_graph()
print()

# Inserting Nodes
add_node("A")
add_node("A")
add_node("B")
add_node("D")
add_node("C")

# Adding Undirected Edges for weighted and unWeighted
add_edge_undirected("A", "C")
add_edge_undirected("A", "B", 45)
add_edge_undirected("B", "D", 78)

# Adding Directed Edges for weighted and unWeighted
add_edge_directed("A", "D")
add_edge_directed("D", "C", 83)

# Printing after inserting nodes & edges
print("After Adding Nodes")
print("Nodes Present in the Graph", nodesList)
print("Adjacency Matrix")
print(nodesList)
print_graph()


# Printing after deleting node
delete_node("A")
print("\nGraph After Deleting the Node")
print(nodesList)
print_graph()

# Removing Undirected & Directed Edge
delete_edge_directed("B", "D")
delete_edge_undirected("D", "C")

# Printing after deleting Edges
print()
print("Printing after deleting Edges")
print(nodesList)
print_graph()
