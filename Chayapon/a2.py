#import random

game_over = False
p1 = p2 = p3 = False
p1_placed = p2_placed = p3_placed = False
chancep1 = chancep2 = chancep3 = 1
a = [0, 0, 0]
grid_size = 50
center_board_x = 250
center_board_y = 200
num_shape = num_piece = 0
combo_streak = score = combo_timer = combo_y = 0
status_notice = ""
status_timer = 0
SAVE_FILE = "savegame.txt"
lines_points = False
board_info =   [[0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0]]

shape_dot = [[1]] #0

shape_2_downl = [[1,1]] #1
shape_2_upl =   [[1], #2
                 [1]]

shape_3_downl = [[1,1,1]] #3
shape_3_upl = [[1],[1],[1]] #4

shape_4_full =  [[1,1], #5
                 [1,1]]
shape_4_downl = [[1,1,1,1]] #6
shape_4_upl =  [[1],[1],[1],[1]] #7

shape_4_left_topr = [[1,1], #8
                    [1,0]] 
shape_4_left_topl = [[1,1], #9
                     [0,1]]
shape_4_left_downr = [[1,0], #10
                      [1,1]]  
shape_4_left_downl = [[0,1], #11
                      [1,1]] 

shape_9_full = [[1,1,1],
                [1,1,1], #12
                [1,1,1]]



SHAPE_TEMPLATES = [shape_dot,shape_2_downl,shape_2_upl,shape_3_downl,shape_3_upl,shape_4_full,shape_4_downl,shape_4_upl,shape_4_left_topr,shape_4_left_topl,shape_4_left_downr,shape_4_left_downl,shape_9_full]

class Board:
    cbx = cby = gs = gr = 0
    board_info = []
    def __init__(self, center_board_x, center_board_y, grid_size, board_info):
        self.cbx = center_board_x - 200
        self.cby = center_board_y - 175
        self.gs = grid_size
        self.gr = 50
        self.board_info = board_info

    def draw_board(self):
        draw_cbx = self.cbx
        draw_cby = self.cby
        ix = iy = 0
        fill(0,0,0)
        while (ix <= 8):
            line(draw_cbx, draw_cby, draw_cbx, draw_cby + 400)
            draw_cbx += 50
            ix += 1
        draw_cbx = self.cbx
        while (iy <= 8):
            line(draw_cbx, draw_cby, draw_cbx + 400, draw_cby)
            draw_cby += 50
            iy += 1

        r = 0
        while (r < 8):
            c = 0
            while (c < 8):
                if (self.board_info[r][c] == 1):
                    ellipse(self.cbx + (c * 50) + 25, self.cby + (r * 50) + 25, 40, 40)
                c += 1
            r += 1
        fill(255)

    def check_grid(self, x, y):
        matrix_x = 0
        matrix_y = 0
        positon = [0, 0]
        if (x > 50 and x < 100):
            matrix_x = 1
        elif (x > 100 and x < 150):
            matrix_x = 2
        elif (x > 150 and x < 200):
            matrix_x = 3
        elif (x > 200 and x < 250):
            matrix_x = 4
        elif (x > 250 and x < 300):
            matrix_x = 5
        elif (x > 300 and x < 350):
            matrix_x = 6
        elif (x > 350 and x < 400):
            matrix_x = 7
        elif (x > 400 and x < 450):
            matrix_x = 8

        if (y > 25 and y < 75):
            matrix_y = 1
        elif (y > 75 and y < 125):
            matrix_y = 2
        elif (y > 125 and y < 175):
            matrix_y = 3
        elif (y > 175 and y < 225):
            matrix_y = 4
        elif (y > 225 and y < 275):
            matrix_y = 5
        elif (y > 275 and y < 325):
            matrix_y = 6
        elif (y > 325 and y < 375):
            matrix_y = 7
        elif (y > 375 and y < 425):
            matrix_y = 8
        positon[0] = matrix_x
        positon[1] = matrix_y
        return positon

    def can_place(self, piece, position):
        if (position[0] == 0 or position[1] == 0):
            return False
        start_x = position[0] - 1
        start_y = position[1] - 1
        bms = piece.bms
        i = 0
        while (i < len(bms)):
            j = 0
            while (j < len(bms[i])):
                if (bms[i][j] == 1):
                    target_x = start_x + j
                    target_y = start_y + i
                    if (target_x >= 8 or target_y >= 8):
                        return False
                    if (self.board_info[target_y][target_x] == 1):
                        return False
                j += 1
            i += 1
        return True

    def place(self, piece, position, piece_points):
        global score
        if (self.can_place(piece, position)):
            if (piece_points == 0):
                score += 10
            elif (piece_points > 0 and piece_points < 3):
                score += 20
            elif (piece_points > 2 and piece_points < 5):
                score += 30
            elif (piece_points > 4 and piece_points < 8):
                score += 40
            elif (piece_points > 7 and piece_points < 12):
                score += 30
            elif (piece_points == 12):
                score += 90
            start_x = position[0] - 1
            start_y = position[1] - 1
            bms = piece.bms
            i = 0
            while (i < len(bms)):
                j = 0
                while (j < len(bms[i])):
                    if (bms[i][j] == 1):
                        self.board_info[start_y + i][start_x + j] = 1
                    j += 1
                i += 1
            self.clear_lines()
            return True
        else:
            return False
    
    def clear_lines(self):
        global score, lines_points
        ix=0
        
        while(ix<len(self.board_info)):
            jx=sumx=0
            while(jx<len(self.board_info[ix])):
                sumx+=self.board_info[ix][jx]
                jx+=1
            if(sumx == 8):
                self.board_info[ix] = [0,0,0,0,0,0,0,0] 
                score += 100
                lines_points = True
            ix+=1
        jy=0
        while(jy<len(self.board_info)):
            iy=sumy=0
            while(iy<len(self.board_info)):
                sumy+=self.board_info[iy][jy]
                iy+=1
            if(sumy == 8):
                clr=0
                while(clr<len(self.board_info)):
                    self.board_info[clr][jy] = 0
                    clr+=1
                score += 100
                lines_points = True
            jy+=1

