class BoardHandler:

    def __init__(self, board):
        """creates a board handler for the board passed in"""
        self.board = board

    def insertTileAtAnchorSquare(self, anchorSquare, partialWord, newTile):
        """inserts a tile at the position of the anchor square after recursively shifting the current tiles to the LEFT one square to make room"""
        print 'insert \'%s\' at anchor square' % newTile
        print '  before insert', partialWord
        if len(partialWord) == 0:
            leftSquare = self.getLeftSquare(anchorSquare)
            leftSquare.tile = newTile
            partialWord.append(leftSquare)
        else:
            leftSquare = self.getLeftSquare(partialWord[0])
            partialWord.insert(0, leftSquare)

            for index in range(1, len(partialWord)):
                partialWord[index-1].tile = partialWord[index].tile

            partialWord[-1].tile = newTile

        print '  after insert', partialWord

    def removeTileFromAnchorSquare(self, partialWord):
        """removes a tile at the position of the anchor square then shifts the current tiles to the RIGHT one square"""
        if len(partialWord) > 1:
            for square in partialWord[:0:-1]:
                leftSquare = self.getLeftSquare(square)
                square.tile = leftSquare.tile
        partialWord[0].tile = '-'
        partialWord = partialWord[1:]

        print 'remove tile from at anchor square', partialWord

    def getLeftSquare(self, square):
        """return the LEFT adjacent square to the passed in square based on orientation of the self.board"""
        if self.board.orientation == 0:
            x = square.x - 1
            if x >= 0:
                return self.board.grid[square.y][x]
        else:
            y = square.y - 1
            if y >= 0:
                return self.board.grid[y][square.x]
        return None

    def getRightSquare(self, square):
        """return the RIGHT adjacent square to the passed in square based on orientation of the board"""
        if self.board.orientation == 0:
            x = square.x + 1
            if x < 15:
                return self.board.grid[square.y][x]
        else:
            y = square.y + 1
            if y < 15:
                return self.board.grid[y][square.x]
        return None

    def getTopSquare(self, square):
        """return the ABOVE adjacent square to the passed in square based on orientation of the board"""
        if self.board.orientation == 0:
            y = square.y - 1
            if y >= 0:
                return self.board.grid[square.x][y]
        else:
            x = square.x - 1
            if x >= 0:
                return self.board.grid[square.y][x]
        return None

    def getBottomSquare(self, square):
        """return the BELOW adjacent square to the passed in square based on orientation of the board"""
        if self.board.orientation == 0:
            y = square.y + 1
            if y < 15:
                return self.board.grid[y][square.x]
        else:
            x = square.x - 1
            if x >= 0:
                return self.board.grid[square.y][x]
        return None
