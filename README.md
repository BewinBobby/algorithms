# Algorithms

Courses Coding Asigments


# Problem of the day

## Decomposition pair

This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the
list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?

Solution:
- [tests](tests/test__decomposition_pair.py)
- [implementation](src/decomposition_pair.py)

## The product of others

This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i 
of the new array is the product of all the numbers in the original array except
the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be 
[120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be 
[2, 3, 6].

Follow-up: what if you can't use division?

Solution:
- [tests](tests/test__the_product_of_others.py)
- [implementation](src/the_product_of_others.py)


## Tree Again

This problem was asked by Google.

Given the root to a binary tree, implement serialize(root), which serializes the
tree into a string, and deserialize(s), which deserializes the string back into
the tree.

For example, given the following Node class

```Python
    class Node:
        def __init__(self, val, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right
```


The following test should pass:

```Python
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    assert deserialize(serialize(node)).left.left.val == 'left.left'
```

I decided not to take shortcuts (using custom serializer for pickle or json), but
instead implement a tailored syntax. It's not too complex and allows for a more clean
representation:

```
    root
        left
            left.left
                None
                None
            None
        right
            None
            None
```

Solution:
- [tests](tests/test__tree_again.py)
- [implementation](src/tree_again.py)
