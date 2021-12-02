import numpy
import pylab
import random

class GameOfLife:

   def __init__(self, s=3, T=5):
      """ Set up Game"""
      #Initialize old and new board.
      #Creates an n by n grid.
      #1 represents live cells, 0 represents dead cells.
      #T represents max number of generations
      self.s = s
      self.old_grid = numpy.zeros(s*s, dtype='i').reshape(s,s)
      self.new_grid = numpy.zeros(s*s, dtype='i').reshape(s,s)
      self.T = T 

      # Configuration of inital board is set up.
      for i in range(0, self.s):
         for j in range(0, self.s):
            if(random.randint(0, 100) < 40):
               self.old_grid[i][j] = 1
            else:
               self.old_grid[i][j] = 0
      
   def live_neighbors(self, i, j):
      #n represents number of living neighbors 
      n = 0 
      #Loop over all the neighbors.
      for x in [i-1, i, i+1]:
         for y in [j-1, j, j+1]:
            if(x == i and y == j):
               continue 
            if(x != self.s and y != self.s):
               n += self.old_grid[x][y]
            #The remaining branches handle the case where the neighbor is off the end of the grid.
            #In this case, we loop back round such that the grid becomes a "toroidal array".
            elif(x == self.s and y != self.s):
               n += self.old_grid[0][y]
            elif(x != self.s and y == self.s):
               n += self.old_grid[x][0]
            else:
               n += self.old_grid[0][0]
      return n

   def play(self):
      """ Play The Game of Life. """

      # Write the initial configuration to file.
      pylab.pcolormesh(self.old_grid)
      pylab.colorbar()
      pylab.savefig("generation0.png")

      t = 1 # Current time level
      #How often generation summaries are printed
      write_frequency = 1 
      while t <= self.T: 
         print ("Current Generation: %d" % t)

         
         for i in range(self.s):
            for j in range(self.s):
               live = self.live_neighbors(i, j)
               if(self.old_grid[i][j] == 1 and live < 2):
                  self.new_grid[i][j] = 0 # Dead from starvation.
               elif(self.old_grid[i][j] == 1 and (live == 2 or live == 3)):
                  self.new_grid[i][j] = 1 # Continue living.
               elif(self.old_grid[i][j] == 1 and live > 3):
                  self.new_grid[i][j] = 0 # Dead from overcrowding.
               elif(self.old_grid[i][j] == 0 and live == 3):
                  self.new_grid[i][j] = 1 # Alive from reproduction.

         # Output the new configuration.
         if(t % write_frequency == 0):
            pylab.pcolormesh(self.new_grid)
            pylab.savefig("generation%d.png" % t)

         # The new configuration becomes the old configuration for the next generation.
         self.old_grid = self.new_grid.copy()

         #Continues to next generation
         t += 1

if(__name__ == "__main__"):
   game = GameOfLife(s = 5, T = 15)
   game.play()
