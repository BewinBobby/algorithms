def is_it_match(input1, input2):
    """SHIFT_MATCH
    Difficulty: Easy 
    
    This problem was asked by Google.Given two strings A and B, return whether or not A can be shifted some number of times to get B.
    For example, if A is abcde and B is cdeab, return true. If A is abc and B is acb, return false.
    
    """
    for shift in range(len(input1)):
        input2 = input2[1:] + input2[0]
        if input2 == input1:
            return True
    return False


is_it_match('abcde', 'cdeab')