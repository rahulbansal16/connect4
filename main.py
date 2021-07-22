"""
Connect Four is a two-player connection board game, 
in which the players choose a color and then take turns dropping colored discs into a seven-column, 
six-row vertically suspended grid. 

The pieces fall straight down, occupying the lowest available space within the column. 
The objective of the game is to be the first to form a horizontal, vertical, or diagonal line of four of one's own discs. 

https://en.wikipedia.org/wiki/Connect_Four#/media/File:Connect_Four.gif

phase 1: filling the board (no win-state checks)
phase 2: win-state checks
phase 3: AI players (bonus)
"""
# 0
# [
#     [' ', ' ', ' ']
#     [' ', ' ']
#  ]
class Connect:

    def __init__(self):
        # super().__init__()
        self.columns = 7
        self.rows = 6 
        self.positions = [0 for x in range(self.columns)]
        self.board = [ [ ' '  for x in range(self.columns) ] for y in range(self.rows)]
        self.lastMove = None
        self.lastMarker = None

    def getColumnCount(self):
        return self.columns
        
    def indexOutOfRange(self, x,y):
        if x  < 0 or y < 0 :
            return True
        if x >= self.rows or y >= self.columns:
            return True
        return False
        
    def bfs(self, x, y, direction, visited, marker):
        
        visited[(x,y)] = True
        ct = 1
        print(self.lastMarker,x,y,ct)
        for i in range(2):
            xx = x + direction[i][0]
            yy = y + direction[i][1]
            if not visited[(xx,yy)]:
                if not self.indexOutOfRange(xx,yy):
                    if self.board[xx][yy] == marker:
                        ct += self.bfs(xx, yy, direction, visited, marker)
        return ct        
        
    # def bfs(self, x, y, direction, visited, ct, marker):
    #     print(self.lastMarker,x,y,ct)
    #     if ct == 4:
    #         return True
    #     visited[(x,y)] = True
    #     p = False
    #     for i in range(2):
    #         xx = x + direction[i][0]
    #         yy = y + direction[i][1]
    #         if not visited[(xx,yy)]:
    #             if not self.indexOutOfRange(xx,yy):
    #                 if self.board[xx][yy] == marker:
    #                     p = p or self.bfs(xx, yy, direction, visited, ct  + 1, marker)
    #     return p

    def isHorizontal(self, x, y, marker):
        import collections
        visited  = collections.defaultdict(lambda: False)
        return self.bfs(x, y, [ [ 0, 1], [0, -1]], visited, marker )
    
    def isVertical(self, x, y, marker):
        import collections
        visited  = collections.defaultdict(lambda: False)
        return self.bfs(x, y, [ [1, 0], [-1, 0]], visited, marker )
    
    def isWon(self):
        if self.lastMove == None:
            return False
        return self.isHorizontal(self.lastMove[0], self.lastMove[1], self.lastMarker) == 4 or self.isVertical(self.lastMove[0], self.lastMove[1], self.lastMarker) == 4

    
    def makeMove(self, position, marker):
        
        if self.positions[position] >= self.rows:
            return False
        
        x = self.positions[position]
        y = position
        self.lastMarker = marker
        self.lastMove = (x, y)
        print(self.lastMove, self.lastMarker)
        self.board[self.positions[position]][position] = marker
        self.positions[position] += 1
        
        return True
        
    def display(self):
        for line in self.board[::-1]:
            print(line)
        print('\n')

    def isComplete(self):
      ct = 0
      if self.isWon():
          print("game won")
          return True
      for x in self.positions:
        ct += x 
      if ct == self.rows * self.columns:
        return True

      return False

class Player:
    
    def __init__(self, marker):
        self.marker = marker
    
    def getMove(self, n):
        # if self.marker == "X":
        #     return 0
        # else:
        #     return 1
        import random
        return random.randint(0, n-1)

    def getMarker(self):
      return self.marker
        
class Game:
    
    def __init__(self, p1, p2, connect):
        self.p1  = p1
        self.p2 = p2
        self.connect = connect
    
    def play(self, n):
      turn = 0
      self.connect.display()

      while not self.connect.isComplete():
        m = -1

        if turn == 0:
          while True:
            m = self.p1.getMove(n)
            if self.connect.makeMove(m, self.p1.getMarker()):
              break
          turn = 1
        else:
          while True:
            m = self.p2.getMove(n)
            if self.connect.makeMove(m, self.p2.getMarker()):
              break          
          turn = 0

        self.connect.display()

        
print('Hi ')
p1 = Player('X')
p2 = Player('O')

c = Connect()
g = Game(p1, p2, c)
g.play(c.getColumnCount())


# c.makeMove(0,'X')
# print('\n')
# c.display()
