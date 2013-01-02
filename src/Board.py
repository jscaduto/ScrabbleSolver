import Square
import re

class Board:

    def __init__(self): # TODO: add gameType as input
        self.rows = 0
        self.cols = 0
        self.orientation = 0

        self.grid = self.__setBoardLayout()
        self.__setGameState()

    def __str__(self):
        buffer = ''
        if self.orientation == 0:
            buffer += '-'*((self.cols * 2) + 1) + '\n'
            for y in range(self.rows):
                for x in range(self.cols):
                    buffer += '|' + str(self.grid[y][x])
                buffer += '|\n'
                buffer += '-'*((self.cols * 2) + 1) + '\n'
        else:
            buffer = ''
            buffer += '-'*((self.rows * 2) + 1) + '\n'
            for x in range(self.cols):
                for y in range(self.rows):
                    buffer += '|' + str(self.grid[y][x])
                buffer += '|\n'
                buffer += '-'*((self.rows * 2) + 1) + '\n'
        return buffer

    def __setBoardLayout(self):
        boardLayout = open('../resources/wordsWithFriends/layout.txt').read().split()
        self.rows = int(boardLayout[-2])
        self.cols = int(boardLayout[-1])

        grid = [[Square.Square(x,y) for x in range(self.cols)] for y in range(self.rows)]
        for y, rowInputString in enumerate(boardLayout[1:-2:2]):
            rowInputList = re.findall('\-|DW|TW|DL|TL', rowInputString)
            for x, value in enumerate(rowInputList):
                if value == 'DW':
                    grid[y][x].wordBonus = 2
                elif value == 'TW':
                    grid[y][x].wordBonus = 3
                elif value == 'DL':
                    grid[y][x].letterBonus = 2
                elif value == 'TL':
                    grid[y][x].letterBonus = 3
        return grid

    def __setGameState(self):
        boardState = open('../resources/wordsWithFriends/state.txt').read().split()
        for y, rowInputString in enumerate(boardState[1::2]):
            rowInputList = re.findall('\-|[a-z]', rowInputString)
            for x, squareState in enumerate(rowInputList):
                self.grid[y][x].tile = squareState
                self.grid[y][x].wordBonus = 1
                self.grid[y][x].letterBonus = 1

    def specialPrint(self):
        """docstring for specialPrint"""
        pass
