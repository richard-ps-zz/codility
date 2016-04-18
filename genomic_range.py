import unittest


# The DNA sequence is given as a non-empty string S = S[0]S[1]...S[N-1] consisting of N characters.

# There are M queries, which are given in non-empty arrays P and Q, each
# consisting of M integers. The K-th query (0 ≤ K < M) requires you to find the
# minimal impact factor of nucleotides contained in the DNA sequence between
# positions P[K] and Q[K] (inclusive).

# A, C, G and T have impact factors of 1, 2, 3 and 4,

def solution(S, P, Q):
    results = []
    X = {'A':1, 'C':2, 'G':3, 'T':4}
    full_word = [X[S[i]] for i in xrange(0, len(S), 1)]

    for i in xrange(0, len(P), 1):
        word = full_word[P[i]:Q[i]+1]
        results.append(min(word))   

    return results

class TestGenomicRange(unittest.TestCase):

  def test_genomic_range(self):
      self.assertEqual(solution("CAGCCTA",[2,5,0],[4,5,6]), [2,4,1])

if __name__ == '__main__':
    unittest.main()
