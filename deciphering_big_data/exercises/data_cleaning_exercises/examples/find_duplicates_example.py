## Remove duplicates
# list_with_dupes = [1, 5, 6, 2, 5, 6, 8, 3, 8, 3, 3, 7, 9]
# set_without_dupes = set(list_with_dupes)
# print(set_without_dupes)

## Perform different types of comparisons
# first_set = set([1, 5, 6, 2, 6, 3, 6, 7, 3, 7, 9, 10, 321, 54, 654, 432]) 
# second_set = set([4, 6, 7, 432, 6, 7, 4, 9, 0])
# print(first_set.intersection(second_set))
# print(first_set.union(second_set))
# print(first_set.difference(second_set))
# print(second_set - first_set)
# print(6 in second_set)
# print(0 in first_set)

# # Use numpy unique
# import numpy as np
# list_with_dupes = [1, 5, 6, 2, 5, 6, 8, 3, 8, 3, 3, 7, 9]
# print(np.unique(list_with_dupes, return_index=True))
# array_with_dupes = np.array([[1, 5, 7, 3, 9, 11, 23], [2, 4, 6, 8, 2, 8, 4]]) 
# print(np.unique(array_with_dupes))