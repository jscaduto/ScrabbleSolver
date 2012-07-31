'''
Created on Jun 28, 2012

@author: JS018234
'''

import Square

class Board:
  def __init__(self, cols, rows):
    self.rows = rows
    self.cols = cols
    self.grid = [[Square.Square() for j in range(cols)] for i in range(rows)]
  def __str__(self):
    buffer = '' 
    buffer += '-'*((self.cols * 2) + 1) + '\n'
    for row in range(self.rows):
      for col in range(self.cols):
        buffer += '|' + str(self.grid[row][col])
      buffer += '|\n'
      buffer += '-'*((self.cols * 2) + 1) + '\n'
    return buffer