class Piece:
    bms = []
    def __init__(self, block_matrix_scheme):
        self.bms = block_matrix_scheme

    def draw_piece(self, x, y):
        i = 0
        while (i < len(self.bms)):
            j = 0
            while (j < len(self.bms[i])):
                if (self.bms[i][j] == 1):
                    bx = x + (j * 50)
                    by = y + (i * 50)
                    fill(0,0,0)
                    line(bx, by, bx + 50, by)
                    line(bx, by + 50, bx + 50, by + 50)
                    line(bx, by, bx, by + 50)
                    line(bx + 50, by, bx + 50, by + 50)
                j += 1
            i += 1

    def reset_pos(self):
        global p1, p2, p3
        p1 = False
        p2 = False
        p3 = False

def check_game_over():
    global game_over
    placed = [p1_placed, p2_placed, p3_placed]
    if (p1_placed and p2_placed and p3_placed):
        return
    over = True
    index = 0
    while (index < len(a)):
        if (placed[index] == False):
            r = 1
            while (r <= 8):
                c = 1
                while (c <= 8):
                    position = [c, r]
                    if (board.can_place(SHAPE_TEMPLATES[a[index]], position) == True):
                        over = False
                        c = 9
                        r = 9
                    c += 1
                r += 1
        index += 1

    if (over):
        game_over = True

