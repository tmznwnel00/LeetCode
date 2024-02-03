class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        n_odd = n // 2 + n % 2
        n_even = n // 2
        m_odd = m // 2 + m % 2
        m_even = m // 2
        return n_odd * m_even + n_even * m_odd
        
        