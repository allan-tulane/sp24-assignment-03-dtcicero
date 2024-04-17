import math, queue
from collections import Counter

####### Problem 3 #######

test_cases = [('book', 'back'), ('kookaburra', 'kookybird'), ('elephant', 'relevant'), ('AAAGAATTCA', 'AAATCA')]
alignments = [('b--ook', 'bac--k'), ('kook-ab-urr-a', 'kooky-bi-r-d-'), ('relev--ant','-ele-phant'), ('AAAGAATTCA', 'AAA---T-CA')]

def MED(S, T):
  if S == "":
      return len(T)  
  elif T == "":
      return len(S)  
  else:
      if S[0] == T[0]:
          return MED(S[1:], T[1:]) 
      else:
          
          insert = 1 + MED(S, T[1:])     
          delete = 1 + MED(S[1:], T)     
          substitute = 1 + MED(S[1:], T[1:]) 
          return min(insert, delete, substitute)


def fast_MED(S, T, memo={}):
  if (S, T) in memo:
      return memo[(S, T)]

  if S == "":
      result = len(T)
  elif T == "":
      result = len(S)
  elif S[0] == T[0]:
      result = fast_MED(S[1:], T[1:], memo)
  else:
      insert = 1 + fast_MED(S, T[1:], memo)
      delete = 1 + fast_MED(S[1:], T, memo)
      substitute = 1 + fast_MED(S[1:], T[1:], memo)
      result = min(insert, delete, substitute)

  memo[(S, T)] = result
  return result

def fast_align_MED(S, T):
  m, n = len(S), len(T)


  memo = [[0] * (n + 1) for _ in range(m + 1)]
  

  for i in range(m + 1):
      memo[i][0] = i
  for j in range(n + 1):
     memo[0][j] = j

  for i in range(1, m + 1):
    for j in range(1, n + 1):
      if S[i - 1] == T[j - 1]:
         memo[i][j] = memo[i - 1][j - 1]
      else:
          memo[i][j] = min(memo[i - 1][j], memo[i][j - 1], memo[i - 1][j - 1]) + 1

  align_S = ''
  align_T = ''
  i, j = m, n
  while i > 0 or j > 0:
    if i > 0 and j > 0 and S[i - 1] == T[j - 1]:
        align_S = S[i - 1] + align_S
        align_T = T[j - 1] + align_T
        i -= 1
        j -= 1
    elif j > 0 and (i == 0 or memo[i][j - 1] + 1 == memo[i][j]):
        align_S = '-' + align_S
        align_T = T[j - 1] + align_T
        j -= 1
    elif i > 0 and (j == 0 or memo[i - 1][j] + 1 == memo[i][j]):
        align_S = S[i - 1] + align_S
        align_T = '-' + align_T
        i -= 1
    else:
        align_S = S[i - 1] + align_S
        align_T = T[j - 1] + align_T
        i -= 1
        j -= 1

  return align_S, align_T