def save_game():
    global status_notice, status_timer
    board_info = Board.board_info
    i = 0
    try:
        with open(SAVE_FILE, "w") as file:
            while(i<len(board_info)-1):
                file.write(board_info[i],end="","/",end="")
                i += 1
            file.write(board_info[7],"\n")
            file.write(score,end="",",",end="",combo_streak,"\n")
            if(p1_placed==True):
                file.write(SHAPE_TEMPLATES[a[0]],end="",":",int(random(0,5)),end="")
            else:
                file.write("EMPTY",end="")
            file.write(";",end="")
            if(p2_placed==False):
                file.write(SHAPE_TEMPLATES[a[1]],end="",":",int(random(0,5)),end="")
            else:
                file.write("EMPTY",end="")
            if(p3_placed==False):
                file.write(SHAPE_TEMPLATES[a[2]],end="",":",int(random(0,5)),end="")
            else:
                file.write("EMPTY",end="")
        status_notice = "Game Saved"
        status_timer = 60
    except Exception as e:
        status_notice = "Save Failed"
        status_timer = 60

def load_game():
    global board, score, combo_streak, a, num_piece
    global p1, p2, p3, p1_placed, p2_placed, p3_placed
    global chancep1, chancep2, chancep3, game_over
    global status_notice, status_timer



def setup():
    global board
    size(500, 600)
    frameRate(60)
    board = Board(center_board_x, center_board_y, grid_size, board_info)
    i = 0
    while (i < len(SHAPE_TEMPLATES)):
        SHAPE_TEMPLATES[i] = Piece(SHAPE_TEMPLATES[i])
        i += 1


def draw():
    global num_shape, num_piece, a, p1, p2, p3, p1_placed, p2_placed, p3_placed, chancep1, chancep2, chancep3, lines_points, combo_streak, combo_timer, combo_y, score
    background(225)
    board.draw_board()
    position = board.check_grid(mouseX, mouseY)

    fill(0,0,0)
    textSize(22)
    text("Score: "+str(score),50,20)
    text("[S] Save  |  [L] Load",280,20)

    if (num_piece == 0):
        a = [int(random(0, 13)), int(random(0, 13)), int(random(0, 13))]
        num_piece = 3
        p1 = p2 = p3 = p1_placed = p2_placed = p3_placed = False
        chancep1 = chancep2 = chancep3 = 1

    if (p1_placed == False and chancep1 == 1):
        if (p1 == False):
            SHAPE_TEMPLATES[a[0]].draw_piece(15, 440)
        else:
            if board.can_place(SHAPE_TEMPLATES[a[0]], position):
                fill(200, 200, 200)
                bms = SHAPE_TEMPLATES[a[0]].bms
                i = 0
                while (i < len(bms)):
                    j = 0
                    while (j < len(bms[i])):
                        if (bms[i][j] == 1):
                            ellipse(board.cbx + (position[0] - 1 + j) * 50 + 25, board.cby + (position[1] - 1 + i) * 50 + 25, 40, 40)
                        j += 1
                    i += 1
                fill(255)
            SHAPE_TEMPLATES[a[0]].draw_piece(mouseX - 25, mouseY - 25)

    if (p2_placed == False and chancep2 == 1):
        if (p2 == False):
            SHAPE_TEMPLATES[a[1]].draw_piece(175, 440)
        else:
            if board.can_place(SHAPE_TEMPLATES[a[1]], position):
                fill(200, 200, 200)
                bms = SHAPE_TEMPLATES[a[1]].bms
                i = 0
                while (i < len(bms)):
                    j = 0
                    while (j < len(bms[i])):
                        if (bms[i][j] == 1):
                            ellipse(board.cbx + (position[0] - 1 + j) * 50 + 25, board.cby + (position[1] - 1 + i) * 50 + 25, 40, 40)
                        j += 1
                    i += 1
                fill(255)
            SHAPE_TEMPLATES[a[1]].draw_piece(mouseX - 25, mouseY - 25)

    if (p3_placed == False and chancep3 == 1):
        if (p3 == False):
            SHAPE_TEMPLATES[a[2]].draw_piece(335, 440)
        else:
            if board.can_place(SHAPE_TEMPLATES[a[2]], position):
                fill(200, 200, 200)
                bms = SHAPE_TEMPLATES[a[2]].bms
                i = 0
                while (i < len(bms)):
                    j = 0
                    while (j < len(bms[i])):
                        if (bms[i][j] == 1):
                            ellipse(board.cbx + (position[0] - 1 + j) * 50 + 25, board.cby + (position[1] - 1 + i) * 50 + 25, 40, 40)
                        j += 1
                    i += 1
                fill(255)
            SHAPE_TEMPLATES[a[2]].draw_piece(mouseX - 25, mouseY - 25)

    text(num_piece, mouseX, mouseY)
    check_game_over()
    if(game_over):
        fill(0, 0, 0, 180)
        textSize(36)
        text("GAME OVER", width / 2 - 110, height / 2 - 20)

    if lines_points:
        combo_streak += 1
        score += (combo_streak - 1) * 50
        combo_y = 255
        combo_timer = 100
        lines_points = False

    if combo_timer > 0:
        fill(225, 0, 0)
        textSize(22)
        if combo_streak >= 2:
            text("STREAK X" + str(combo_streak) + " +" + str(100 + (combo_streak - 1) * 50), 150, combo_y)
        else:
            text("Line clear + 100", 170, combo_y)
        combo_y -= 2
        combo_timer -= 2


    if (status_timer > 0):
        text(status_notice,175,255)
        status_timer -= 1

