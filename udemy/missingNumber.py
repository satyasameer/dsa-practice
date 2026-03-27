#Brute force approach
# time complexity O(n2)

def missing_number(arr, n):
    # TODO
    for i in range(1,n+1):
        if i not in arr:
            return i

# Sum Formula
# time complexity O(n)

def missing_number(arr, n):
    # Calculate the sum of first n natural numbers
    total = n * (n + 1) // 2

    # Calculate the sum of numbers in the array
    sum_arr = sum(arr)

    # Find the missing number by subtracting sum_arr from total
    missing = total - sum_arr

    return missing

# Example
print(missing_number([1, 2, 3, 4, 6], 6))