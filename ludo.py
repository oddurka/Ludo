import tkinter as tk
from itertools import cycle
import random

class Ludo(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.root = master
        self.die = 0

        self.redOnBoard = []
        self.redHome = []
        self.redGoal = 0
        
        self.greenOnBoard = []
        self.greenHome = []
        self.greenGoal = 0
        
        self.yellowOnBoard = []
        self.yellowHome = []
        self.yellowGoal = 0
        
        self.blueOnBoard = []
        self.blueHome = []
        self.blueGoal = 0
        
        self.teams = cycle(['red', 'green', 'yellow', 'blue'])
        self.color = ''
        self.grid()
        self.board()
        self.gui()
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
        self.color = self.teams.__next__()
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
                    
                can.bind('<Button-1>', self.move)
                
    def move(self, event):
        if self.color == 'red':
            print('RED TURN')
            self.move_red(event)
        elif self.color == 'green':
            print('GREEN TURN')
            self.move_green(event)
        elif self.color == 'yellow':
            print('YELLOW TURN')
            self.move_yellow(event)
        elif self.color == 'blue':
            print('BLUE TURN')
            self.move_blue(event)
        self.gui()

    #RED MOVE
    def move_red(self, event):
        home = [(2,2),(2,3),(3,2),(3,3)]
        legalMoves = [(6,0), (6,1), (6,2), (6,3), (6,4), (6,5), (5,6), (4,6), (3,6), (2,6), (1,6), (0,6),
                       (0,7), (0,8), (1,8), (2,8), (3,8), (4,8), (5,8), (6,9), (6,10), (6,11), (6,12), (6,13), (6,14),
                       (7,14), (8,14), (8,13), (8,12), (8,11), (8,10), (8,9), (9,8), (10,8), (11,8), (12,8), (13,8), (14,8),
                       (14,7), (14,6), (13,6), (12,6), (11,6), (10,6), (9,6), (8,5), (8,4), (8,3), (8,2), (8,1), (8,0), (7,0)]
        if self.die != 6 and len(self.redHome) == 4:
            self.die == 0
            self.color = self.teams.__next__()
        else:
            if self.die == 6:
                for i in self.redHome:
                    i.on =  True
            if event.widget.on:
                if (event.widget.row,event.widget.col) in home:
                    if self.redHome:
                        nextColor = self.redHome[0]
                    if self.color in self.squares[legalMoves[1]].gettags(red):
                        pass
                    else:
                        curRed = self.squares[legalMoves[1]]
                        if self.redHome:
                            self.redHome.remove(nextColor)
                            self.redOnBoard.append(curRed)
                        curRed.create_oval(5,5,45,45, fill = self.color, tags = 'red')
                        curRed.on = True
                        nextColor.delete(self.color)
                    self.die = 0

                if (event.widget.row,event.widget.col) in legalMoves:
                    idx = (legalMoves.index((event.widget.row,event.widget.col)) + self.die) % len(legalMoves)
                    if self.color in self.squares[legalMoves[idx]].gettags(red):
                        pass 
                    elif self.color in self.squares[legalMoves[idx]].gettags(red) and 6 > idx >= 0:
                        pass
                    else:
                        curRed = self.squares[(event.widget.row,event.widget.col)]

                        if 6 > idx >= 0 and 51 < legalMoves.index((event.widget.row,event.widget.col)) + self.die and self.color in self.squares[(event.widget.row,event.widget.col)].gettags(red):
                            self.redGoal += 1
                            nextPlace = self.squares[(7,5 - self.redGoal)]
                        else:
                            nextPlace = self.squares[legalMoves[idx]]
                        curRed.delete(self.color)
                        curRed.on = False
                        nextPlace.create_oval(5,5,45,45, fill = self.color, tags = 'red')
                        nextPlace.on = True
                        self.die = 0
                        
                red1.on = False
                red2.on = False
                red3.on = False
                red4.on = False
                if self.redGoal == 4:
                    self.winner(self.color)
                self.die == 0
                self.color = self.teams.__next__()

    #GREEN MOVE
    def move_green(self, event):
        if self.greenHome:
            nextColor = self.greenHome[0]
        home = [(2,11),(2,12),(3,11),(3,12)]
        legalMoves = [(6,0), (6,1), (6,2), (6,3), (6,4), (6,5), (5,6), (4,6), (3,6), (2,6), (1,6), (0,6),
                       (0,7), (0,8), (1,8), (2,8), (3,8), (4,8), (5,8), (6,9), (6,10), (6,11), (6,12), (6,13), (6,14),
                       (7,14), (8,14), (8,13), (8,12), (8,11), (8,10), (8,9), (9,8), (10,8), (11,8), (12,8), (13,8), (14,8),
                       (14,7), (14,6), (13,6), (12,6), (11,6), (10,6), (9,6), (8,5), (8,4), (8,3), (8,2), (8,1), (8,0), (7,0)]
        if self.die != 6 and len(self.greenHome) == 4:
            self.die == 0
            self.color = self.teams.__next__()
        else:
            if self.die == 6:
                for i in self.greenHome:
                    i.on =  True
            if event.widget.on:
                if (event.widget.row,event.widget.col) in home:
                    if self.color in self.squares[legalMoves[14]].gettags(green):
                        pass
                    elif self.color in self.squares[legalMoves[14]].gettags(red):
                        self.redOnBoard.remove(red)
                        self.redHome.append(red)
                        sendRed = self.squares[red1]
                        sendRed.create_oval(5,5,45,45, fill = self.color, tags = self.color)
                        
                    else:
                        curGreen = self.squares[legalMoves[14]]
                        if self.greenHome:
                            self.greenHome.remove(nextColor)
                            self.greenOnBoard.append(curGreen)
                        curGreen.create_oval(5,5,45,45, fill = self.color, tags = self.color)
                        curGreen.on = True
                        nextColor.delete(self.color)
                    self.die = 0

                if (event.widget.row,event.widget.col) in legalMoves:
                    idx = (legalMoves.index((event.widget.row,event.widget.col)) + self.die) % len(legalMoves)
                    if self.color in self.squares[legalMoves[idx]].gettags(green):
                        pass 
                    elif self.color in self.squares[legalMoves[idx]].gettags(green) and 19 > idx >= 14:
                        pass
                    else:
                        curGreen = self.squares[(event.widget.row,event.widget.col)]
                    
                        
                        if 19 > idx >= 13 and 12 < legalMoves.index((event.widget.row,event.widget.col)) + self.die and self.color in self.squares[(event.widget.row,event.widget.col)].gettags(green):
                            self.greenGoal += 1
                            nextPlace = self.squares[(5 - self.greenGoal,7)]
                        else:
                            nextPlace = self.squares[legalMoves[idx]]
                        curGreen.delete(self.color)
                        curGreen.on = False
                        nextPlace.create_oval(5,5,45,45, fill = self.color, tags = self.color)
                        nextPlace.on = True
                        self.die = 0
                        
                green1.on = False
                green2.on = False
                green3.on = False
                green4.on = False
                if self.greenGoal == 4:
                    self.winner(self.color)
                self.die == 0
                self.color = self.teams.__next__()

    #YELLOW MOVE
    def move_yellow(self, event):
        if self.yellowHome:
            nextColor = self.yellowHome[0]
        home = [(11,11),(11,12),(12,11),(12,12)]
        legalMoves = [(6,0), (6,1), (6,2), (6,3), (6,4), (6,5), (5,6), (4,6), (3,6), (2,6), (1,6), (0,6),
                       (0,7), (0,8), (1,8), (2,8), (3,8), (4,8), (5,8), (6,9), (6,10), (6,11), (6,12), (6,13), (6,14),
                       (7,14), (8,14), (8,13), (8,12), (8,11), (8,10), (8,9), (9,8), (10,8), (11,8), (12,8), (13,8), (14,8),
                       (14,7), (14,6), (13,6), (12,6), (11,6), (10,6), (9,6), (8,5), (8,4), (8,3), (8,2), (8,1), (8,0), (7,0)]
        if self.die != 6 and len(self.yellowHome) == 4:
            self.die == 0
            self.color = self.teams.__next__()
        else:
            if self.die == 6:
                for i in self.yellowHome:
                    i.on =  True
            if event.widget.on:
                if (event.widget.row,event.widget.col) in home:
                    if self.color in self.squares[legalMoves[27]].gettags(yellow):
                        pass                        
                    else:
                        curYellow = self.squares[legalMoves[27]]
                        if self.yellowHome:
                            self.yellowHome.remove(nextColor)
                            self.yellowOnBoard.append(curYellow)
                        curYellow.create_oval(5,5,45,45, fill = self.color, tags = self.color)
                        curYellow.on = True
                        nextColor.delete(self.color)
                    self.die = 0

                if (event.widget.row,event.widget.col) in legalMoves:
                    idx = (legalMoves.index((event.widget.row,event.widget.col)) + self.die) % len(legalMoves)
                    if self.color in self.squares[legalMoves[idx]].gettags(yellow):
                        pass 
                    elif self.color in self.squares[legalMoves[idx]].gettags(yellow) and 33 > idx >= 26:
                        pass
                    else:
                        curYellow = self.squares[(event.widget.row,event.widget.col)]
                    
                        
                        if 33 > idx >= 26 and 19 < legalMoves.index((event.widget.row,event.widget.col)) + self.die and self.color in self.squares[(event.widget.row,event.widget.col)].gettags(yellow):
                            self.yellowGoal += 1
                            nextPlace = self.squares[(7,9 + self.yellowGoal)]
                        else:
                            nextPlace = self.squares[legalMoves[idx]]
                        curYellow.delete(self.color)
                        curYellow.on = False
                        nextPlace.create_oval(5,5,45,45, fill = self.color, tags = self.color)
                        nextPlace.on = True
                        self.die = 0
                        
                yellow1.on = False
                yellow2.on = False
                yellow3.on = False
                yellow4.on = False
                if self.yellowGoal == 4:
                    self.winner(self.color)
                self.die == 0
                self.color = self.teams.__next__()

    #BLUE MOVE
    def move_blue(self, event):
        if self.blueHome:
            nextColor = self.blueHome[0]
        home = [(11,2),(12,2),(11,3),(12,3)]
        legalMoves = [(6,0), (6,1), (6,2), (6,3), (6,4), (6,5), (5,6), (4,6), (3,6), (2,6), (1,6), (0,6),
                       (0,7), (0,8), (1,8), (2,8), (3,8), (4,8), (5,8), (6,9), (6,10), (6,11), (6,12), (6,13), (6,14),
                       (7,14), (8,14), (8,13), (8,12), (8,11), (8,10), (8,9), (9,8), (10,8), (11,8), (12,8), (13,8), (14,8),
                       (14,7), (14,6), (13,6), (12,6), (11,6), (10,6), (9,6), (8,5), (8,4), (8,3), (8,2), (8,1), (8,0), (7,0)]
        if self.die != 6 and len(self.blueHome) == 4:
            self.die == 0
            self.color = self.teams.__next__()
        else:
            if self.die == 6:
                for i in self.blueHome:
                    i.on =  True
            if event.widget.on:
                if (event.widget.row,event.widget.col) in home:
                    if self.color in self.squares[legalMoves[40]].gettags(blue):
                        pass                        
                    else:
                        curBlue = self.squares[legalMoves[40]]
                        if self.blueHome:
                            self.blueHome.remove(nextColor)
                            self.blueOnBoard.append(curBlue)
                        curBlue.create_oval(5,5,45,45, fill = self.color, tags = self.color)
                        curBlue.on = True
                        nextColor.delete(self.color)
                    self.die = 0

                if (event.widget.row,event.widget.col) in legalMoves:
                    idx = (legalMoves.index((event.widget.row,event.widget.col)) + self.die) % len(legalMoves)
                    if self.color in self.squares[legalMoves[idx]].gettags(blue):
                        pass 
                    elif self.color in self.squares[legalMoves[idx]].gettags(blue) and 45 > idx >= 39:
                        pass
                    else:
                        curBlue = self.squares[(event.widget.row,event.widget.col)]
                    
                        
                        if 45 > idx >= 39 and 32 < legalMoves.index((event.widget.row,event.widget.col)) + self.die and self.color in self.squares[(event.widget.row,event.widget.col)].gettags(blue):
                            self.blueGoal += 1
                            nextPlace = self.squares[(9 + self.blueGoal,7)]
                        else:
                            nextPlace = self.squares[legalMoves[idx]]
                        curBlue.delete(self.color)
                        curBlue.on = False
                        nextPlace.create_oval(5,5,45,45, fill = self.color, tags = self.color)
                        nextPlace.on = True
                        self.die = 0
                        
                blue1.on = False
                blue2.on = False
                blue3.on = False
                blue4.on = False
                if self.blueGoal == 4:
                    self.winner(self.color)
                self.die == 0
                self.color = self.teams.__next__()

    def roll_die(self):
        self.die = random.randint(1,6)
        self.gui()
    
    def gui(self):
        frame = tk.Frame(self.root)
        frame.grid(row = 0,column = 1, sticky = 'n')

        playerCan = tk.Canvas(frame, width = 50, height = 50, bg = self.color)
        playerCan.grid(row = 0, column = 0, sticky = 'nw')
        
        rollLabel = tk.Label(frame, text = 'You rolled a ' + str(self.die)).grid(row = 1,column = 0, sticky = 'nw')
        rollDie = tk.Button(frame, text = 'Roll die', command = self.roll_die).grid(row = 2,column = 0, sticky = 'we')

    def winner(self, color):
        winWindow = tk.Toplevel()
        winLabel = tk.Label(winWindow, text = color + ' Wins')
        winLabel.pack()
        

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
        red = red1.create_oval(5,5,45,45, fill = 'red', tags = 'red')
        red2.create_oval(5,5,45,45, fill = 'red', tags = 'red')
        red3.create_oval(5,5,45,45, fill = 'red', tags = 'red')
        red4.create_oval(5,5,45,45, fill = 'red', tags = 'red')
        red1.on = False
        red2.on = False
        red3.on = False
        red4.on = False
        self.redHome.append(red1)
        self.redHome.append(red2)
        self.redHome.append(red3)
        self.redHome.append(red4)

    def com_green(self):
        global green1
        global green2
        global green3
        global green4
        global green
        green1 = self.squares[(2,11)]
        green2 = self.squares[(2,12)]
        green3 = self.squares[(3,11)]
        green4 = self.squares[(3,12)]
        green = green1.create_oval(5,5,45,45, fill = 'green', tags = 'green')
        green2.create_oval(5,5,45,45, fill = 'green', tags = 'green')
        green3.create_oval(5,5,45,45, fill = 'green', tags = 'green')
        green4.create_oval(5,5,45,45, fill = 'green', tags = 'green')
        green1.on = False
        green2.on = False
        green3.on = False
        green4.on = False
        self.greenHome.append(green1)
        self.greenHome.append(green2)
        self.greenHome.append(green3)
        self.greenHome.append(green4)

    def com_blue(self):
        global blue1
        global blue2
        global blue3
        global blue4
        global blue
        blue1 = self.squares[(11,2)]
        blue2 = self.squares[(12,2)]
        blue3 = self.squares[(11,3)]
        blue4 = self.squares[(12,3)]
        blue = blue1.create_oval(5,5,45,45, fill = 'blue', tags = 'blue')
        blue2.create_oval(5,5,45,45, fill = 'blue', tags = 'blue')
        blue3.create_oval(5,5,45,45, fill = 'blue', tags = 'blue')
        blue4.create_oval(5,5,45,45, fill = 'blue', tags = 'blue')
        blue1.on = False
        blue2.on = False
        blue3.on = False
        blue4.on = False
        self.blueHome.append(blue1)
        self.blueHome.append(blue2)
        self.blueHome.append(blue3)
        self.blueHome.append(blue4)

    def com_yellow(self):
        global yellow1
        global yellow2
        global yellow3
        global yellow4
        global yellow
        yellow1 = self.squares[(11,11)]
        yellow2 = self.squares[(12,11)]
        yellow3 = self.squares[(11,12)]
        yellow4 = self.squares[(12,12)]
        yellow = yellow1.create_oval(5,5,45,45, fill = 'yellow', tags = 'yellow')
        yellow2.create_oval(5,5,45,45, fill = 'yellow', tags = 'yellow')
        yellow3.create_oval(5,5,45,45, fill = 'yellow', tags = 'yellow')
        yellow4.create_oval(5,5,45,45, fill = 'yellow', tags = 'yellow')
        yellow1.on = False
        yellow2.on = False
        yellow3.on = False
        yellow4.on = False
        self.yellowHome.append(yellow1)
        self.yellowHome.append(yellow2)
        self.yellowHome.append(yellow3)
        self.yellowHome.append(yellow4)
        
        
root = tk.Tk()
app = Ludo(master = root)
app.mainloop()
