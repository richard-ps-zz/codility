import unittest
# A zero-indexed array A consisting of N different integers is given. The array
# contains integers in the range [1..(N + 1)], which means that exactly one
# element is missing.
#
# Your goal is to find that missing element.
#
# Write a function:
#
# def solution(A)
#
# that, given a zero-indexed array A, returns the value of the missing element.
#
# For example, given array A such that:
#
#   A[0] = 2
#   A[1] = 3
#   A[2] = 1
#   A[3] = 5
# the function should return 4, as it is the missing element.
#
# Assume that:
#
# N is an integer within the range [0..100,000];
# the elements of A are all distinct;
# each element of array A is an integer within the range [1..(N + 1)].
# Complexity:
#
# expected worst-case time complexity is O(N);
# expected worst-case space complexity is O(1), beyond input storage (not
# counting the storage required for input arguments).
# Elements of input arrays can be modified.


def solution(A):
    if not A:
        return 1

    length_A = len(A)

    if length_A == 1 and A[0] == 1:
        return 2

    if length_A == 1 and A[0] != 1:
        return 1

    sorted_list = sorted(A)

    if sorted_list[0] != 1:
        return 1

    if sorted_list[length_A-1] != length_A+1:
        return length_A+1

    if length_A == 2 and A[0] == 1 and A[1] == 2:
        return 3

    for i in range(0, len(A)-1, 1):
        if sorted_list[i+1] - sorted_list[i] != 1:
            return sorted_list[i]+1

class TestPermutationMiss(unittest.TestCase):

  def test_permutation_miss(self):
      self.assertEqual(solution([2,3,1,5]), 4)

if __name__ == '__main__':
    unittest.main()
