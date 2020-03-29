from pytest import fixture

from src.addup_for_k_bygoogle import find_k

"""
ADDUP_FOR_K(BYGOOGLE)

This problem was recently asked by Google.
Difficulty: Easy

Given a list of numbers and a number k, return whether any two numbers from thelist add up to k.For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.Bonus: Can you do this in one pass?
"""

CASES = [
    {
        "input1": [10, 15, 3, 7],
        "input2": 17,
        "answer": True,
    },
    {
        "input1": [10, 15, 3, 7],
        "input2": 16,
        "answer": False,
    },
]



@fixture(params=CASES)
def case(request):
    return request.param


def test__find_k__signature(case):
    input1 = case["input1"]
    input2 = case["input2"]

    result = find_k(input1, input2)
    assert isinstance(result, bool)


def test__find_k__examples(case):
    input1 = case["input1"]
    input2 = case["input2"]
    answer = case["answer"]

    result = find_k(input1, input2)
    assert answer == result

