#!/usr/bin/python3
""" Minimum Operations """
def minOperations(n):
     """
     Your text editor can execute only two operations in this file: Copy All and Paste
     """   
     if not isinstance(n, int):
          return 0

     opr = 0
     i = 2
     while (i <= n):
          if not (n % i):
                n = int(n / i)
                opr += i
                i = 1
          i += 1
     return opr
