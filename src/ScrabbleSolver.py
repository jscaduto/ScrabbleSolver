import copy
import pickle
import re
import sys
import time

from Dawg import Dawg
from Board import Board
from BoardHandler import BoardHandler

valueMap = {'A':1, 'B':4, 'C':4, 'D':2, 'E':1, 'F':4, 'G':3, 'H':3, 'I':1, 'J':10, 'K':5, 'L':2, 'M':4, 'N':2, 'O':1, 'P':4, 'Q':10, 'R':1, 'S':1, 'T':1, 'U':2, 'V':5, 'W':4, 'X':8, 'Y':3, 'Z':10, '*':0}
dawg = None
boardHandler = None
rack = []    #list of tiles
legalMoves = [] # a list of moves (ie a list of square from the board with tiles from rack placed)
plays = {} # dictionary of words:points

def getRack():
    global rack
    rack = re.findall('[a-z]|[*]', sys.argv[2])

def findAnchorSquares():
    """finds all anchor squares on board and create crossCheckSet for each of them"""
    anchorSquares = []
    for row in range(0,board.rows):
        for col in range(0,board.cols):
            square = board.grid[col][row]
            # find a square with a tile placed
            if square.tile != '-':
                # if left or right adjacent square are empty they are anchor squares
                print repr(square)
                leftSquare = boardHandler.getLeftSquare(square)
                if leftSquare.tile == '-':
                    print 'left square: ' + repr(leftSquare)
                    anchorSquares.append(leftSquare)
                rightSquare = boardHandler.getRightSquare(square)
                if rightSquare.tile == '-':
                    print 'right square: ' + repr(rightSquare)
                    anchorSquares.append(rightSquare)
    for anchorSquare in anchorSquares:
        anchorSquare.tile = '0'
    print board
    for anchorSquare in anchorSquares:
        anchorSquare.tile = '-'
    return anchorSquares

def findWords(anchorSquare):
    """find all words possible at an anchor square"""

    partialWord = [] # word formed of tiles left of anchor square
    limit = 0  # number of empty space left of the anchor square

# look at left adjacent square to anchor square
    leftSquare = boardHandler.getLeftSquare(anchorSquare)
#  if empty count how many empty sqaures there are in a row
    limit = 0
    while leftSquare != None and leftSquare.tile == '-':
        limit += 1
        leftSquare = boardHandler.getLeftSquare(leftSquare)
    if limit > 0:
        LeftPart(partialWord, dawg.root, limit, anchorSquare)
        return

#  if it has a tile, add that square and all consecutive squares to leftPart
    partialWordStr = leftSquare.tile
    while leftSquare != None and leftSquare.tile != '-':
        partialWord.insert(0, leftSquare)
        partialWordStr = leftSquare.tile + partialWordStr
        leftSquare = boardHandler.getLeftSquare(leftSquare)

    node = dawg.getNode(partialWordStr)
    if node != None:
        ExtendRight(partialWord, node, anchorSquare)
    return

def LeftPart(partialWord, N, limit, anchorSquare):
    ExtendRight(partialWord, N, anchorSquare)
    if limit > 0:
        for Eletter, Enode in N.edges.items():
            if Eletter in rack:
                #insert tile at anchor square (pushing back the current leftPart --LP[])
                rack.remove(Eletter)

                boardHandler.insertTileAtAnchorSquare(anchorSquare, partialWord, Eletter)
                LeftPart(partialWord, Enode, limit-1, anchorSquare)
                boardHandler.removeTileFromAnchorSquare(partialWord)
                rack.append(Eletter)

def ExtendRight(partialWord, N, square):
    print ' before extend right ', partialWord
    print '  square ', square
    if N.final and (square == None or square.tile == '-'):
        addLegalMove(partialWord)
    if square == None:
        return
    if (square.tile == '-'):
        for Eletter, Enode in N.edges.items():
            if Eletter in rack and Eletter in square.crossCheckSet: #TODO: and (E.letter in square.crossCheckSet)
                rack.remove(Eletter)
                square.tile = Eletter
                partialWord.append(square)
                print ' after extend right ', partialWord
                nextSquare = boardHandler.getRightSquare(square)
                ExtendRight(partialWord, Enode, nextSquare)
                partialWord.pop()
                square.tile = '-'
                rack.append(Eletter)
    if re.match("^[a-z]$", square.tile):
        if square.tile in N.edges:
            Enode = N.edges[square.tile]
            partialWord.append(square)
            print ' after extend right ', partialWord
            nextSquare = boardHandler.getRightSquare(square)
            ExtendRight(partialWord, Enode, nextSquare)
            partialWord.pop()

def addLegalMove(move):
    legalMoves.append(copy.copy(move))

def tallyPoints(move):
    score = 0
    word = ''
    wordBonus = 1
    for square in move:
        word += square.tile
        score += valueMap.get(square.tile.upper()) * int(float(square.letterBonus))
        wordBonus = wordBonus * square.wordBonus
    score = score * wordBonus
    plays[word] = score

def sortMoves():
    playList = [x for x in plays.items()]
    playList.sort(key = lambda x: x[0]) # sort by key
    playList.sort(key = lambda x: x[1]) # sort by value
    for word, score in playList:
        print word, score

def getDawg(gameName):
    """get Directed Acyclic Word Graph for the game"""
    dawg = Dawg()
    try:
        dawg = pickle.load(open('../resources/' + gameName + '/dawg.p', 'rb'))
    except:
        words = open('../resources/' + gameName + '/wordSet.txt', 'rt').read().split()
        words.sort()
        for word in words:
            dawg.insert(word)
        dawg.finish()
        pickle.dump(dawg, open('../resources/' + gameName + '/dawg.p', 'wb'))
    return dawg

if __name__ == '__main__':
    start = time.time()

    # parse the input from command line
    gameName = sys.argv[1]
    getRack()
    print rack

    dawg = getDawg(gameName)
    board = Board()
    boardHandler = BoardHandler(board)

    # find anchor squares and words first with board in initial orientation
    anchorSquares = findAnchorSquares()
    for anchorSquare in anchorSquares:
        findWords(anchorSquare)

    # then change orientation and find anchor squares and words again
    board.orientation = 1
    print 'changing orientation...'
    anchorSquares = findAnchorSquares()
    for anchorSquare in anchorSquares:
        findWords(anchorSquare)

    for move in legalMoves:
        tallyPoints(move)

    sortMoves()
    print time.time() - start
