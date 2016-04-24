import unittest

def solution(A):
    A = sorted(A)

    for i in range(0,len(A)-2, 1):
        if A[i] + A[i+1] > A[i+2]:
            return 1

    return 0

class TestTriangle(unittest.TestCase):

  def test_triangle(self):
      self.assertEqual(solution([10,2,5,1,8,20]), 1)
      self.assertEqual(solution([10,50,5,1]), 0)
      self.assertEqual(solution([5, 3, 3]), 1)


if __name__ == '__main__':
    unittest.main()
