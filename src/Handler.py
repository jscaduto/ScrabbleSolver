import logging
import Square
import Board

class Handler:
  
  #recursively shift tile LEFT one square at a time, until you hit the right-most square, then replace it with a blank ('-')
  def insertTileAtAnchorSquare(board, anchorSquare, partialWord, newTile):
    if not partialWord:
      leftSquare = getLeftSquare(anchorSquare)
      partialWord.insert(0, leftSquare)
    else:
      leftSquare = getLeftSquare(partialWord[0])
      partialWord.insert(0, leftSquare)

    if len(partialWord) > 1:
      for index in range(1, len(partialWord)):
        partialWord[index-1].letter = partialWord[index].letter

    partialWord[-1].letter = newTile

    return partialWord

  #recursively shift tile RIGHT one square at a time, until you hit the left-most square, then replace it with a blank ('-')
  def removeTileFromAnchorSquare(board, partialWord, newTile):
    for index in range(0, len(LeftPart)-1):
      partialWord[index+1].letter = partialWord[index].letter
    partialWord[0].tile = newTile
    return partialWord[1:]
    
    if len(leftPart) == 1:
      tempTile = leftPart[0].tile
      leftPart[0].tile = '-'
      return tempTile
    rightSquare = leftPart[-1].getRightSquare()
    rightSquare.tile = shiftLPRight(leftPart[0:-1])

  def getLeftSquare(board, square):
    if board.orientation == 0:
      x = square.x - 1
      if x >= 0: 
        return board[x][square.y]
    else:
      y = square.y - 1
      if y >= 0: 
        return board[square.x][y]
    return None

  def getRightSquare(board, square):
    if board.orientation == 0:
      x = square.x + 1
      if x < 15:
        return board[x][square.y]
    else:
      y = square.y + 1
      if y < 15:
        return board[square.x][y]
    return None

  def getTopSquare(board, square):
    if board.orientation == 0:
      y = square.y - 1
      if y >= 0: 
        return board[square.x][y]
    else:
      x = square.x - 1
      if x >= 0: 
        return board[x][square.y]
    return None

  def getBottomSquare(board, square):
    if board.orientation == 0:
      y = square.y + 1
      if y < 15: 
        return board[square.x][y]
    else:
      x = square.x - 1
      if x >= 0: 
        return board[x][square.y]
    return None
