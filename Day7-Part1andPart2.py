import re

class Node(object):
    """Objects in a tree"""

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.parent = None
        self.children = []

    def isLeaf(self):
        return len(self.children) == 0

    def isRoot(self):
        return self.parent == self


def all_same(items: list):
    return all(x == items[0] for x in items)


def find_unbalanced(tree_node: Node):
    list_of_child_weights = []
    if len(tree_node.children) > 0:
        for node in tree_node.children:
            list_of_child_weights.append(find_unbalanced(node))

    if not all_same(list_of_child_weights):
        print(tree_node.name)

    return tree_node.weight





def main():
    tree = []

    data_file = open("Data/Day7_data.txt", "r")

    # Populate all nodes in tree
    for line in data_file:
        tokens = re.findall(r'(\w+)', line)
        tree.append(Node(tokens[0], tokens[1]))

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

    for node in tree:
        if node.parent == None:
            print("Tree Root:" + node.name)
            root_node = node


    find_unbalanced(root_node)


if __name__ == "__main__":
    main()