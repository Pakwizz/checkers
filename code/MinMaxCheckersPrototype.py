#!/usr/bin/python

'''''''''''''''''''''''''''''''''''''''
' Concepts in Artifical Intelligence
' Rowan University, Fall 2015
' Professor: 	Dr. Tinkham
'
' Submitted By:	Arafat Qureshi, Zabih Shinwari & Quadii McMillan
' Date: October 27, 2015
' Semester Project Prototype - MiniMax Implelentation for Checkers
'
'''''''''''''''''''''''''''''''''''''''''

#import required libraries
import math
import copy
import time
import datetime

# Minimax algorithm draft
#def MiniMax(node, depth, maximize):
#   decendant = 0
#    if we are at the leaf node or root node
#    calculate and return the heuristic value of the node
#    if(DecendantExist(node) == False):
#        return GetHeuristicValue(node, board_state)
#    return the value for the best move for this branch of the tree
#    if (maximizing_player):
#    	best_value = -(infinity)
#    	child = node
#    	while (child = GetDecendant(node)):
#   		node_value = MiniMax(child, depth-1, maximizing_player)
#    		max_value = maximum(max_value, node_value)
#    		if max_value <= :
#    			pass
#    	return max_value
#   else
#    	return the minimum value for each child node
#    	min_value = infinity
#    	while (child = GetDecendant()):
#    		node_value = MiniMax(child, depth-1, minimizing_player)
#    		max_value = minimum(max_value, node_value)
#    	return max_value

def DecendantExists(node):
	if(node.next <> nullptr):
		return true
	return false

# this functin calculates a very simple heurstic
# we intend to flesh this algorithm our more as we move forward
def GetHeuristicValue(node, board_state):
	return num_black - num_red

'''
 This piece of code was lifted from the Python Wiki page. It works well and paints a nice checkers board.
 Since we intend to implement a GUI that can be used on tablets, our interface will be somewhat different.
 However, we expect this code will be useful as a reference tool.
 '''
def make_display(self):
        """This function will create the Canvas for the board, and then the board.
        The variables required by this function are:
        self.master, self.SQUARESIZE."""
        foo=self.SQUARESIZE*8 #calculation saver
        self.c=Canvas(self.master, height=foo, width=foo)
        self.message=Label(self.master, text="", bd=2, relief=RAISED,\
                           font=("", "10", ""))
        self.make_checker_squares(0,7,"bisque")
        self.make_checker_squares(1,8,"green3", "squares")

        history_scroll=Scrollbar(self.master)
        self.history_display=Listbox(self.master, yscrollcommand=history_scroll.set)
        history_scroll.config(command=self.history_display.yview)
        self.history_display.bind("<Double-Button-1>", self.go_to_move)
        self.c.grid(row=1, column=0)
        self.message.grid(row=0, column=0, columnspan=3, pady=5)
        self.history_display.grid(row=1, column=1, sticky=N+S)
        history_scroll.grid(row=1, column=2, sticky=N+S)
        
        for baz in self.c.find_overlapping(self.SQUARESIZE*1.5,\
                                           self.SQUARESIZE*0.5,\
                                           self.SQUARESIZE*1.5,\
                                           self.SQUARESIZE*0.5):
            if self.c.type(baz)=="rectangle":
                self.upper_corner_square=baz

'''''''''''''''
The following are some of the function we have identified as likely pieces 
needed to produce a complete checkers game.

'''''''''''''''
# create checkerboard
def CreateBoard():
    pass

# this function will build a node tree of depth N
def BuildNodeTree():	
	pass

# return list of valid moves for given board state
def GetMoves(player):	
	pass

# get move for a given piece
def GetMoves(player):
	pass

# return valid jump moves for a given piece
def GetJumpMoves(player):	
		pass
# graphically display pieces on the board
def ShowPieces():
	pass

if __name__ == "__main__":
    pass
