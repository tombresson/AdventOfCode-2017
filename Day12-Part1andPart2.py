from typing import List
import re


class Program(object):
    def __init__(self, id):
        self.id = id
        self.connections: List[Program] = []


def traverse_graph(node: Program, visited_nodes: List[str]):
    for x in node.connections:
        x: Program = x
        if x not in visited_nodes:
            visited_nodes.append(x)
            traverse_graph(x, visited_nodes)

def main():
    prgms: List[Program] = []

    data_file = open("Data/Day12_data.txt", "r")

    # Populate prgm list
    for line in data_file:
        tokens = re.findall(r'(\w+)', line)
        prgm = Program(tokens[0])

        # Add prgm to list
        prgms.append(prgm)

    # Reset file position to beginning
    data_file.seek(0)

    # Populate all prgms connections
    for line in data_file:
        tokens = re.findall(r'(\w+)', line)

        # Get the relevent prgm
        # this works since the array idx is the same as the read value
        prgm = prgms[int(tokens[0])]

        if len(tokens) > 1:
            # Iterate through the prgms connections
            for token in tokens[1:]:

                # Append the connection to the prgm
                prgm.connections.append(prgms[int(token)])

    # Find nodes connected to zero
    nodes_connected_to_zero = []
    traverse_graph(prgms[0], nodes_connected_to_zero)

    # Find number of groups
    node_groups: List[List] = []
    for node in prgms:
        node_found = False;
        for node_list in node_groups:
            if node in node_list:
                node_found = True

        # If the node is not in a list of nodes yet
        # Add a new list and traverse the graph starting at that node
        if not node_found:
            new_list = []
            node_groups.append(new_list)
            traverse_graph(node, new_list)


    print(len(nodes_connected_to_zero))
    print(len(node_groups))



if __name__ == "__main__":
    main()