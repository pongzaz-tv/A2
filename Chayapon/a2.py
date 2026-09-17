from processing import *
import random

grid_size = 50
center_board_x = 250
center_board_y = 200

PALETTE =  [(245, 93, 62),   # Orange-Red
            (66, 133, 244),  # Blue
            (52, 168, 83),   # Green
            (251, 188, 5),   # Yellow
            (171, 71, 188)]  # Purple

#SHAPE_TEMPLATES =  


class Board:
    cbx = cby = gs = gr = 0

    def __init__(self,center_board_x,center_board_y,grid_size):
        self.cbx = center_board_x -200
        self.cby = center_board_y -175
        self.gs = grid_size
        self.gr = 50

    def draw_board(self): #loop draw ทำให้
        draw_cbx = self.cbx
        draw_cby = self.cby
        ix = iy =0
        while(ix <= 8):
            line(draw_cbx,draw_cby,draw_cbx,draw_cby+400)
            draw_cbx += 50
            ix += 1
        draw_cbx = self.cbx
        while(iy <= 8):
            line(draw_cbx,draw_cby,draw_cbx+400,draw_cby)
            draw_cby += 50
            iy += 1




"""     
class Piece:
    def __init__():
"""
def setup():
    global board
    size(500,600)
    frameRate(60)
    board = Board(center_board_x,center_board_y,grid_size)

def draw():
    background(225)
    #ellipse(250,300,40,40) #system tester
    
    board.draw_board()

#def can_place():

#def place():

#def clear_lines():

#def mousePressed():

#def mouseDragged():

#def mouseReleased():

run()