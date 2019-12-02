#!/usr/bin/python3
from typing import List


def read_input(filename: str) -> List[str]:
    lines = []

    with open(filename, 'r') as f:
        for line in f:
            lines.append(line.rstrip('\n'))
    return lines


input_data = read_input('./input')

END_CODE = 99
ADD_CODE = 1
MULTIPLY_CODE = 2
OFFSET = 4

operations = input_data[0].split(',')
# LENGTH = len(operations)

# operations[1] = 12
# operations[2] = 2

# index = 0
# while index < LENGTH:
#     operation = int(operations[index])
#     a_index = int(operations[index + 1])
#     b_index = int(operations[index + 2])
#     c_index = int(operations[index + 3])

#     a = int(operations[a_index])
#     b = int(operations[b_index])

#     if operation == ADD_CODE:
#         operations[c_index] = a + b
#     elif operation == MULTIPLY_CODE:
#         operations[c_index] = a * b
#     elif operation == END_CODE:
#         break
#     index += OFFSET

# print('Part 1', operations[0])

test_noun = 0
test_verb = 0

original_operations = operations.copy()
for test_noun in range(100):
    for test_verb in range(100):
        operations[1] = test_noun
        operations[2] = test_verb

        index = 0
        LENGTH = len(operations)
        while index < LENGTH:
            operation = int(operations[index])
            a_index = int(operations[index + 1])
            b_index = int(operations[index + 2])
            c_index = int(operations[index + 3])

            a = int(operations[a_index])
            b = int(operations[b_index])

            if operation == ADD_CODE:
                operations[c_index] = a + b
            elif operation == MULTIPLY_CODE:
                operations[c_index] = a * b
            elif operation == END_CODE:
                break

            if operations[0] == 19690720:
                print(100 * test_noun + test_verb)
                break

            index += OFFSET

        operations = original_operations.copy()


# print('Part 1', operations[0])
