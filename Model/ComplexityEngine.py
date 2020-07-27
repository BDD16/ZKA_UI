import math



me = '[ComplexityEngine]'
class ComplexityEngine:

      def __init__(self,N=94, L=0):
          self.N = N;
          self.L = L;

      def CalculatePwdCompelxity(self):
          result = self.L * math.log2(self.N)

          return result
