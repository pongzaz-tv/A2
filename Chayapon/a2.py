from processing import *
import random

grid_size = 50
center_board_x = 250
center_board_y = 200
board_info =   [[0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0]]

shape_dot = [[1]]

shape_2_downl = [[1,1]]
shape_2_upl =   [[1],
                 [1]]

shape_3_downl = [[1,1,1]]
shape_3_upl = [[1],[1,[1]]]

shape_4_full =  [[1,1],
                 [1,1]]
shape_4_downl = [[1,1,1,1]]
shape_4_upl =  [[1],
                [1],
                [1],
                [1]]
shape_4_left_topr = [[1,1],
                    [1,0]] 
shape_4_left_topl = [[1,1],
                     [0,1]]
shape_4_left_downr = [[1,0],
                      [1,1]]  
shape_4_left_downl = [[0,1],
                      [1,1]] 

shape_9_full = [[1,1,1],
                [1,1,1],
                [1,1,1]]

PALETTE =  [(245, 93, 62),   # Orange-Red
            (66, 133, 244),  # Blue
            (52, 168, 83),   # Green
            (251, 188, 5),   # Yellow
            (171, 71, 188)]  # Purple

SHAPE_TEMPLATES = [shape_dot,shape_2_downl,shape_2_upl,shape_3_downl,shape_3_upl,shape_4_full,shape_4_downl,shape_4_upl,shape_4_left_topr,shape_4_left_topl,shape_4_left_downr,shape_4_left_downl,shape_9_full]

class Board:
    cbx = cby = gs = gr = 0
    board_info = []
    def __init__(self,center_board_x,center_board_y,grid_size,board_info):
        self.cbx = center_board_x -200
        self.cby = center_board_y -175
        self.gs = grid_size
        self.gr = 50
        self.board_info = board_info

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

    def check_grid(self,x,y):
        matrix_x = 0
        matrix_y = 0
        if(x>50 and x<100):
            matrix_x = 1
        elif (x>100 and x<150):
            matrix_x = 2
        elif (x>150 and x<200):
            matrix_x = 3
        elif (x>200 and x<250):
            matrix_x = 4
        elif (x>250 and x<300):
            matrix_x = 5
        elif (x>300 and x<350):
            matrix_x = 6
        elif (x>350 and x<400):
            matrix_x = 7
        elif (x>400 and x<450):
            matrix_x = 8

        if(y>25 and y<75):
            matrix_y = 1
        elif (y>75 and y<125):
            matrix_y = 2
        elif (y>125 and y<175):
            matrix_y = 3
        elif (y>175 and y<225):
            matrix_y = 4
        elif (y>225 and y<275):
            matrix_y = 5
        elif (y>275 and y<325):
            matrix_y = 6
        elif (y>325 and y<375):
            matrix_y = 7
        elif (y>375 and y<425):
            matrix_y = 8
        text(matrix_y,mouseX,mouseY)
        text(matrix_x,mouseX+4,mouseY)

    def can_place(self):



    def place():


radius = 25

class Piece:
    bms = []
    colour = 0
    def __init__(self,block_matrix_scheme,colour):
        self.bms = block_matrix_scheme
        self.colour = colour

def setup():
    global board
    size(500,600)
    frameRate(60)
    board = Board(center_board_x,center_board_y,grid_size,board_info)

def draw():
    background(225)
    ellipse(mouseX,mouseY,radius,radius) #system tester
    is_mouse_pressed()
    board.draw_board()
    board.check_grid(mouseX,mouseY)
    
def is_mouse_pressed():
    global radius
    if mousePressed:
        radius = 12.5
    else:
        radius = 25

#def clear_lines():

#def mouseDragged():

#def mouseReleased():

run()