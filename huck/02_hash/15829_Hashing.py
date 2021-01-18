import sys
import os

g_r = 31
g_M = 1234567891
g_result = 0

def handleInput():
  inputFileSuffix = '_input.txt'
  fileName, fileExtension = os.path.splitext(__file__)
  inputFileName = fileName + inputFileSuffix
  sys.stdin = open(inputFileName, "r")

def solution(expression):
  global g_r
  global g_M
  global g_result

  expression = expression.rstrip('\n')
  sequence = []
  sequence.extend(ord(char) - ord('a') + 1 for char in expression)
  for i, value in enumerate(sequence):
    # sum(a0 * r^0   ~   ai * r^i) / M
    # i의 최대값은 50
    g_result += (value * pow(g_r, i)) % g_M

  # g_result %= g_M
  print(g_result)
  g_result = 0

if __name__ == "__main__":
  if None != os.getenv('IS_LOCAL'):
    handleInput()

  for _ in sys.stdin:
    expression = sys.stdin.__next__() # 문자열길이 스킵
    solution(expression)
