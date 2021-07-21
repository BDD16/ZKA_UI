"""
DBA 1337_TECH, AUSTIN TEXAS © July 2021
Proof of Concept code, No liabilities or warranties expressed or implied.
"""

import math



me = '[ComplexityEngine]'
class ComplexityEngine:

      def __init__(self,N=94, L=0):
          self.N = N;
          self.L = L;

      def CalculatePwdCompelxity(self):
          result = self.L * math.log2(self.N)

          return result
