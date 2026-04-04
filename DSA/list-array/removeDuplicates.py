## time complexity O(n**2)
## space Complexity O(n)

def remove_duplicates(arr):
    # TODO
    new_arr = []
    for num in arr:
        if num not in new_arr:
            new_arr.append(num)
    return new_arr

# time complexity O(n)  -> array/list lookup is O(n)
# set lookup is O(1)
def remove_duplicates_1(arr):
    new_arr = []
    seen = set()
    for num in arr:
        if num not in seen:
            new_arr.append(num)
            seen.add(num)
    return new_arr

my_list = [1, 1, 2, 2, 3, 4, 5]
print(remove_duplicates_1(my_list))  # Output: [1, 2, 3, 4, 5]
