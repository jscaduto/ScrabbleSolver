import unittest
import Square
import Board

class TestBoardCreation(unittest.TestCase):
  def setUp(self):
    self.board = Board.Board(15,15) 

  def test_printBoard(self):
    print self.board

if __name__ == '__main__':
  unittest.main()
