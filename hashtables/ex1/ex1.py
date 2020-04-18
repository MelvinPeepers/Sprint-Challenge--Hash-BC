#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)

"""

Given a package with a weight limit limit and a list weights of item weights, implement a function get_indices_of_item_weights 
that finds two items whose sum of weights equals the weight limit limit. Your function will return an instance of an Answer tuple 
that has the following form:

    (zero, one)

The higher valued index should be placed in the zeroth index and the smaller index should be placed in the first index.

If such a pair doesn’t exist for the given inputs, your function should return None.

NOTE: When calling hash_table_retrieve with a key that doesn't exist in the hash table, hash_table_retrieve will return None.

Your solution should run in linear time.

Example:

input: weights = [ 4, 6, 10, 15, 16 ], length = 5, limit = 21
output: [ 3, 1 ]  # since these are the indices of weights 15 and 6 whose sum equals 21

"""

"""
UPER

So I have a hashtables.py to use
I'll need to iteriate through the length
I'll need to retrieve and insert
I'll need to get the indicies of the items weight who's sum equals the limit

"""


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    for i in range(length):
        weight_pairs = hash_table_retrieve(ht, limit - weights[i])
        if weight_pairs is not None:
            return (i, weight_pairs)
        else:
            hash_table_insert(ht, weights[i], i)

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
