import tkinter as tk
import random

class Ludo(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.root = master
        self.die = 6
        self.redOnBoard = []
        self.redHome = []
        self.grid()
        self.gui()
        self.board()
        self.player()
        self.com_green()
        self.com_blue()
        self.com_yellow()
        
    def board(self):
        red = ['0,0', '0,1', '0,2', '0,3', '0,4', '0,5', '1,0', '1,5', '2,0', '2,5', '3,0', '3,5', '4,0', '4,5', '5,0', '5,1', '5,2', '5,3', '5,4', '5,5', '6,1', '7,1', '7,2', '7,3', '7,4', '7,5', '7,6']
        green = ['0,9', '0,10', '0,11', '0,12', '0,13', '0,14', '1,9', '1,14', '2,9', '2,14', '3,9', '3,14', '4,9', '4,14', '5,9', '5,10', '5,11', '5,12', '5,13', '5,14', '1,7', '1,8', '2,7', '3,7', '4,7', '5,7', '6,7']
        blue = ['9,0', '9,1', '9,2', '9,3', '9,4', '9,5', '10,0', '10,5', '11,0', '11,5', '12,0', '12,5', '13,0', '13,5', '14,0', '14,1', '14,2', '14,3', '14,4', '14,5', '13,6', '13,7', '12,7', '11,7', '10,7', '9,7', '8,7']
        yellow = ['9,9', '9,10', '9,11', '9,12', '9,13', '9,14', '10,9', '10,14', '11,9', '11,14', '12,9', '12,14', '13,9', '13,14', '14,9', '14,10', '14,11', '14,12', '14,13', '14,14', '8,13', '7,13', '7,12', '7,11', '7,10', '7,8', '7,9']
        self.squares = {}
        for board_row in range(15):
            for board_col in range(15):
                can = tk.Canvas(self, width = 50, height = 50, bg = 'white')
                can.grid(row = board_row, column = board_col)
                can.row = board_row
                can.col = board_col
                can.on = False
                self.squares[(board_row, board_col)] = can
                #colored square
                if str(board_row)+','+str(board_col) in red:
                    can.config(bg = 'red')
                if str(board_row)+','+str(board_col) in blue:
                    can.config(bg = 'blue')
                if str(board_row)+','+str(board_col) in green:
                    can.config(bg = 'green')
                if str(board_row)+','+str(board_col) in yellow:
                    can.config(bg = 'yellow')
                #arrows
                if board_row == 6 and board_col == 8:
                    can.create_polygon(50,0,0,0,0,50, fill = 'green')
                    can.create_polygon(0,50,50,50,50,0, fill = 'yellow')
                if board_row == 8 and board_col == 6:
                    can.create_polygon(50,0,0,0,0,50, fill = 'red')
                    can.create_polygon(0,50,50,50,50,0, fill = 'blue')
                if board_row == 6 and board_col == 6:
                    can.create_polygon(0,50,50,50,0,0, fill = 'red')
                    can.create_polygon(0,0,50,50,50,0, fill = 'green')
                if board_row == 8 and board_col == 8:
                    can.create_polygon(0,50,50,50,0,0, fill = 'blue')
                    can.create_polygon(0,0,50,50,50,0, fill = 'yellow')
                if board_row == 7 and board_col == 7:
                    can.create_polygon(0,0,0,50,25,25, fill = 'red')
                    can.create_polygon(0,50,50,50,25,25, fill = 'blue')
                    can.create_polygon(50,50,50,0,25,25, fill = 'yellow')
                    can.create_polygon(0,0,50,0,25,25, fill = 'green')

                can.bind('<Button-1>', self.move_piece)

    def move_piece(self, event):
        home = [(2,2),(2,3),(3,2),(3,3)]
        legalMoves = [(6,0), (6,1), (6,2), (6,3), (6,4), (6,5), (5,6), (4,6), (3,6), (2,6), (1,6), (0,6),
                       (0,7), (0,8), (1,8), (2,8), (3,8), (4,8), (5,8), (6,9), (6,10), (6,11), (6,12), (6,13), (6,14),
                       (7,14), (8,14), (8,13), (8,12), (8,11), (8,10), (8,9), (9,8), (10,8), (11,8), (12,8), (13,8), (14,8),
                       (14,7), (14,6), (13,6), (12,6), (11,6), (10,6), (9,6), (8,5), (8,4), (8,3), (8,2), (8,1), (8,0), (7,0)]
        if self.die == 6:
            for i in self.redHome:
                i.on =  True
            print(self.squares[(event.widget.row,event.widget.col)].gettags(red))
        if event.widget.on:
            if (event.widget.row,event.widget.col) in home:
                current = self.squares[legalMoves[1]]
                current.create_oval(5,5,45,45, fill = 'red', tags = 'red')
                current.on = True
                print(current)
                self.redHome.remove(red)

            if (event.widget.row,event.widget.col) in legalMoves:
                current = self.squares[(event.widget.row,event.widget.col)]
                idx = (legalMoves.index((event.widget.row,event.widget.col)) + self.die) % len(legalMoves)
                if 6 > idx >= 0 and 51 < legalMoves.index((event.widget.row,event.widget.col)) + self.die and 'red' in self.squares[(event.widget.row,event.widget.col)].gettags(red):
                    nextPlace = self.squares[(7,5)]
                else:
                    nextPlace = self.squares[legalMoves[idx]]
                current.delete('red')
                current.on = False
                nextPlace.create_oval(5,5,45,45, fill = 'red', tags = 'red')
                nextPlace.on = True
            self.die = 0
            red1.on = False
            red2.on = False
            red3.on = False
            red4.on = False

    def roll_die(self):
        self.die = random.randint(1,6)
        self.gui()
    
    def gui(self):
        frame = tk.Frame(self.root)
        frame.grid(row = 0,column = 1, sticky = 'n')

        playerCan = tk.Canvas(frame, width = 50, height = 50, bg = 'purple')
        playerCan.grid(row = 0, column = 0, sticky='nw')
        
        rollLabel = tk.Label(frame, text = 'You rolled a ' + str(self.die)).grid(row = 1,column = 0, sticky = 'nw')
        rollDie = tk.Button(frame, text = 'Roll die', command = self.roll_die).grid(row = 2,column = 0, sticky = 'we')

    def player(self):
        global red1
        global red2
        global red3
        global red4
        global red
        red1 = self.squares[(2,2)]
        red2 = self.squares[(2,3)]
        red3 = self.squares[(3,2)]
        red4 = self.squares[(3,3)]
        self.redHome.append(red1)
        self.redHome.append(red2)
        self.redHome.append(red3)
        self.redHome.append(red4)
        red = red1.create_oval(5,5,45,45, fill = 'red', tags = 'red')
        red2.create_oval(5,5,45,45, fill = 'red', tags = 'red')
        red3.create_oval(5,5,45,45, fill = 'red', tags = 'red')
        red4.create_oval(5,5,45,45, fill = 'red', tags = 'red')
        red1.on = False
        red2.on = False
        red3.on = False
        red4.on = False

    def com_green(self):
        green1 = self.squares[(2,11)]
        green2 = self.squares[(2,12)]
        green3 = self.squares[(3,11)]
        green4 = self.squares[(3,12)]
        green1.create_oval(5,5,45,45, fill = 'green', tags = 'green')
        green2.create_oval(5,5,45,45, fill = 'green', tags = 'green')
        green3.create_oval(5,5,45,45, fill = 'green', tags = 'green')
        green4.create_oval(5,5,45,45, fill = 'green', tags = 'green')
        green1.on = True
        green2.on = True
        green3.on = True
        green4.on = True

    def com_blue(self):
        blue1 = self.squares[(11,2)]
        blue2 = self.squares[(12,2)]
        blue3 = self.squares[(11,3)]
        blue4 = self.squares[(12,3)]
        blue1.create_oval(5,5,45,45, fill = 'blue', tags = 'blue')
        blue2.create_oval(5,5,45,45, fill = 'blue', tags = 'blue')
        blue3.create_oval(5,5,45,45, fill = 'blue', tags = 'blue')
        blue4.create_oval(5,5,45,45, fill = 'blue', tags = 'blue')
        blue1.on = True
        blue2.on = True
        blue3.on = True
        blue4.on = True

    def com_yellow(self):
        yellow1 = self.squares[(11,11)]
        yellow2 = self.squares[(12,11)]
        yellow3 = self.squares[(11,12)]
        yellow4 = self.squares[(12,12)]
        yellow1.create_oval(5,5,45,45, fill = 'yellow', tags = 'yellow')
        yellow2.create_oval(5,5,45,45, fill = 'yellow', tags = 'yellow')
        yellow3.create_oval(5,5,45,45, fill = 'yellow', tags = 'yellow')
        yellow4.create_oval(5,5,45,45, fill = 'yellow', tags = 'yellow')
        yellow1.on = True
        yellow2.on = True
        yellow3.on = True
        yellow4.on = True

class Player(color, homeCoord):
    def __init__(self, color, homeCoord):
        self.color = color
        self.homeCoord = homeCoord
        self.home()
        self.on_board()

    def home(coord):
        return self.homeCoord == coord

    def on_board(coord):
        if not home(coord):
            return True
        
        
root = tk.Tk()
app = Ludo(master = root)
app.mainloop()