def keyPressed():
    if key in ('s', 'S'):
        save_game()
    elif key in ('l', 'L'):
        load_game()

def mousePressed():
    global p1, p2, p3, p1_placed, p2_placed, p3_placed, chancep1, chancep2, chancep3
    if (p1_placed == False and chancep1 == 1):
        if (mouseX < 175 and mouseY > 440):
            p1 = True
            p2 = False
            p3 = False
    if (p2_placed == False and chancep2 == 1):
        if (mouseX > 175 and mouseX < 335 and mouseY > 440):
            p2 = True
            p1 = False
            p3 = False
    if (p3_placed == False and chancep3 == 1):
        if (mouseX > 335 and mouseY > 440):
            p3 = True
            p1 = False
            p2 = False

def mouseDragged():
    global p1, p2, p3, p1_placed, p2_placed, p3_placed, chancep1, chancep2, chancep3
    if (p1_placed == False and chancep1 == 1):
        if (mouseX < 175 and mouseY > 440 and p2 == False and p3 == False):
            p1 = True
    if (p2_placed == False and chancep2 == 1):
        if (mouseX > 175 and mouseX < 335 and mouseY > 440 and p1 == False and p3 == False):
            p2 = True
    if (p3_placed == False and chancep3 == 1):
        if (mouseX > 335 and mouseY > 440 and p1 == False and p2 == False):
            p3 = True
        
def mouseReleased():
    global p1, p2, p3, p1_placed, p2_placed, p3_placed, chancep1, chancep2, chancep3, num_piece, a, board
    position = board.check_grid(mouseX, mouseY)

    if (p1 == True and chancep1 == 1):
        p1_placed = board.place(SHAPE_TEMPLATES[a[0]], position, a[0])
        if (p1_placed == True):
            num_piece -= 1
            chancep1 = 0
            p1 = False
        else:
            SHAPE_TEMPLATES[a[0]].reset_pos()

    if (p2 == True and chancep2 == 1):
        p2_placed = board.place(SHAPE_TEMPLATES[a[1]], position, a[1])
        if (p2_placed == True):
            num_piece -= 1
            chancep2 = 0
            p2 = False
        else:
            SHAPE_TEMPLATES[a[1]].reset_pos()

    if (p3 == True and chancep3 == 1):
        p3_placed = board.place(SHAPE_TEMPLATES[a[2]], position, a[2])
        if (p3_placed == True):
            num_piece -= 1
            chancep3 = 0
            p3 = False
        else:
            SHAPE_TEMPLATES[a[2]].reset_pos()