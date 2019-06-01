# coding: utf-8
import math
import collections

data = 88888

def resolve_binary(number):
  result = []
  while number > 0:
    base = int(math.log2(number))
    result.append(base)
    number = number - 2 ** base
  return result

def eca_step(base):
  result = []
  for i in base:
    result.append(i + 1)
    result.append(i - 1)
  return result

def control_step(base):
  result = []
  c = collections.Counter(base)
  for key, count in c.items():
    if key < 0:
      continue
    if count == 1:
      result.append(key)
  return result

def main():
  result = resolve_binary(data)
  print(result)
  result = eca_step(result)
  print(result)
  result = control_step(result)
  print(result)

if __name__ == '__main__':
  main()