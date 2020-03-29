def find_k(input1,input2):
    """ADDUP_FOR_K(BYGOOGLE)

    This problem was recently asked by Google.
    Difficulty: Easy

    Given a list of numbers and a number k, return whether any two numbers from thelist add up to k.For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.Bonus: Can you do this in one pass?
    """
    input1_set = set(input1)

    for number in input1:
        if number < input2:
            need_to_find = input2 - number
            if need_to_find in input1_set:
                return True
    return False