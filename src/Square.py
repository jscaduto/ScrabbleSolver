'''
Created on Jun 27, 2012

@author: JS018234
'''

class Square(object):
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.tile = '-'
    self.wordBonus = 1
    self.letterBonus = 1
    self.crossCheckSet = set(map(chr, range(97, 123)))
    self.isAnchorSquare = False
  def __str__(self):
    return self.tile
