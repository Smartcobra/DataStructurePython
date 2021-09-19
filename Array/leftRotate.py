import array as arr


def left_rotation(array, d):
    length = len(arr)
    for i in range(d):
        left_rotation_one(arr)


def left_rotation_one(array):
    tmp = arr[0]
    length = len(arr)
    for i in range(length - 1):
        arr[i] = arr[i + 1]
    arr[length - 1] = tmp


# utility function to print an array */
def print_array(array):
    arr_len = len(arr)
    for i in range(arr_len):
        print(arr[i], end=" ")


# Driver program to test above functions */
arr = arr.array('i', [1, 2, 3, 4, 5, 6, 7])
left_rotation(arr, 2)
print_array(arr)
