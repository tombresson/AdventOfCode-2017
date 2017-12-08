import re

class Node(object):
    """Objects in a tree"""
    parent = None
    children = []

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def isLeaf(self):
        return len(self.children) == 0

    def isRoot(self):
        return self.parent == self

def main():
    tree = []

    data_file = open("Data/Day7_data.txt", "r")

    # Populate all nodes in tree
    for line in data_file:
        tokens = re.findall(r'(\w+)', line)
        tree.append(Node(tokens[0], tokens[1]))

    # Populate children/parents
    for line in data_file:
        tokens = re.findall(r'(\w+)', line)
        # Check if node has children
        if len(tokens) > 2:




    for node in tree:
        print(node.name + ": " + node.weight)


if __name__ == "__main__":
    main()