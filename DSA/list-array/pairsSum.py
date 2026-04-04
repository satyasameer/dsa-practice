# time complexity O(n**2)
# space complexity O(n)

def pair_sum(myList, sum):
    # TODO
    final_result = []
    for i in range(len(myList)):
        for j in range(i+1, len(myList)):
            if myList[i] + myList[j] == sum:
                final_result.append(f"{myList[i]}+{myList[j]}")
    return final_result

# time complexity O(n)
# space complexity O(n)

def pair_sum_1(myList, target):
    seen = set()
    final_result = []
    for num in myList:
        complement = target - num
        if complement in seen:
            final_result.append(f"{complement}+{num}")

        seen.add(num)
    return final_result

print(pair_sum_1([2, 4, 3, 5, 6, -2, 4, 7, 8, 9], 7))

#print(pair_sum([2, 4, 3, 5, 6, -2, 4, 7, 8, 9], 7))