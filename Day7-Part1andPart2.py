import re

class Node(object):
    """Objects in a tree"""

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.supported_weight = 0
        self.parent = None
        self.children = []

    def isLeaf(self):
        return len(self.children) == 0

    def isRoot(self):
        return self.parent is None


def all_same(items: list):
    return all(x == items[0] for x in items)


def populate_supported_weight(node: Node):
    list_of_child_weights = []
    if len(node.children) > 0:
        for x in node.children:
            list_of_child_weights.append(populate_supported_weight(x))

    # Sum up weights of children
    for weight in list_of_child_weights:
        node.supported_weight += weight

    # Add in own weight
    node.supported_weight += node.weight

    return node.supported_weight


def find_unbalanced(tree_node: Node):
    # Only one child will be different from the rest
    weights = []
    counts = []

    for node in tree_node.children:
        if node.supported_weight in weights:
            idx = weights.index(node.supported_weight)
            counts[idx] += 1
        else:
            weights.append(node.supported_weight)
            counts.append(1)

    # Only a single node should have a count of one
    unbal_weight = weights[counts.index(1)]

    # for node in tree_node.children:
    #     if node.supported_weight == unbal_weight:
    #         # Traverse down the tree






def main():
    tree = []

    data_file = open("Data/Day7_data.txt", "r")

    # Populate all nodes in tree
    for line in data_file:
        tokens = re.findall(r'(\w+)', line)
        tree.append(Node(tokens[0], int(tokens[1])))

    # Reset file position to beginning
    data_file.seek(0)

    # Populate children/parents
    for i, line in enumerate(data_file):
        tokens = re.findall(r'(\w+)', line)
        # Check if node has children
        if len(tokens) > 2:
            for token in tokens[2:]:
                for node in tree:
                    if node.name == token:
                        # Add parent to child
                        node.parent = tree[i]
                        # Add child to parent
                        tree[i].children.append(node)

    # Find root node
    for node in tree:
        node: Node = node
        if node.isRoot():
            root_node = node
            print("Tree Root: " + node.name)

    populate_supported_weight(root_node)
    find_unbalanced(root_node)


if __name__ == "__main__":
    main()