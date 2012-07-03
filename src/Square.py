'''
Created on Jun 27, 2012

@author: JS018234
'''

class Square:
  NextID = 0
  def __init__(self):
    self.id = self.NextID
    Square.NextID += 1
    self.nextSquare = None
    self.tile = '-'
    self.wordBonus = 1
    self.letterBonus = 1