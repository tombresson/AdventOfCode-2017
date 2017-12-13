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


def find_next_value(spiral_list: List[Node], loc:Point):
    walk = [up, left, down, down, right, right, up, up]
    current_location = deepcopy(loc)
    value = 0
    for move in walk:
        # Modify the location
        move(current_location)

        # Check the list to see if location exists
        for node in spiral_list:
            # If so, add the value to the current value
            if node.loc == current_location:
                value += node.value

    return value


def main():
    target_value = 368078

    movement = [right, up, left, down]
    spiral_list: List[Node] = []

    current_location = Point(0,0)
    current_value = 1
    current_step = 1
    current_direction = 0
    num_directions = len(movement)
    value_which_exceeds_target = 0

    # Generate Spiral
    while current_value <= target_value:
        for idx in range(2):
            steps = 0
            while steps < current_step:
                # Place the value
                spiral_list.append(Node(current_value, deepcopy(current_location)))

                # Move to the next position
                movement[current_direction](current_location)

                # Find next value
                current_value = find_next_value(spiral_list, current_location)

                # Check to see if the just calculated value exceeds the target
                if (value_which_exceeds_target == 0) and (current_value > target_value):
                    # Store the value which exceeded the target
                    value_which_exceeds_target = current_value

                # Count the step
                steps += 1

            # Change direction
            current_direction = (current_direction + 1) % num_directions

        # Increase the number of steps taken per direction
        current_step += 1

    # Number of steps to get to a value greater than the target
    print("Steps: " + str(value_which_exceeds_target))


if __name__ == "__main__":
    main()