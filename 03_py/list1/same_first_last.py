# https://codingbat.com/prob/p179078

"""
Given an array of ints, return True if the array is length 1 or more, and the
first element and the last element are equal.
"""
def same_first_last(nums):
  if len(nums) == 0:
    return False
  first = nums[0]
  last = nums[-1]
  return first == last

# test cases: do not edit
print(same_first_last([1, 2, 3])) # False
print(same_first_last([1, 2, 3, 1])) # True
print(same_first_last([1, 2, 1])) # True

