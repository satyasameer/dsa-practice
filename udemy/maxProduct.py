#time complexity O(n**2)
def max_product(arr):
    # TODO
    max_product = 0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            product = arr[i]*arr[j]
            #print(arr[i], arr[j], product)
            if product > max_product:
                max_product = product
    return max_product


##time Complexity O(n)
##Space Complexity O(1)

def max_product_1(arr):
    max1, max2 = 0, 0

    for num in arr:
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2:
            max2 = num

    return max1*max2



print(max_product_1([1,7,3,4,9,5]))

#print(max_product([1,7,3,4,9,5]))