"""
In Python, the insert method is used to insert an element into a list at a specified position. The syntax for the insert method is as follows:

list.insert(index, element)

"""

"""
Here, list refers to the list object on which you want to perform the insertion. index is the position at which you want to insert the element. The element is the value that you want to insert into the list.

Let's see an example to understand how the insert method works:
"""
my_list = [1, 2, 3, 4, 5]
my_list.insert(2, 10)

print(my_list)

"""
In the above example, the insert method is used to insert the value 10 at index 2 in the my_list list. After the insertion, the list becomes [1, 2, 10, 3, 4, 5].

Note that the insert method modifies the original list in-place and returns None. It does not create a new list. If you want to create a new list with the inserted element, you can use concatenation or other list manipulation techniques.
"""


# Difference between "insert" and "append"

"""
The main difference between the insert and append methods in Python lies in how they add elements to a list:

insert: The insert method is used to insert an element at a specific position in a list. It takes two arguments: the index at which the element should be inserted and the element itself. The existing elements in the list are shifted to the right to make room for the new element.

Example:
"""
my_list = [1, 2, 3, 4, 5]
my_list.insert(2, 10)
print(my_list)

# In the above example, insert(2, 10) inserts the element 10 at index 2, resulting in the list [1, 2, 10, 3, 4, 5].


"""
append: The append method is used to add an element at the end of a list. It takes a single argument, which is the element to be added. The element is appended to the end of the list without affecting the existing elements.

Example:
"""
my_list = [1, 2, 3, 4, 5]
my_list.append(10)
print(my_list)

"""
In the above example, append(10) adds the element 10 at the end of the list, resulting in the list [1, 2, 3, 4, 5, 10].

In summary, insert allows you to specify the position where you want to insert an element, whereas append always adds an element at the end of the list.
"""