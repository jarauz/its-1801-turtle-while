"""
This is the Template Repl for Python with Turtle.

Python with Turtle lets you make graphics easily in Python.

Check out the official docs here: https://docs.python.org/3/library/turtle.html
"""

import turtle

casper = turtle.Turtle()

i = 0
while (i<4):
  print(i)
  i = i + 1
  casper.forward(75)
  casper.left(90)
 
# Read i = i + 1 as: the new
# value of i is equal to
# the current value + 1
  