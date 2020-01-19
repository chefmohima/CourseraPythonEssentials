"""
Template - Flatten a nested list
"""

def flatten(nested_list):
    """
    Given a list whose items are list, 
    return the list formed by joining all of these lists
    """
    result_list = []
    for row in range(len(nested_list)):
        for col in range(len(nested_list[row])):
            result_list.append(nested_list[row][col])
    return result_list

# Test code
print(flatten([]))
print(flatten([[]]))
print(flatten([[1, 2, 3]]))
print(flatten([["cat", "dog"], ["pig", "cow"]]))
print(flatten([[9, 8, 7], [6, 5], [4, 3, 2], [1]]))


# Output
#[]
#[]
#[1, 2, 3]
#['cat', 'dog', 'pig', 'cow']
#[9, 8, 7, 6, 5, 4, 3, 2, 1]
