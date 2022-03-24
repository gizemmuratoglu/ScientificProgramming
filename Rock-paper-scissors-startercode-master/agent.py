'''
Rock-Paper-Scissors game
Starter code for Stanford CME 193
author: Sven Schmit
'''

import random

class Agent:
    def getMove(self, moves_other, moves_self):
        pass


class InstructorAgent(Agent):
    def __init__(self):
        p_rock = random.random()
        p_scissors = random.random()
        p_paper = random.random()
        p_total = p_rock + p_scissors + p_paper

        self.p_rock = p_rock / p_total
        self.p_scissors = self.p_rock + p_scissors / p_total
        global prock
        global pscissor
        prock=self.p_rock
        pscissor=self.p_scissors



    def getMove(self, moves_other, moves_self):
        random_move = random.random()
        if random_move < self.p_rock:
            return 'r'
        elif random_move < self.p_scissors:
            return 's'
        else:
            return 'p'


class MyAgent(Agent):
  def getMove(self, moves_other, moves_self):
      random_move = random.random()
      if random_move < prock:
          return 's'
      elif random_move < pscissor:
          return 's'
      else:
          return 'p'


class HumanAgent(Agent):
    def getMove(self, moves_other, moves_self):
        moveTypes = ['r', 'p', 's']
        move = ''
        while True:
            theMove = str(input('\tEnter your move as r,p or s >>  ')).lower()
            if theMove in moveTypes:
                move = theMove
                break
            else:
                print('INVALID MOVE')
        return move

