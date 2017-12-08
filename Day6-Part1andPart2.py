import copy

data = [10, 3, 15, 10, 5, 15, 5, 15, 9, 2, 5, 8, 5, 2, 3, 6]

# data = [0, 2, 7, 0]

history = []

repeated_set = False
redistribution_count = 0
repeated_index = 0
while (not repeated_set):
    # Check if set has been seen before
    for element in history:
        if(element == data):
            repeated_set = True
            repeated_index = history.index(element)

    # Store the current data set
    history.append(copy.deepcopy(data))

    if not repeated_set:
        # Find next max value
        max_value = max(data)
        max_index = data.index(max_value)

        # Set to zero and redistribute
        data[max_index] = 0
        current_index = max_index
        while(max_value  > 0):
            current_index = ((current_index + 1) %len(data))
            data[current_index] += 1
            max_value -= 1

        redistribution_count += 1

print(redistribution_count)

print(((len(history) - 1) - repeated_index))