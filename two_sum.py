# Given an array of integers, return indices of the two numbers such that they add up to a specific target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.


# 1. Restate the problem:
    # Given a target (t) and an array of integers (a), I will return the indices of the two numbers that add up to the specific target.

# 2. Ask clarifying questions
    # 1) Is this list sorted?

# 3. State your assumptions
    # 2) I assume this list in unsorted.

# 4. Think out loud (the whole time)
#       a. Brainstorm solutions:

            # a = [1, 4, 6, 8]
            # t = 10

            #(0, 1) (1, 4) (2, 6) (3, 8)

            # naive solution : iterate through the array find the sum of each pair then compare each sum to the target

            # 1+4, 1+6, 1+8 -> see if equals 10
            # 10 -1 = 9; 10 - 4

            # iterate through list see if the number added to the complement = target

            #val = {1:0, 4:1, 6:2, 8:3}
            # loop through the array we're getting comp_value
            # comp_value = t - value
            # val[num] = index
            # if comp_value is val.keys():
            #     return key, value   # as well as the number and index of that number
            #look at comp_value in dict
            #dictionary with complement of value as key, index as value

#       b. Explain your rationale
            # I chose to use a hashtable so that I could simultaneously add each number and index to the table while also checking to see if the number's complement is present. If I find the number and its complement, then I return the indices of those two numbers as a list.

#       c. Discuss tradeoffs
            # This solution is more time efficient but less space efficient. 

#       d. Suggest improvements
            # I can't think of improvements on this solution, since it brought the time complexity down as close to O(1) as possible.


def two_sum(arr, t):
    val = {} 
    for index, num in enumerate(arr):
        if t - num in val:
            return ([val[t-num], index])
        val[num] = index
    return ([])



print(two_sum([5, 6, 8, 3, 2, 6], 11))
