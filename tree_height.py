# python3

#Deniss Dmitrijevs 221RDB322

import sys
import threading
import numpy


def compute_height(n, parents):
    # Write this function
    max_height = 0
    # Your code here
    node_heights = numpy.zeros(n)

    for node, parent in enumerate(parents):
        if (node_heights[node] == 0):
            node_heights[node] = node_heights[node] + 1
        if node_heights[parent] <= node_heights[node]:
            node_heights[parent] = node_heights[node] + 1

    max_height = node_heights[0]
    for node_height in node_heights[1:]:
        if node_height > max_height:
            max_height = node_height

    return int(max_height)


def main():
    # implement input form keyboard and from files
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result

    input_type = str(input())

    if "i" in input_type.lower():
        node_count = int(input())
        parent_list = [int(num) for num in input().split()]
        print(compute_height(node_count, parent_list))
    elif "f" in input_type.lower():
        path = "test/" + input()
        if not "a" in path:
            with open(path, 'r') as file:
                node_count = file.readLine()
                parent_list = [int(num) for num in file.readLine().split()]
                print(compute_height(node_count, parent_list))

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
main()
# print(numpy.array([1,2,3]))