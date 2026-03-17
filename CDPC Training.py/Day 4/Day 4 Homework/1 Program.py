#Write a Python function to find the maximum and minimum elements in an array.
#Logic: Iterate through the array and update the maximum and minimum values as you go.


def find_max_min(arr):
    max_num = arr[0]
    min_num = arr[0]

    for i in arr:
        if i > max_num:
            max_num = i
        if i < min_num:
            min_num = i

    return max_num, min_num


numbers = [5, 3, 9, 2, 8]

maximum, minimum = find_max_min(numbers)

print("Maximum:",maximum)
print("Minimum:", minimum)