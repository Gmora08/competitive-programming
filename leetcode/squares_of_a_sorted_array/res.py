class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        length = len(A) - 1

        for n, i in enumerate(A, start=0):
            p
            A[i] = pow(n, 2)
        
        for n, i in enumerate(A, start=0):
            if i == length:
                break
            if n > A[i+1]:
                A[i] = A[i+1]
                A[i+1] = n
        return squares
