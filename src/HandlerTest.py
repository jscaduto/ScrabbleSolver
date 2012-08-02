import unittest
import Handler
import Board
import Square

class TestHandlerFunctions(unittest.TestCase):
    
  def test_insertTileAtAnchorSquare(self):
    #test partialWord length 0
    board = Board.Board(15,15)
    anchorSquare = board.grid[7][7]
    partialWord = []
    newTile = 't'
    partialWord = Handler.insertTileAtAnchorSquare(board, anchorSquare, partialWord, newTile)
    self.assertEqual(partialWord, ['t'])
    #test partialWord length 1

    #test partialWord length 2

  #def test_shiftLPRight(self):
    #test LP length 0
    #test LP length 1
    #test LP length 2

  #def test_getLeftSquare(self):
    #test normal
    # for horizontal
    # for vertical

    #test LEFT-most square
    # for horizontal
    # for vertical

  #def test_getRightSquare(self):
    #test normal
    # for horizontal
    # for vertical

    #test RIGHT-most square
    # for horizontal
    # for vertical

  #def test_getTopSquare(self):
    #test normal
    # for horizontal
    # for vertical

    #test TOP-most square
    # for horizontal
    # for vertical

  #def test_getBottomSquare(self):
    #test normal
    # for horizontal
    # for vertical

    #test BOTTOM-most square
    # for horizontal
    # for vertical

if __name__ == '__main__':
  unittest.main()
