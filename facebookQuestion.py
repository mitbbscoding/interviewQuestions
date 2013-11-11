#!/usr/bin/env python2.7
import sys
import pdb
import argparse
from collections import defaultdict
import numpy as np

"""
question was originally post here: http://goo.gl/L7uwNH

user1:
  login_time: 0
  logout_time: 1

  user2:
  login_time: 0
  logout_time: 2

  user3:
  login_time: 1
  logout_time: 3

  [0 - 2): 2
  [2 - 3): 1
  [3 - infinite): 0

"""
def printUsersForEachPeriod(logs):
  """
  Given a list of `log`s, print the number of users in each period to the STDOUT 

  Parameters
  ===========
  logs: list, `log` is defined by a login time and a logout time

  class log:
    def __init__(self, start, end):
    pass

  """ 
  table = defaultdict(int)

  if len(logs) <= 0:
    return

  for log in logs:
    for i in range(log[0], log[1]):
      table[i] += 1

  sortedKeys = sorted(table.keys())

  prev = sortedKeys[0]
  for i in range(1, sortedKeys[-1] + 1):
    if table[i] != table[prev]:
      print "[%d - %d): %d" % (prev, i, table[prev])
      prev = i
   
  print "[%d - %d): %d" % (prev, sortedKeys[-1] + 1, table[prev])
  print "[%d - %f): %d" % (sortedKeys[-1] + 1, np.inf, 0)

if __name__ == '__main__':
  logs = [ (0, 1), (0, 2), (1, 3), (4, 5)]
  printUsersForEachPeriod(logs)

