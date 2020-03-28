from pytest import fixture

from src.shift_match import is_it_match

"""
SHIFT_MATCH

??
Difficulty: Easy

This problem was asked by Google.Given two strings A and B, return whether or not A can be shifted some number of times to get B.
For example, if A is abcde and B is cdeab, return true. If A is abc and B is acb, return false.
"""

CASES = [
    {
        "input1": 'abcde',
        "input2": 'cdeab',
        "answer": True,
        
    },
    {
        "input1": 'abc',
        "input2": 'acb',
        "answer": False,
    },
    {
        "input1": 'cde',
        "input2": 'cde',
        "answer": True,
    },
]



@fixture(params=CASES)
def case(request):
    return request.param


def test__is_it_match__signature(case):
    input1 = case["input1"]
    input2 = case["input2"]

    result = is_it_match(input1, input2)
    assert isinstance(result, bool)


def test__is_it_match__examples(case):
    input1 = case["input1"]
    input2 = case["input2"]
    answer = case["answer"]

    result = is_it_match(input1, input2)
    assert answer == result

