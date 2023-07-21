"""
In Python, the get() method is a built-in function for dictionaries. It is used to retrieve the value associated with a given key from a dictionary.

The get() method takes two parameters: the key you want to retrieve the value for, and an optional default value to return if the key is not found in the dictionary.

Here's the syntax for using the get() method:

dictionary.get(key, default)

"""


"""
key: The key whose value you want to retrieve from the dictionary.
default (optional): The value to be returned if the key is not found in the dictionary. If not specified, it defaults to None.

Here's an example to illustrate how the get() method works:
"""
student_scores = {'John': 90, 'Alice': 85, 'Bob': 70}

score = student_scores.get('Alice')
print(score)  # Output: 85

score = student_scores.get('Charlie')
print(score)  # Output: None

score = student_scores.get('Charlie', 0)
print(score)  # Output: 0

# In the example above, student_scores is a dictionary that stores the scores of different students. We use the get() method to retrieve the score for the key 'Alice', which returns 85. When we try to retrieve the score for the key 'Charlie', which is not present in the dictionary, the get() method returns None. In the last example, we provide a default value of 0 as the second argument to get(), so if the key is not found, it returns 0 instead of None.


# Example Program
# Dictionary of student scores
student_scores = {'John': 90, 'Alice': 85, 'Bob': 70}

# Retrieve scores using the get() method
score_john = student_scores.get('John')
score_alice = student_scores.get('Alice')
score_charlie = student_scores.get('Charlie', 0)

# Print the scores
print("John's score:", score_john)
print("Alice's score:", score_alice)
print("Charlie's score:", score_charlie)

"""
In this example, we have a dictionary student_scores that contains the scores of different students. We use the get() method to retrieve the scores for three students: John, Alice, and Charlie.

For John and Alice, their scores are present in the dictionary, so the get() method returns the respective scores (90 and 85). However, for Charlie, the key is not present in the dictionary. In this case, we have provided a default value of 0 as the second argument to get(). Hence, it returns 0 as Charlie's score.

Finally, we print the scores using print() statements.
"""