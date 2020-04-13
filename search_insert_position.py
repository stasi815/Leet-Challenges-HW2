# Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

#You may assume no duplicates in the array.

# 1. Restate the problem:
    # I am going to return the index of a target value (t) in a given array (arr) and if t is not in arr, I will return the index where it would be.

# 2. Ask clarifying questions
    # 1) Is this made up of integer values?

# 3. State your assumptions
    # 2) I assume this list has integers.

# 4. Think out loud (the whole time)
#       a. Brainstorm solutions:

            # A binary search could shorten search time and utilize the fact that the array is sorted.

#       b. Explain your rationale
            # We can use a binary search since the array is sorted.

#       c. Discuss tradeoffs
            # This solution is more elegant than the naive solution but just as time complex.

#       d. Suggest improvements
            # There might be a way to use a hashtable here to decrease search time.

def searchInsertPosition(arr, t):
    start = 0
    end = len(arr) - 1
    insert = 0
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == t:
            # Target found
            return mid
        elif arr[mid] > t:
            end = mid - 1
            insert = mid
        else:
            start = mid + 1
            insert = mid + 1
    return insert

print(searchInsertPosition([1, 2, 3, 4, 5, 7], 6))