from typing import List
import re

class Program(object):
    def __init__(self, id):
        self.id = id
        self.connected_to_zero = False
        self.connections = []

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

        # Special case 0
        if prgm.id == '0':
            prgm.connected_to_zero = True

        if len(tokens) > 1:
            # Iterate through the prgms connections
            for token in tokens[1:]:

                if token == '0':
                    prgm.connected_to_zero = True

                else:
                    # Check existing node to determine if
                    # it is connected to zero through another prgm
                    x: Program = prgms[int(token)]
                    if x.connected_to_zero:
                        prgm.connected_to_zero = True

                # Append the connection to the prgm
                prgm.connections.append(prgms[int(token)])

            # If this node is now connected to zero, ensure all the listed nodes are as well
            if prgm.connected_to_zero:
                for x in prgm.connections:
                    x.connected_to_zero = True


    connections_cnt = 0
    for prgm in prgms:
        if prgm.connected_to_zero:
            connections_cnt += 1

    print(connections_cnt)





if __name__ == "__main__":
    main()