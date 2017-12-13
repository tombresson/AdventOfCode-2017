from typing import List
from copy import deepcopy

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y)

class Node(object):
    def __init__(self, value, loc: Point):
        self.value = value
        self.loc = loc


def right(loc: Point):
    loc.x += 1
    return loc


def down(loc: Point):
    loc.y -= 1
    return loc


def left(loc: Point):
    loc.x -= 1
    return loc


def up(loc: Point):
    loc.y += 1
    return loc


def main():
    target_value = 368078

    movement = [right, up, left, down]
    spiral_list: List[Node] = []


    current_location = Point(0,0)
    current_value = 1
    current_step = 1
    current_direction = 0
    num_directions = len(movement)

    # Generate Spiral
    while current_value < target_value:
        for idx in range(2):
            steps = 0
            while steps < current_step:
                # Place the value
                spiral_list.append(Node(current_value, deepcopy(current_location)))

                # Increment the value
                current_value += 1

                # Move to the next position
                movement[current_direction](current_location)

                # Count the step
                steps += 1

            # Change direction
            current_direction = (current_direction + 1) % num_directions

        # Increase the number of steps taken per direction
        current_step += 1

    # Find Manhattan Distance from End Node to origin
    end_node = spiral_list[target_value-1]
    print("Distance: " + str(abs(end_node.loc.x)+ abs(end_node.loc.y)))




if __name__ == "__main__":
    main()