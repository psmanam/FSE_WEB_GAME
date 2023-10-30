from random import randint
from random import choice
import time
from tkinter import *
from PIL import Image
from PIL import ImageTk
import os
import sys
from tkinter import PhotoImage


class ludoGame:
    def __init__(self, root,b6,b5,b4,b3,b2,b1):
        self.gamePage = root
        self.canvas_build = Canvas(self.gamePage, bg="#141414", width=800, height=630)
        self.canvas_build.pack(fill=BOTH,expand=1)

        self.val_block = [b1, b2, b3, b4, b5, b6]
        self.pos_red = [0, 1, 2, 3]
        self.pos_green = [0, 1, 2, 3]
        self.pos_yellow = [0, 1, 2, 3]
        self.pos_blue = [0, 1, 2, 3]

        self.label_red = []
        self.label_green = []
        self.label_yellow = []
        self.label_blue = []

        self.cordinates_red = [-1, -1, -1, -1]
        self.cordinates_green = [-1, -1, -1, -1]
        self.cordinates_yellow = [-1, -1, -1, -1]
        self.cordinates_blue = [-1, -1, -1, -1]

        self.red_player = []
        self.green_player = []
        self.yellow_player = []
        self.blue_player = []

        self.val_block_pred = []
        self.max_players = []

        for index in range(len(self.pos_red)):
            self.pos_red[index] = -1
            self.pos_green[index] = -1
            self.pos_yellow[index] = -1
            self.pos_blue[index] = -1

        self.red_count = 0
        self.green_count = 0
        self.yellow_count = 0
        self.blue_count = 0

        self.seek_req = 0
        self.max_cross = 0

        self.red_val_st = 0
        self.blue_val_st = 0
        self.yellow_val_st = 0
        self.green_val_st = 0

        self.max_cn = 0
        self.tm = -1

        self.safe_zone_1 = None
        self.safe_zone_2 = None
        self.safe_zone_4 = None
        self.safe_zone_3 = None

        self.comp_first = 0
        self.comp_start_val = 0
        self.comp_val = []


        self.red_play()
        self.blue_play()
        self.yellow_play()
        self.green_play()
        self.designing_board()
        self.begin_game_start()


    def designing_board(self):
        self.canvas_build.create_rectangle(100, 15, 100 + (40 * 15), 15 + (40 * 15), width=6, fill="white")

        self.canvas_build.create_rectangle(100, 15, 100+240, 15+240, width=3, fill="red")
        self.canvas_build.create_rectangle(100, (15+240)+(40*3), 100+240, (15+240)+(40*3)+(40*6), width=3, fill="#04d9ff")
        self.canvas_build.create_rectangle(340+(40*3), 15, 340+(40*3)+(40*6), 15+240, width=3, fill="#00FF00")
        self.canvas_build.create_rectangle(340+(40*3), (15+240)+(40*3), 340+(40*3)+(40*6), (15+240)+(40*3)+(40*6), width=3, fill="yellow")

        self.canvas_build.create_rectangle(100, (15+240), 100+240, (15+240)+40, width=3)
        self.canvas_build.create_rectangle(100+40, (15 + 240)+40, 100 + 240, (15 + 240) + 40+40, width=3, fill="#F00000")
        self.canvas_build.create_rectangle(100, (15 + 240)+80, 100 + 240, (15 + 240) + 80+40, width=3)

        self.canvas_build.create_rectangle(100+240, 15, 100 + 240+40, 15 + (40*6), width=3)
        self.canvas_build.create_rectangle(100+240+40, 15+40, 100+240+80, 15 + (40*6), width=3, fill="#00FF00")
        self.canvas_build.create_rectangle(100+240+80, 15, 100 + 240+80+40, 15 + (40*6), width=3)

        self.canvas_build.create_rectangle(340+(40*3), 15+240, 340+(40*3)+(40*6), 15+240+40, width=3)
        self.canvas_build.create_rectangle(340+(40*3), 15+240+40, 340+(40*3)+(40*6)-40, 15+240+80, width=3, fill="yellow")
        self.canvas_build.create_rectangle(340+(40*3), 15+240+80, 340+(40*3)+(40*6), 15+240+120, width=3)

        self.canvas_build.create_rectangle(100, (15 + 240)+(40*3), 100 + 240+40, (15 + 240)+(40*3)+(40*6), width=3)
        self.canvas_build.create_rectangle(100+240+40, (15 + 240)+(40*3), 100 + 240+40+40, (15 + 240)+(40*3)+(40*6)-40, width=3, fill="#04d9ff")
        self.canvas_build.create_rectangle(100 + 240+40+40, (15 + 240)+(40*3), 100 + 240+40+40+40, (15 + 240)+(40*3)+(40*6), width=3)

        x_cor = 100 + 40
        y_cor = 15 + 240
        x_cor_e = 100 + 40
        y_cor_e = 15 + 240 + (40 * 3)
        for _ in range(5):
            self.canvas_build.create_line(x_cor, y_cor, x_cor_e, y_cor_e, width=3)
            x_cor+=40
            x_cor_e+= 40

        x_cor = 100+240+(40*3)+40
        y_cor = 15 + 240
        x_cor_e = 100+240+(40*3)+40
        y_cor_e = 15 + 240 + (40 * 3)
        for _ in range(5):
            self.canvas_build.create_line(x_cor, y_cor, x_cor_e, y_cor_e, width=3)
            x_cor += 40
            x_cor_e += 40

        x_cor = 100+240
        y_cor = 15+40
        x_cor_e = 100+240+(40*3)
        y_cor_e = 15+40
        for _ in range(5):
            self.canvas_build.create_line(x_cor, y_cor, x_cor_e, y_cor_e, width=3)
            y_cor += 40
            y_cor_e += 40

        x_cor = 100 + 240
        y_cor = 15 + (40*6)+(40*3)+40
        x_cor_e = 100 + 240 + (40 * 3)
        y_cor_e = 15 + (40*6)+(40*3)+40
        for _ in range(5):
            self.canvas_build.create_line(x_cor, y_cor, x_cor_e, y_cor_e, width=3)
            y_cor += 40
            y_cor_e += 40

        self.canvas_build.create_rectangle(100+20, 15+40-20, 100 + 40 + 60 + 40 +60+20, 15+40+40+40+100-20, width=3, fill="white")
        self.canvas_build.create_rectangle(340+(40*3)+40 - 20, 15 + 40-20, 340+(40*3)+40 + 60 + 40 + 40+20+20, 15+40+40+40+100-20, width=3, fill="white")
        self.canvas_build.create_rectangle(100+20, 340+80-20+15, 100 + 40 + 60 + 40 +60+20, 340+80+60+40+40+20+15, width=3, fill="white")
        self.canvas_build.create_rectangle(340+(40*3)+40 - 20, 340 + 80 - 20+15, 340+(40*3)+40 + 60 + 40 + 40+20+20, 340 + 80 + 60 + 40 + 40 + 20+15, width=3, fill="white")


        self.canvas_build.create_rectangle(100+40, 15+40, 100+40+40, 15+40+40, width=3, fill="red")
        self.canvas_build.create_rectangle(100+40+60+60, 15 + 40, 100+40+60+40+60, 15 + 40 + 40, width=3, fill="red")
        self.canvas_build.create_rectangle(100 + 40, 15 + 40+100, 100 + 40 + 40, 15 + 40 + 40+100, width=3, fill="red")
        self.canvas_build.create_rectangle(100 + 40 + 60 + 60, 15 + 40+100, 100 + 40 + 60 + 40 +60, 15 + 40 + 40+100, width=3, fill="red")


        self.canvas_build.create_rectangle(340+(40*3)+40, 15 + 40, 340+(40*3)+40 + 40, 15 + 40 + 40, width=3, fill="#00FF00")
        self.canvas_build.create_rectangle(340+(40*3)+40+ 60 + 40+20, 15 + 40, 340+(40*3)+40 + 60 + 40 + 40+20, 15 + 40 + 40, width=3, fill="#00FF00")
        self.canvas_build.create_rectangle(340+(40*3)+40, 15 + 40 + 100, 340+(40*3)+40 + 40, 15 + 40 + 40 + 100, width=3, fill="#00FF00")
        self.canvas_build.create_rectangle(340+(40*3)+40+ 60 + 40+20, 15 + 40 + 100, 340+(40*3)+40 + 60 + 40 + 40+20, 15 + 40 + 40 + 100, width=3, fill="#00FF00")


        self.canvas_build.create_rectangle(100 + 40, 340+80+15, 100 + 40 + 40, 340+80+40+15, width=3, fill="#04d9ff")
        self.canvas_build.create_rectangle(100 + 40 + 60 + 40+20, 340+80+15, 100 + 40 + 60 + 40 + 40+20, 340+80+40+15, width=3, fill="#04d9ff")
        self.canvas_build.create_rectangle(100 + 40, 340+80+60+40+15, 100 + 40 + 40, 340+80+60+40+40+15, width=3, fill="#04d9ff")
        self.canvas_build.create_rectangle(100 + 40 + 60 + 40+20, 340+80+60+40+15, 100 + 40 + 60 + 40 + 40+20, 340+80+60+40+40+15, width=3, fill="#04d9ff")


        self.canvas_build.create_rectangle(340 + (40 * 3) + 40, 340+80+15, 340 + (40 * 3) + 40 + 40, 340+80+40+15, width=3, fill="yellow")
        self.canvas_build.create_rectangle(340 + (40 * 3) + 40 + 60 + 40+20, 340+80+15, 340 + (40 * 3) + 40 + 60 + 40 + 40+20, 340+80+40+15, width=3, fill="yellow")
        self.canvas_build.create_rectangle(340 + (40 * 3) + 40, 340+80+60+40+15, 340 + (40 * 3) + 40 + 40,340+80+60+40+40+15, width=3, fill="yellow")
        self.canvas_build.create_rectangle(340 + (40 * 3) + 40 + 60 + 40+20, 340+80+60+40+15,340 + (40 * 3) + 40 + 60 + 40 + 40+20, 340+80+60+40+40+15, width=3, fill="yellow")

        self.canvas_build.create_rectangle(100+240,340+(40*5)-5,100+240+40,340+(40*6)-5,fill="#04d9ff",width=3)
        self.canvas_build.create_rectangle(100 + 40, 15+(40*6), 100 +40 + 40, 15+(40*6)+40, fill="red", width=3)
        self.canvas_build.create_rectangle(100 + (40*8), 15 + 40, 100 +(40*9), 15 + 40+ 40, fill="#00FF00", width=3)
        self.canvas_build.create_rectangle(100 + (40 * 6)+(40*3)+(40*4), 15 + (40*8), 100 + (40 * 6)+(40*3)+(40*5), 15 + (40*9), fill="yellow", width=3)

        self.canvas_build.create_polygon(100+240, 15+240, 100+240+60, 15+240+60, 100+240, 15+240+(40*3), width=3,fill="red",outline="black")
        self.canvas_build.create_polygon(100 + 240+(40*3), 15 + 240, 100 + 240 + 60, 15 + 240 + 60, 100 + 240+(40*3), 15 + 240 + (40 * 3), width=3, fill="yellow",outline="black")
        self.canvas_build.create_polygon(100 + 240, 15 + 240, 100 + 240 + 60, 15 + 240 + 60, 100 + 240 + (40 * 3), 15 + 240, width=3, fill="#00FF00",outline="black")
        self.canvas_build.create_polygon(100 + 240, 15 + 240+(40*3), 100 + 240 + 60, 15 + 240 + 60, 100 + 240 + (40 * 3), 15 + 240+(40*3), width=3, fill="#04d9ff",outline="black")

        coin1_red = self.canvas_build.create_oval(100+40, 15+40, 100+40+40, 15+40+40, width=3, fill="red", outline="black")
        coin2_red = self.canvas_build.create_oval(100+40+60+60, 15 + 40, 100+40+60+60+40, 15 + 40 + 40, width=3, fill="red", outline="black")
        coin3_red = self.canvas_build.create_oval(100 + 40 + 60 + 60, 15 + 40 + 100, 100 + 40 + 60 + 60 + 40, 15 + 40 + 40 + 100, width=3, fill="red", outline="black")
        coin4_red = self.canvas_build.create_oval(100 + 40, 15 + 40+100, 100 + 40 + 40, 15 + 40 + 40+100, width=3,fill="red", outline="black")
        self.red_player.append(coin1_red)
        self.red_player.append(coin2_red)
        self.red_player.append(coin3_red)
        self.red_player.append(coin4_red)

        l1_red = Label(self.canvas_build, text="1", font=("Arial", 15, "bold"), bg="red", fg="black")
        l1_red.place(x=100 + 40 + 10, y=15 + 40 + 5)
        l2_red = Label(self.canvas_build, text="2", font=("Arial", 15, "bold"), bg="red", fg="black")
        l2_red.place(x=100 + 40 + 60 + 60 + 10, y=15 + 40 + 5)
        l3_red = Label(self.canvas_build, text="3", font=("Arial", 15, "bold"), bg="red", fg="black")
        l3_red.place(x=100 + 40 + 60 + 60 + 10, y=15 + 40 + 100 + 5)
        l4_red = Label(self.canvas_build, text="4", font=("Arial", 15, "bold"), bg="red", fg="black")
        l4_red.place(x=100 + 40 + 10, y=15 + 40 + 100 + 5)
        self.label_red.append(l1_red)
        self.label_red.append(l2_red)
        self.label_red.append(l3_red)
        self.label_red.append(l4_red)

        coin1_green = self.canvas_build.create_oval(340+(40*3)+40, 15 + 40, 340+(40*3)+40 + 40, 15 + 40 + 40, width=3, fill="#00FF00", outline="black")
        coin2_green = self.canvas_build.create_oval(340+(40*3)+40+ 60 + 40+20, 15 + 40, 340+(40*3)+40 + 60 + 40 + 40+20, 15 + 40 + 40, width=3, fill="#00FF00", outline="black")
        coin3_green = self.canvas_build.create_oval(340 + (40 * 3) + 40 + 60 + 40 + 20, 15 + 40 + 100, 340 + (40 * 3) + 40 + 60 + 40 + 40 + 20, 15 + 40 + 40 + 100, width=3, fill="#00FF00", outline="black")
        coin4_green = self.canvas_build.create_oval(340+(40*3)+40, 15 + 40 + 100, 340+(40*3)+40 + 40, 15 + 40 + 40 + 100, width=3, fill="#00FF00", outline="black")
        self.green_player.append(coin1_green)
        self.green_player.append(coin2_green)
        self.green_player.append(coin3_green)
        self.green_player.append(coin4_green)

        l1_green = Label(self.canvas_build, text="1", font=("Arial", 15, "bold"), bg="#00FF00", fg="black")
        l1_green.place(x=340 + (40 * 3) + 40 + 10, y=15 + 40 + 5)
        l2_green = Label(self.canvas_build, text="2", font=("Arial", 15, "bold"), bg="#00FF00", fg="black")
        l2_green.place(x=340 + (40 * 3) + 40 + 40 + 60 + 30, y=15 + 40 + 5)
        l3_green = Label(self.canvas_build, text="3", font=("Arial", 15, "bold"), bg="#00FF00", fg="black")
        l3_green.place(x=340 + (40 * 3) + 40 + 40 + 60 + 30, y=15 + 40 + 100 + 5)
        l4_green = Label(self.canvas_build, text="4", font=("Arial", 15, "bold"), bg="#00FF00", fg="black")
        l4_green.place(x=340 + (40 * 3) + 40 + 10, y=15 + 40 + 100 + 5)
        self.label_green.append(l1_green)
        self.label_green.append(l2_green)
        self.label_green.append(l3_green)
        self.label_green.append(l4_green)

        coin1_blue = self.canvas_build.create_oval(100 + 40, 340+80+15, 100 + 40 + 40, 340+80+40+15, width=3, fill="#04d9ff", outline="black")
        coin2_blue = self.canvas_build.create_oval(100 + 40 + 60 + 40+20, 340+80+15, 100 + 40 + 60 + 40 + 40+20, 340+80+40+15, width=3, fill="#04d9ff", outline="black")
        coin3_blue = self.canvas_build.create_oval(100 + 40 + 60 + 40 + 20, 340 + 80 + 60 + 40 + 15, 100 + 40 + 60 + 40 + 40 + 20, 340 + 80 + 60 + 40 + 40 + 15, width=3, fill="#04d9ff", outline="black")
        coin4_blue = self.canvas_build.create_oval( 100 + 40, 340+80+60+40+15, 100 + 40 + 40, 340+80+60+40+40+15, width=3, fill="#04d9ff", outline="black")
        self.blue_player.append(coin1_blue)
        self.blue_player.append(coin2_blue)
        self.blue_player.append(coin3_blue)
        self.blue_player.append(coin4_blue)

        l1_blue = Label(self.canvas_build, text="1", font=("Arial", 15, "bold"), bg="#04d9ff", fg="black")
        l1_blue.place(x=100 + 40 + 10, y=30 + (40 * 6) + (40 * 3) + 40 + 10)
        l2_blue = Label(self.canvas_build, text="2", font=("Arial", 15, "bold"), bg="#04d9ff", fg="black")
        l2_blue.place(x=100 + 40 + 60 + 60 + 10, y=30 + (40 * 6) + (40 * 3) + 40 + 10)
        l3_blue = Label(self.canvas_build, text="3", font=("Arial", 15, "bold"), bg="#04d9ff", fg="black")
        l3_blue.place(x=100 + 40 + 60 + 60 + 10, y=30 + (40 * 6) + (40 * 3) + 40 + 60 + 40 + 10)
        l4_blue = Label(self.canvas_build, text="4", font=("Arial", 15, "bold"), bg="#04d9ff", fg="black")
        l4_blue.place(x=100 + 40 + 10, y=30 + (40 * 6) + (40 * 3) + 40 + 60 + 40 + 10)
        self.label_blue.append(l1_blue)
        self.label_blue.append(l2_blue)
        self.label_blue.append(l3_blue)
        self.label_blue.append(l4_blue)

        coin1_yellow = self.canvas_build.create_oval(340 + (40 * 3) + 40, 340+80+15, 340 + (40 * 3) + 40 + 40, 340+80+40+15, width=3, fill="yellow", outline="black")
        coin2_yellow = self.canvas_build.create_oval(340 + (40 * 3) + 40 + 60 + 40 + 20, 340+80+15, 340 + (40 * 3) + 40 + 60 + 40 + 40+20, 340+80+40+15, width=3, fill="yellow", outline="black")
        coin3_yellow = self.canvas_build.create_oval(340 + (40 * 3) + 40 + 60 + 40 + 20, 340 + 80 + 60 + 40 + 15, 340 + (40 * 3) + 40 + 60 + 40 + 40 + 20, 340 + 80 + 60 + 40 + 40 + 15, width=3, fill="yellow", outline="black")
        coin4_yellow = self.canvas_build.create_oval(340 + (40 * 3) + 40, 340+80+60+40+15, 340 + (40 * 3) + 40 + 40,340+80+60+40+40+15, width=3, fill="yellow", outline="black")
        self.yellow_player.append(coin1_yellow)
        self.yellow_player.append(coin2_yellow)
        self.yellow_player.append(coin3_yellow)
        self.yellow_player.append(coin4_yellow)

        l1_yellow = Label(self.canvas_build, text="1", font=("Arial", 15, "bold"), bg="yellow", fg="black")
        l1_yellow.place(x=340 + (40 * 3) + 40 + 10, y=30 + (40 * 6) + (40 * 3) + 40 + 10)
        l2_yellow = Label(self.canvas_build, text="2", font=("Arial", 15, "bold"), bg="yellow", fg="black")
        l2_yellow.place(x=340 + (40 * 3) + 40 + 40 + 60 + 30, y=30 + (40 * 6) + (40 * 3) + 40 + 10)
        l3_yellow = Label(self.canvas_build, text="3", font=("Arial", 15, "bold"), bg="yellow", fg="black")
        l3_yellow.place(x=340 + (40 * 3) + 40 + 40 + 60 + 30, y=30 + (40 * 6) + (40 * 3) + 40 + 100 + 10)
        l4_yellow = Label(self.canvas_build, text="4", font=("Arial", 15, "bold"), bg="yellow", fg="black")
        l4_yellow.place(x=340 + (40 * 3) + 40 + 10, y=30 + (40 * 6) + (40 * 3) + 40 + 100 + 10)
        self.label_yellow.append(l1_yellow)
        self.label_yellow.append(l2_yellow)
        self.label_yellow.append(l3_yellow)
        self.label_yellow.append(l4_yellow)

        """
                                              A
                                           L  *  B
                                   K *  *  *     *  *  * C
                                        *           *
                                        J *        * D
                                       *            *
                                  I*  *  *      *  *  * E
                                         H   *   F
                                             G
        """
        x_comm = 340+(40*6)+20
        y_comm = 15+240+2
        cordinates = [x_comm,y_comm,  x_comm+5,y_comm+15,  x_comm+15,y_comm+15,  x_comm+8,y_comm+20,    x_comm+15,y_comm+25,    x_comm+5,y_comm+25,    x_comm,y_comm+25+10,   x_comm-5,y_comm+25,   x_comm-16,y_comm+25,   x_comm-8,y_comm+15+5,   x_comm-15,y_comm+15,   x_comm-5,y_comm+15]
        self.canvas_build.create_polygon(cordinates,width=3,fill="blue")
        x_comm = 100+240+2+18
        y_comm = 15 + (40*2) + 2
        cordinates = [x_comm, y_comm,   x_comm + 5,   y_comm + 15,      x_comm + 15, y_comm + 15,      x_comm + 8, y_comm + 20,     x_comm + 15, y_comm + 25,       x_comm + 5, y_comm + 25,      x_comm, y_comm + 25 + 10,    x_comm - 5, y_comm + 25,     x_comm - 16, y_comm + 25,     x_comm - 8,y_comm + 15 + 5,     x_comm - 15,y_comm + 15,     x_comm - 5,y_comm + 15]
        self.canvas_build.create_polygon(cordinates, width=3, fill="blue")

        
        x_comm = 100 + (40*2) + 2 +18
        y_comm = 15 + 240+(40*2) + 2
        cordinates = [x_comm, y_comm,   x_comm + 5, y_comm + 15,    x_comm + 15, y_comm + 15,    x_comm + 8,y_comm + 20,    x_comm + 15, y_comm + 25,    x_comm + 5, y_comm + 25,    x_comm, y_comm + 25 + 10,    x_comm - 5, y_comm + 25,      x_comm - 16, y_comm + 25,     x_comm - 8, y_comm + 15 + 5,     x_comm - 15, y_comm + 15,     x_comm - 5, y_comm + 15]
        self.canvas_build.create_polygon(cordinates, width=3, fill="blue")
        x_comm = 100 + 240 + (40*2) + 2 + 18
        y_comm = 15 + (40 * 6) + (40*3)+(40*3)+2
        cordinates = [x_comm, y_comm,   x_comm + 5, y_comm + 15,    x_comm + 15, y_comm + 15,    x_comm + 8, y_comm + 20,    x_comm + 15, y_comm + 25,      x_comm + 5, y_comm + 25,       x_comm, y_comm + 25 + 10,        x_comm - 5, y_comm + 25,       x_comm - 16, y_comm + 25,       x_comm - 8, y_comm + 15 + 5,      x_comm - 15, y_comm + 15,      x_comm - 5, y_comm + 15]
        self.canvas_build.create_polygon(cordinates, width=3, fill="blue")


    
    def begin_game_start(self):
        for i in range(4):
            self.val_block_pred[i][1]['state'] = DISABLED

        
        top = Toplevel()
        top.geometry("530x300")
        top.maxsize(530,300)
        top.minsize(530,300)
        top.config(bg="#141414")
        icon_image = PhotoImage(file=resource_path("Images/game_board.png"))
        top.iconphoto(False, icon_image)

        head = Label(top,text="-:Total number of players:- ",font=("Arial",25,"bold","italic"),bg="#141414",fg="chocolate")
        head.place(x=50,y=30)
        take_entry = Entry(top,font=("Arial",18,"bold","italic"),relief=SUNKEN,bd=5,width=12, state=DISABLED)
        take_entry.place(x=130,y=85)
        take_entry.focus()

        def filtering():
            def input_filtering(player_num_coin):
                try:
                    return True if (4>=int(player_num_coin)>=2) or type(player_num_coin) == int else False
                except:
                    return False

            response_take = input_filtering(take_entry.get())
            if response_take:
                for player_index in range(int(take_entry.get())):
                    self.max_players.append(player_index)
                print(self.max_players)
                self.choice_sel()
                top.destroy()
            else:
                messagebox.showerror("Invalid Number", "Input should be 2-4")
                top.destroy()
                self.begin_game_start()

        button_sub = Button(top,text="Submit",bg="#262626",fg="#00FF00",font=("Arial",13,"bold"),relief=RAISED,bd=3,command=filtering,state=DISABLED)
        button_sub.place(x=330,y=87)

        def operate(ind):
            if ind:
                self.comp_first = 1
                for player_index in range(2):
                    self.max_players.append(player_index)
                print(self.max_players)
                def delay_with_instrctions(t1):
                    if place_ins['text'] != "":
                        place_ins.place_forget()
                    if command_play['text'] != "":
                        command_play.place_forget()
                
                    place_ins['text'] = f"  Your game will start within {t1} sec"
                    place_ins.place(x=20, y=220)

                    if t1 > 5:
                        command_play['text'] = f"             Machine Play With Red and You Play With Sky Blue"
                    elif t1>= 2 and t1<5:
                        command_play['text'] = f"                       You Will Get the First Chance to play"
                    else: 
                        command_play['text'] = f"                                        Enjoy this Game"
                    command_play.place(x=10, y=260)

                t1 = 10
                place_ins = Label(top, text="", font=("Arial", 20, "bold"), fg="#FF0000", bg="#141414")
                command_play = Label(top, text="", font=("Arial", 12, "bold"), fg="#af7439", bg="#141414")

                try:
                    while t1:
                        delay_with_instrctions(t1)
                        t1-=1
                        self.gamePage.update()
                        time.sleep(1)
                    top.destroy()
                except:
                    print("Stop! error")
                self.val_block_pred[1][1]['state'] = NORMAL
            else:
                button_sub['state'] = NORMAL
                take_entry['state'] = NORMAL
        
        button_mv = Button(top,text="Play With Computer",bg="#262626",fg="#00FF00",font=("Arial",15,"bold"),relief=RAISED,bd=3,command=lambda: operate(1), activebackground="#262626")
        button_mv.place(x=30,y=160)

        mvh_btn = Button(top,text="Play With Friends",bg="#262626",fg="#00FF00",font=("Arial",15,"bold"),relief=RAISED,bd=3,command=lambda: operate(0), activebackground="#262626")
        mvh_btn.place(x=260,y=160)

        top.mainloop()

    
    def pred_val_prediction(self,c_mapper):
        try:
            if c_mapper == "red":
                val_block_pred = self.val_block_pred[0]
                if self.comp_first and self.comp_start_val < 3:
                    self.comp_start_val += 1
                if self.comp_first and self.comp_start_val == 3 and self.max_cn < 2:
                    real_num_bl = self.red_count = 6
                    self.comp_start_val += 1
                else:    
                    real_num_bl = self.red_count = randint(1, 6)

            elif c_mapper == "sky_blue":
                val_block_pred = self.val_block_pred[1]
                real_num_bl = self.blue_count = randint(1, 6)
                if self.comp_first and real_num_bl == 6:
                    for coin_loc in self.pos_red:
                        if coin_loc>=40 and coin_loc<=46:
                            real_num_bl = self.blue_count = randint(1, 5)
                            break
                            
            elif c_mapper == "yellow":
                val_block_pred = self.val_block_pred[2]
                real_num_bl = self.yellow_count = randint(1, 6)

            else:
                val_block_pred = self.val_block_pred[3]
                real_num_bl = self.green_count = randint(1, 6)

            val_block_pred[1]['state'] = DISABLED

            
            cn_tm = 12
            while cn_tm>0:
                move_cn_tm = randint(1, 6)
                val_block_pred[0]['image'] = self.val_block[move_cn_tm - 1]
                self.gamePage.update()
                time.sleep(0.1)
                cn_tm-=1

            print("Spin output: ", real_num_bl)

            
            val_block_pred[0]['image'] = self.val_block[real_num_bl-1]
            if self.comp_first == 1 and c_mapper == "red":
                self.gamePage.update()
                time.sleep(0.4)
            self.button_choice_after_spin(c_mapper,real_num_bl,val_block_pred)
        except:
            print("Stop! error")
        
    def button_choice_after_spin(self,c_mapper,real_num_bl,val_block_pred):
        comp_op = None
        if c_mapper == "red":
            coin_pos_temp = self.pos_red
        elif c_mapper == "green":
            coin_pos_temp = self.pos_green
        elif c_mapper == "yellow":
            coin_pos_temp = self.pos_yellow
        else:
            coin_pos_temp = self.pos_blue

        all_in = 1
        for i in range(4):
            if coin_pos_temp[i] == -1:
                all_in = 1
            else:
                all_in = 0
                break

        if  real_num_bl == 6:
            self.max_cn += 1
        else:
            self.max_cn = 0

        if ((all_in == 1 and real_num_bl == 6) or (all_in==0)) and self.max_cn<3:
            permission = 1
            if c_mapper == "red":
                temp = self.cordinates_red
            elif c_mapper == "green":
                temp = self.cordinates_green
            elif c_mapper == "yellow":
                temp = self.cordinates_yellow
            else:
                temp = self.cordinates_blue

            if  real_num_bl<6:
                if self.max_cross == 1:
                    self.tm-=1
                    self.max_cross=0
                for i in range(4):
                    if  temp[i] == -1:
                        permission=0
                    elif temp[i]>100:
                        if  temp[i]+real_num_bl<=106:
                            permission=1
                            break
                        else:
                            permission=0
                    else:
                        permission=1
                        break
            else:
                for i in range(4):
                    if  temp[i]>100:
                        if  temp[i] + real_num_bl <= 106:
                            permission = 1
                            break
                        else:
                            permission = 0
                    else:
                        permission = 1
                        break
            if permission == 0:
                self.choice_sel(None)
            else:
                self.buttons_num_control(val_block_pred[2])

                if self.comp_first == 1 and val_block_pred == self.val_block_pred[0]:
                    comp_op = "give"
                val_block_pred[1]['state'] = DISABLED

        else:
            val_block_pred[1]['state'] = NORMAL
            if self.max_cross == 1:
                self.tm -= 1
                self.max_cross = 0
            self.choice_sel()

        if  real_num_bl == 6 and self.max_cn<3 and val_block_pred[2][0]['state'] == NORMAL:
            self.tm-=1
        else:
            self.max_cn=0

        if self.comp_first == 1 and comp_op:
            self.comp_choice(comp_op)
            
    
    def choice_sel(self, comp_op=None):
        if  self.tm == -1:
            pass
        else:
            self.val_block_pred[self.max_players[self.tm]][1]['state'] = DISABLED
        if  self.tm == len(self.max_players)-1:
            self.tm = -1

        self.tm+=1
        self.val_block_pred[self.max_players[self.tm]][1]['state'] = NORMAL
        
        if self.comp_first==1 and self.tm == 0:
            comp_op = "Spin"
        if comp_op:
            self.comp_choice(comp_op)


    def red_play(self):
        block_predict_red = Label(self.canvas_build,image=self.val_block[0])
        block_predict_red.place(x=34,y=15)
        predict_red = Button(self.canvas_build, bg="black", fg="#00FF00", relief=RAISED, bd=5, text="Spin", font=("Arial", 8, "bold"), command=lambda: self.pred_val_prediction("red"))
        predict_red.place(x=25, y=15 + 50)
        
        btn_1 = Button(self.canvas_build,bg="#262626",fg="#00eb00",text="1",font=("Arial",13,"bold","italic"),relief=RAISED,bd=3,command=lambda: self.game__control("red",'1'), state=DISABLED, disabledforeground="red")
        btn_1.place(x=20,y=15+100)
        btn_2 = Button(self.canvas_build,bg="#262626",fg="#00eb00",text="2",font=("Arial",13,"bold","italic"),relief=RAISED,bd=3,command=lambda: self.game__control("red",'2'), state=DISABLED, disabledforeground="red")
        btn_2.place(x=60,y=15+100)
        btn_3 = Button(self.canvas_build,bg="#262626",fg="#00eb00",text="3",font=("Arial",13,"bold","italic"),relief=RAISED,bd=3,command=lambda: self.game__control("red",'3'), state=DISABLED, disabledforeground="red")
        btn_3.place(x=20,y=15+100+40)
        btn_4 = Button(self.canvas_build,bg="#262626",fg="#00eb00",text="4",font=("Arial",13,"bold","italic"),relief=RAISED,bd=3,command=lambda: self.game__control("red",'4'), state=DISABLED, disabledforeground="red")
        btn_4.place(x=60,y=15+100+40)

        Label(self.canvas_build,text="Player 1",bg="#141414",fg="gold",font=("Arial",15,"bold")).place(x=15,y=15+140+50)
        self.store_instructional_btn(block_predict_red,predict_red,[btn_1,btn_2,btn_3,btn_4])

    def blue_play(self):
        block_predict_sky_blue = Label(self.canvas_build, image=self.val_block[0])
        block_predict_sky_blue.place(x=34, y=15+(40*6+40*3)+10)
        predict_sky_blue = Button(self.canvas_build, bg="black", fg="#00FF00", relief=RAISED, bd=5, text="Spin",font=("Arial", 8, "bold"), command=lambda: self.pred_val_prediction("sky_blue"))
        predict_sky_blue.place(x=25, y=15+(40*6+40*3)+40 + 20)

        btn_1 = Button(self.canvas_build,bg="#262626",fg="#00eb00",text="1",font=("Arial",13,"bold","italic"),relief=RAISED,bd=3,command=lambda: self.game__control("sky_blue",'1'), state=DISABLED, disabledforeground="red")
        btn_1.place(x=20,y=15+(40*6+40*3)+40 + 70)
        btn_2 = Button(self.canvas_build,bg="#262626",fg="#00eb00",text="2",font=("Arial",13,"bold","italic"),relief=RAISED,bd=3,command=lambda: self.game__control("sky_blue",'2'), state=DISABLED, disabledforeground="red")
        btn_2.place(x=60,y=15+(40*6+40*3)+40 + 70)
        btn_3 = Button(self.canvas_build,bg="#262626",fg="#00eb00",text="3",font=("Arial",13,"bold","italic"),relief=RAISED,bd=3,command=lambda: self.game__control("sky_blue",'3'), state=DISABLED, disabledforeground="red")
        btn_3.place(x=20,y=15+(40*6+40*3)+40 + 70+ 40)
        btn_4 = Button(self.canvas_build,bg="#262626",fg="#00eb00",text="4",font=("Arial",13,"bold","italic"),relief=RAISED,bd=3,command=lambda: self.game__control("sky_blue",'4'), state=DISABLED, disabledforeground="red")
        btn_4.place(x=60,y=15+(40*6+40*3)+40 + 70+ 40)

        Label(self.canvas_build, text="Player 2", bg="#141414", fg="gold", font=("Arial", 15, "bold")).place(x=12,y=15+(40*6+40*3)+40 + 110+50)
        self.store_instructional_btn(block_predict_sky_blue, predict_sky_blue, [btn_1,btn_2,btn_3,btn_4])

    def yellow_play(self):
        block_predict_yellow = Label(self.canvas_build, image=self.val_block[0])
        block_predict_yellow.place(x=100 + (40 * 6 + 40 * 3 + 40 * 6 + 10)+20, y=15 + (40 * 6 + 40 * 3) + 10)
        predict_yellow = Button(self.canvas_build, bg="black", fg="#00FF00", relief=RAISED, bd=5, text="Spin",font=("Arial", 8, "bold"), command=lambda: self.pred_val_prediction("yellow"))
        predict_yellow.place(x=100 + (40 * 6 + 40 * 3 + 40 * 6 + 2)+20, y=15 + (40 * 6 + 40 * 3) + 40 + 20)
        
        btn_1 = Button(self.canvas_build,bg="#262626",fg="#00eb00",text="1",font=("Arial",13,"bold","italic"),relief=RAISED,bd=3,command=lambda: self.game__control("yellow",'1'), state=DISABLED, disabledforeground="red")
        btn_1.place(x=100 + (40 * 6 + 40 * 3 + 40 * 6 + 2)+15, y=15 + (40 * 6 + 40 * 3) + 40 + 70)
        btn_2 = Button(self.canvas_build,bg="#262626",fg="#00eb00",text="2",font=("Arial",13,"bold","italic"),relief=RAISED,bd=3,command=lambda: self.game__control("yellow",'2'), state=DISABLED, disabledforeground="red")
        btn_2.place(x=100 + (40 * 6 + 40 * 3 + 40 * 6 + 2)+15 + 40, y=15 + (40 * 6 + 40 * 3) + 40 + 70)
        btn_3 = Button(self.canvas_build,bg="#262626",fg="#00eb00",text="3",font=("Arial",13,"bold","italic"),relief=RAISED,bd=3,command=lambda: self.game__control("yellow",'3'), state=DISABLED, disabledforeground="red")
        btn_3.place(x=100 + (40 * 6 + 40 * 3 + 40 * 6 + 2)+15, y=15 + (40 * 6 + 40 * 3) + 40 + 70+ 40)
        btn_4 = Button(self.canvas_build,bg="#262626",fg="#00eb00",text="4",font=("Arial",13,"bold","italic"),relief=RAISED,bd=3,command=lambda: self.game__control("yellow",'4'), state=DISABLED, disabledforeground="red")
        btn_4.place(x=100 + (40 * 6 + 40 * 3 + 40 * 6 + 2)+15 + 40, y=15 + (40 * 6 + 40 * 3) + 40 + 70+ 40)
        
        Label(self.canvas_build, text="Player 3", bg="#141414", fg="gold", font=("Arial", 15, "bold")).place(x=100 + (40 * 6 + 40 * 3 + 40 * 6 +7),y=15+(40*6+40*3)+40 + 110+50)
        self.store_instructional_btn(block_predict_yellow, predict_yellow, [btn_1,btn_2,btn_3,btn_4])

    def green_play(self):
        block_predict_green = Label(self.canvas_build, image=self.val_block[0])
        block_predict_green.place(x=100+(40*6+40*3+40*6+10)+20, y=15)
        predict_green = Button(self.canvas_build, bg="black", fg="#00FF00", relief=RAISED, bd=5, text="Spin", font=("Arial", 8, "bold"), command=lambda: self.pred_val_prediction("green"))
        predict_green.place(x=100+(40*6+40*3+40*6+2)+20, y=15 + 50)
        
        btn_1 = Button(self.canvas_build,bg="#262626",fg="#00eb00",text="1",font=("Arial",13,"bold","italic"),relief=RAISED,bd=3,command=lambda: self.game__control("green",'1'), state=DISABLED, disabledforeground="red")
        btn_1.place(x=100 + (40 * 6 + 40 * 3 + 40 * 6 + 2)+15,y=15+100)
        btn_2 = Button(self.canvas_build,bg="#262626",fg="#00eb00",text="2",font=("Arial",13,"bold","italic"),relief=RAISED,bd=3,command=lambda: self.game__control("green",'2'), state=DISABLED, disabledforeground="red")
        btn_2.place(x=100 + (40 * 6 + 40 * 3 + 40 * 6 + 2)+15 + 40,y=15+100)
        btn_3 = Button(self.canvas_build,bg="#262626",fg="#00eb00",text="3",font=("Arial",13,"bold","italic"),relief=RAISED,bd=3,command=lambda: self.game__control("green",'3'), state=DISABLED, disabledforeground="red")
        btn_3.place(x=100 + (40 * 6 + 40 * 3 + 40 * 6 + 2)+15,y=15+100+40)
        btn_4 = Button(self.canvas_build,bg="#262626",fg="#00eb00",text="4",font=("Arial",13,"bold","italic"),relief=RAISED,bd=3,command=lambda: self.game__control("green",'4'), state=DISABLED, disabledforeground="red")
        btn_4.place(x=100 + (40 * 6 + 40 * 3 + 40 * 6 + 2)+15 + 40,y=15+100+40)
        
        Label(self.canvas_build, text="Player 4", bg="#141414", fg="gold", font=("Arial", 15, "bold")).place(x=100+(40*6+40*3+40*6+7), y=15+140+50)
        self.store_instructional_btn(block_predict_green, predict_green, [btn_1,btn_2,btn_3,btn_4])

    def store_instructional_btn(self, block_indicator, predictor, entry_controller):
        temp = []
        temp.append(block_indicator)
        temp.append(predictor)
        temp.append(entry_controller)
        self.val_block_pred.append(temp)

    def red_st_pos(self, player_num_coin):
        self.canvas_build.delete(self.red_player[int(player_num_coin)-1])
        self.red_player[int(player_num_coin)-1] = self.canvas_build.create_oval(100 + 40, 15+(40*6), 100 +40 + 40, 15+(40*6)+40, fill="red", width=3, outline="black")

        self.label_red[int(player_num_coin)-1].place_forget()
        red_start_label_x = 100 + 40 + 10
        red_start_label_y = 15 + (40 * 6) + 5
        self.label_red[int(player_num_coin)-1].place(x=red_start_label_x, y=red_start_label_y)

        self.pos_red[int(player_num_coin)-1] = 1
        self.gamePage.update()
        time.sleep(0.2)

    def green_st_pos(self,player_num_coin):
        self.canvas_build.delete(self.green_player[int(player_num_coin)-1])
        self.green_player[int(player_num_coin)-1] = self.canvas_build.create_oval(100 + (40*8), 15 + 40, 100 +(40*9), 15 + 40+ 40, fill="#00FF00", width=3)

        self.label_green[int(player_num_coin)-1].place_forget()
        green_start_label_x = 100 + (40*8) + 10
        green_start_label_y = 15 + 40 + 5
        self.label_green[int(player_num_coin)-1].place(x=green_start_label_x, y=green_start_label_y)

        self.pos_green[int(player_num_coin)-1] = 14
        self.gamePage.update()
        time.sleep(0.2)

    def yellow_st_pos(self,player_num_coin):
        self.canvas_build.delete(self.yellow_player[int(player_num_coin)-1])
        self.yellow_player[int(player_num_coin)-1] = self.canvas_build.create_oval(100 + (40 * 6)+(40*3)+(40*4), 15 + (40*8), 100 + (40 * 6)+(40*3)+(40*5), 15 + (40*9), fill="yellow", width=3)

        self.label_yellow[int(player_num_coin)-1].place_forget()
        yellow_start_label_x = 100 + (40 * 6)+(40*3)+(40*4) + 10
        yellow_start_label_y = 15 + (40*8) + 5
        self.label_yellow[int(player_num_coin) - 1].place(x=yellow_start_label_x, y=yellow_start_label_y)

        self.pos_yellow[int(player_num_coin) - 1] = 27
        self.gamePage.update()
        time.sleep(0.2)

    def blue_st_pos(self,player_num_coin):
        self.canvas_build.delete(self.blue_player[int(player_num_coin)-1])
        self.blue_player[int(player_num_coin)-1] = self.canvas_build.create_oval(100+240,340+(40*5)-5,100+240+40,340+(40*6)-5,fill="#04d9ff",width=3)

        self.label_blue[int(player_num_coin)-1].place_forget()
        sky_blue_start_label_x = 100+240 + 10
        sky_blue_start_label_y = 340+(40*5)-5 + 5
        self.label_blue[int(player_num_coin) - 1].place(x=sky_blue_start_label_x, y=sky_blue_start_label_y)

        self.pos_blue[int(player_num_coin) - 1] = 40
        self.gamePage.update()
        time.sleep(0.2)

    def buttons_num_control(self, take_nums_btns_list, state_control = 1):
        if state_control:
            for num_btn in take_nums_btns_list:
                num_btn['state'] = NORMAL
        else:
            for num_btn in take_nums_btns_list:
                num_btn['state'] = DISABLED

    def game__control(self, color_coin, player_num_coin):
        comp_op = None

        if  color_coin == "red":
            self.buttons_num_control(self.val_block_pred[0][2], 0)

            if self.red_count == 106:
                messagebox.showwarning("Home Arrived","!")

            elif self.pos_red[int(player_num_coin)-1] == -1 and self.red_count == 6:
                self.red_st_pos(player_num_coin)
                self.cordinates_red[int(player_num_coin) - 1] = 1

            elif self.pos_red[int(player_num_coin)-1] > -1:
                take_cordinates = self.canvas_build.coords(self.red_player[int(player_num_coin)-1])
                red_start_label_x = take_cordinates[0] + 10
                red_start_label_y = take_cordinates[1] + 5
                self.label_red[int(player_num_coin) - 1].place(x=red_start_label_x, y=red_start_label_y)

                if self.pos_red[int(player_num_coin)-1]+self.red_count<=106:
                    self.pos_red[int(player_num_coin)-1] = self.coin_movement(self.pos_red[int(player_num_coin) - 1],self.red_player[int(player_num_coin)-1],self.label_red[int(player_num_coin)-1],red_start_label_x,red_start_label_y,"red",self.red_count) 
                    if self.comp_first and self.pos_red[int(player_num_coin)-1] == 106 and color_coin == "red":
                        self.comp_val.remove(int(player_num_coin))
                        print("After removing: ", self.comp_val)

                else:
                    if not self.comp_first: 
                            messagebox.showerror("Not Available","Position")
                    self.buttons_num_control(self.val_block_pred[0][2])

                    if self.comp_first:
                        comp_op = "give"
                        self.comp_choice(comp_op)
                    return

                if  self.pos_red[int(player_num_coin)-1]==22 or self.pos_red[int(player_num_coin)-1]==9 or self.pos_red[int(player_num_coin)-1]==48 or self.pos_red[int(player_num_coin)-1]==35 or self.pos_red[int(player_num_coin)-1]==14 or self.pos_red[int(player_num_coin)-1]==27 or self.pos_red[int(player_num_coin)-1]==40 or self.pos_red[int(player_num_coin)-1]==1:
                    pass
                else:
                    if self.pos_red[int(player_num_coin) - 1] < 100:
                        self.cordinates_overlap(self.pos_red[int(player_num_coin)-1],color_coin, self.red_count)

                self.cordinates_red[int(player_num_coin)-1] = self.pos_red[int(player_num_coin)-1]

            else:
                messagebox.showerror("Make correct","coin selection")
                self.buttons_num_control(self.val_block_pred[0][2])

                if self.comp_first == 1:
                    comp_op = "give"
                    self.comp_choice(comp_op)
                return

            self.val_block_pred[0][1]['state'] = NORMAL


        elif color_coin == "green":
            self.buttons_num_control(self.val_block_pred[3][2], 0)

            if self.green_count == 106:
                messagebox.showwarning("Home Arrived","!")

            elif self.pos_green[int(player_num_coin) - 1] == -1 and self.green_count == 6:
                self.green_st_pos(player_num_coin)
                self.cordinates_green[int(player_num_coin) - 1] = 14

            elif self.pos_green[int(player_num_coin) - 1] > -1:
                take_cordinates = self.canvas_build.coords(self.green_player[int(player_num_coin) - 1])
                green_start_label_x = take_cordinates[0] + 10
                green_start_label_y = take_cordinates[1] + 5
                self.label_green[int(player_num_coin) - 1].place(x=green_start_label_x, y=green_start_label_y)


                if  self.pos_green[int(player_num_coin) - 1] + self.green_count <= 106:
                    self.pos_green[int(player_num_coin) - 1] = self.coin_movement(self.pos_green[int(player_num_coin) - 1], self.green_player[int(player_num_coin) - 1], self.label_green[int(player_num_coin) - 1], green_start_label_x, green_start_label_y, "green", self.green_count)
                else:
                   messagebox.showerror("Not Available","Path")
                   self.buttons_num_control(self.val_block_pred[3][2])
                   return


                if  self.pos_green[int(player_num_coin)-1]==22 or self.pos_green[int(player_num_coin)-1]==9 or self.pos_green[int(player_num_coin)-1]==48 or self.pos_green[int(player_num_coin)-1]==35 or self.pos_green[int(player_num_coin)-1]==1 or self.pos_green[int(player_num_coin)-1]==27 or self.pos_green[int(player_num_coin)-1]==40 or self.pos_green[int(player_num_coin)-1]==14:
                    pass
                else:
                    if self.pos_green[int(player_num_coin) - 1] < 100:
                        self.cordinates_overlap(self.pos_green[int(player_num_coin) - 1],color_coin, self.green_count)

                self.cordinates_green[int(player_num_coin) - 1] = self.pos_green[int(player_num_coin) - 1]

            else:
                messagebox.showerror("Not Available", "Path")
                self.buttons_num_control(self.val_block_pred[3][2])
                return

            self.val_block_pred[3][1]['state'] = NORMAL

        elif color_coin == "yellow":
            
            self.buttons_num_control(self.val_block_pred[2][2], 0)

            if self.yellow_count == 106:
                messagebox.showwarning("Home Arrived","!")

            elif self.pos_yellow[int(player_num_coin) - 1] == -1 and self.yellow_count == 6:
                self.yellow_st_pos(player_num_coin)
                self.cordinates_yellow[int(player_num_coin) - 1] = 27

            elif self.pos_yellow[int(player_num_coin) - 1] > -1:
                take_cordinates = self.canvas_build.coords(self.yellow_player[int(player_num_coin) - 1])
                yellow_start_label_x = take_cordinates[0] + 10
                yellow_start_label_y = take_cordinates[1] + 5
                self.label_yellow[int(player_num_coin) - 1].place(x=yellow_start_label_x, y=yellow_start_label_y)

                if  self.pos_yellow[int(player_num_coin) - 1] + self.yellow_count <= 106:
                    self.pos_yellow[int(player_num_coin) - 1] = self.coin_movement(self.pos_yellow[int(player_num_coin) - 1], self.yellow_player[int(player_num_coin) - 1], self.label_yellow[int(player_num_coin) - 1], yellow_start_label_x, yellow_start_label_y, "yellow", self.yellow_count)
                else:
                   messagebox.showerror("Not Available","Path")
                   
                   self.buttons_num_control(self.val_block_pred[2][2])
                   return

                if  self.pos_yellow[int(player_num_coin)-1]==22 or self.pos_yellow[int(player_num_coin)-1]==9 or self.pos_yellow[int(player_num_coin)-1]==48 or self.pos_yellow[int(player_num_coin)-1]==35 or self.pos_yellow[int(player_num_coin)-1]==1 or self.pos_yellow[int(player_num_coin)-1]==14 or self.pos_yellow[int(player_num_coin)-1]==40 or self.pos_yellow[int(player_num_coin)-1]==27:
                    pass
                else:
                    if self.pos_yellow[int(player_num_coin) - 1] < 100:
                        self.cordinates_overlap(self.pos_yellow[int(player_num_coin) - 1],color_coin, self.yellow_count)

                self.cordinates_yellow[int(player_num_coin) - 1] = self.pos_yellow[int(player_num_coin) - 1]

            else:
                messagebox.showerror("Not Available", "Path")
                self.buttons_num_control(self.val_block_pred[2][2])
                return

            self.val_block_pred[2][1]['state'] = NORMAL

 
        elif color_coin == "sky_blue":
            self.buttons_num_control(self.val_block_pred[1][2], 0)   

            if self.red_count == 106:
                messagebox.showwarning("Home Arrived","!")

            elif self.pos_blue[int(player_num_coin) - 1] == -1 and self.blue_count == 6:
                self.blue_st_pos(player_num_coin)
                self.cordinates_blue[int(player_num_coin) - 1] = 40

            elif self.pos_blue[int(player_num_coin) - 1] > -1:
                take_cordinates = self.canvas_build.coords(self.blue_player[int(player_num_coin) - 1])
                sky_blue_start_label_x = take_cordinates[0] + 10
                sky_blue_start_label_y = take_cordinates[1] + 5
                self.label_blue[int(player_num_coin) - 1].place(x=sky_blue_start_label_x, y=sky_blue_start_label_y)

                if  self.pos_blue[int(player_num_coin) - 1] + self.blue_count <= 106:
                    self.pos_blue[int(player_num_coin) - 1] = self.coin_movement(self.pos_blue[int(player_num_coin) - 1], self.blue_player[int(player_num_coin) - 1], self.label_blue[int(player_num_coin) - 1], sky_blue_start_label_x, sky_blue_start_label_y, "sky_blue", self.blue_count)
                else:
                   messagebox.showerror("Not Available","Path")
                   
                   self.buttons_num_control(self.val_block_pred[1][2])
                   return

                if  self.pos_blue[int(player_num_coin)-1]==22 or self.pos_blue[int(player_num_coin)-1]==9 or self.pos_blue[int(player_num_coin)-1]==48 or self.pos_blue[int(player_num_coin)-1]==35 or self.pos_blue[int(player_num_coin)-1]==1 or self.pos_blue[int(player_num_coin)-1]==14 or self.pos_blue[int(player_num_coin)-1]==27 or self.pos_blue[int(player_num_coin)-1]==40:
                    pass
                else:
                    if self.pos_blue[int(player_num_coin) - 1] < 100:
                        self.cordinates_overlap(self.pos_blue[int(player_num_coin) - 1],color_coin, self.blue_count)

                self.cordinates_blue[int(player_num_coin) - 1] = self.pos_blue[int(player_num_coin) - 1]

            else:
                messagebox.showerror("Not Available", "Path")
                self.buttons_num_control(self.val_block_pred[1][2])
                return

            self.val_block_pred[1][1]['state'] = NORMAL

        print(self.cordinates_red)
        print(self.cordinates_green)
        print(self.cordinates_yellow)
        print(self.cordinates_blue)
        if self.comp_first == 1:
            print("Comp val is: ", self.comp_val)
        
        permission_granted_to_proceed = True

        if  color_coin == "red" and self.pos_red[int(player_num_coin)-1] == 106:
            permission_granted_to_proceed = self.win_pred(color_coin)
        elif  color_coin == "green" and self.pos_green[int(player_num_coin)-1] == 106:
            permission_granted_to_proceed = self.win_pred(color_coin)
        elif  color_coin == "yellow" and self.pos_yellow[int(player_num_coin)-1] == 106:
            permission_granted_to_proceed = self.win_pred(color_coin)
        elif  color_coin == "sky_blue" and self.pos_blue[int(player_num_coin)-1] == 106:
            permission_granted_to_proceed = self.win_pred(color_coin)

        if permission_granted_to_proceed:
            self.choice_sel(comp_op)

    def coin_movement(self,counter_coin,specific_coin,number_label,number_label_x ,number_label_y,color_coin,path_counter):
        try:
            number_label.place(x=number_label_x,y=number_label_y)
            while True:
                if path_counter == 0:
                    break
                elif (counter_coin == 51 and color_coin == "red") or (counter_coin==12 and color_coin == "green") or (counter_coin == 25 and color_coin == "yellow") or (counter_coin == 38 and color_coin == "sky_blue") or counter_coin>=100:
                    if counter_coin<100:
                        counter_coin=100

                    counter_coin = self.basic_under_control(specific_coin, number_label, number_label_x, number_label_y, path_counter, counter_coin, color_coin)

                    if  counter_coin == 106:
                        
                        if self.comp_first == 1 and color_coin == "red":
                            messagebox.showinfo("Home Arrived","!")
                        else:
                            messagebox.showinfo("Home Arrived","!")
                        if path_counter == 6:
                            self.max_cross = 1
                        else:
                            self.tm -= 1
                    break

                counter_coin += 1
                path_counter -=1
                number_label.place_forget()

                print(counter_coin)

                if counter_coin<=5:
                    self.canvas_build.move(specific_coin, 40, 0)
                    number_label_x+=40
                elif counter_coin == 6:
                    self.canvas_build.move(specific_coin, 40, -40)
                    number_label_x += 40
                    number_label_y-=40
                elif 6< counter_coin <=11:
                    self.canvas_build.move(specific_coin, 0, -40)
                    number_label_y -= 40
                elif counter_coin <=13:
                    self.canvas_build.move(specific_coin, 40, 0)
                    number_label_x += 40
                elif counter_coin <=18:
                    self.canvas_build.move(specific_coin, 0, 40)
                    number_label_y += 40
                elif counter_coin == 19:
                    self.canvas_build.move(specific_coin, 40, 40)
                    number_label_x += 40
                    number_label_y += 40
                elif counter_coin <=24:
                    self.canvas_build.move(specific_coin, 40, 0)
                    number_label_x += 40
                elif counter_coin <=26:
                    self.canvas_build.move(specific_coin, 0, 40)
                    number_label_y += 40
                elif counter_coin <=31:
                    self.canvas_build.move(specific_coin, -40, 0)
                    number_label_x -= 40
                elif counter_coin == 32:
                    self.canvas_build.move(specific_coin, -40, 40)
                    number_label_x -= 40
                    number_label_y += 40
                elif counter_coin <= 37:
                    self.canvas_build.move(specific_coin, 0, 40)
                    number_label_y += 40
                elif counter_coin <= 39:
                    self.canvas_build.move(specific_coin, -40, 0)
                    number_label_x -= 40
                elif counter_coin <= 44:
                    self.canvas_build.move(specific_coin, 0, -40)
                    number_label_y -= 40
                elif counter_coin == 45:
                    self.canvas_build.move(specific_coin, -40, -40)
                    number_label_x -= 40
                    number_label_y -= 40
                elif counter_coin <= 50:
                    self.canvas_build.move(specific_coin, -40, 0)
                    number_label_x -= 40
                elif 50< counter_coin <=52:
                    self.canvas_build.move(specific_coin, 0, -40)
                    number_label_y -= 40
                elif counter_coin == 53:
                    self.canvas_build.move(specific_coin, 40, 0)
                    number_label_x += 40
                    counter_coin = 1

                number_label.place_forget()
                number_label.place(x=number_label_x, y=number_label_y)

                self.gamePage.update()
                time.sleep(0.2)

            return counter_coin
        except:
            print("Stop the game, Rules are not followed")

    def cordinates_overlap(self, counter_coin, color_coin, path_to_traverse_before_overlap):
        if  color_coin!="red":
            for take_player_num_coin in range(len(self.cordinates_red)):
                if  self.cordinates_red[take_player_num_coin] == counter_coin:
                    if path_to_traverse_before_overlap == 6:
                        self.max_cross=1
                    else:
                        self.tm-=1

                    self.canvas_build.delete(self.red_player[take_player_num_coin])
                    self.label_red[take_player_num_coin].place_forget()
                    self.pos_red[take_player_num_coin] = -1
                    self.cordinates_red[take_player_num_coin] = -1
                    if self.comp_first == 1:
                        self.comp_val.remove(take_player_num_coin+1)
                        if self.pos_red.count(-1)>=1:
                            self.comp_start_val = 2

                    if take_player_num_coin == 0:
                       remade_coin = self.canvas_build.create_oval(100+40, 15+40, 100+40+40, 15+40+40, width=3, fill="red", outline="black")
                       self.label_red[take_player_num_coin].place(x=100 + 40 + 10, y=15 + 40 + 5)
                    elif take_player_num_coin == 1:
                        remade_coin = self.canvas_build.create_oval(100+40+60+60, 15 + 40, 100+40+60+60+40, 15 + 40 + 40, width=3, fill="red", outline="black")
                        self.label_red[take_player_num_coin].place(x=100 + 40 + 60 +60 + 10, y=15 + 40 + 5)
                    elif take_player_num_coin == 2:
                        remade_coin = self.canvas_build.create_oval(100 + 40 + 60 + 60, 15 + 40 + 100, 100 + 40 + 60 + 60 + 40, 15 + 40 + 40 + 100, width=3, fill="red", outline="black")
                        self.label_red[take_player_num_coin].place(x=100 + 40 + 60 + 60 + 10, y=15 + 40 + 100 + 5)
                    else:
                        remade_coin = self.canvas_build.create_oval(100 + 40, 15 + 40+100, 100 + 40 + 40, 15 + 40 + 40+100, width=3,fill="red", outline="black")
                        self.label_red[take_player_num_coin].place(x=100 + 40 + 10, y=15 + 40 + 100 + 5)

                    self.red_player[take_player_num_coin]=remade_coin

        if  color_coin != "green":
            for take_player_num_coin in range(len(self.cordinates_green)):
                if  self.cordinates_green[take_player_num_coin] == counter_coin:
                    if path_to_traverse_before_overlap == 6:
                        self.max_cross = 1
                    else:
                        self.tm-=1

                    self.canvas_build.delete(self.green_player[take_player_num_coin])
                    self.label_green[take_player_num_coin].place_forget()
                    self.pos_green[take_player_num_coin] = -1
                    self.cordinates_green[take_player_num_coin] = -1

                    if take_player_num_coin == 0:
                        remade_coin = self.canvas_build.create_oval(340+(40*3)+40, 15 + 40, 340+(40*3)+40 + 40, 15 + 40 + 40, width=3, fill="#00FF00", outline="black")
                        self.label_green[take_player_num_coin].place(x=340 + (40 * 3) + 40 + 10, y=15 + 40 + 5)
                    elif take_player_num_coin == 1:
                        remade_coin = self.canvas_build.create_oval(340+(40*3)+40+ 60 + 40+20, 15 + 40, 340+(40*3)+40 + 60 + 40 + 40+20, 15 + 40 + 40, width=3, fill="#00FF00", outline="black")
                        self.label_green[take_player_num_coin].place(x=340 + (40 * 3) + 40 + 40 + 60 + 30, y=15 + 40 + 5)
                    elif take_player_num_coin == 2:
                        remade_coin = self.canvas_build.create_oval(340 + (40 * 3) + 40 + 60 + 40 + 20, 15 + 40 + 100, 340 + (40 * 3) + 40 + 60 + 40 + 40 + 20, 15 + 40 + 40 + 100, width=3, fill="#00FF00", outline="black")
                        self.label_green[take_player_num_coin].place(x=340 + (40 * 3) + 40 + 40 + 60 + 30, y=15 + 40 + 100 + 5)
                    else:
                        remade_coin = self.canvas_build.create_oval(340+(40*3)+40, 15 + 40 + 100, 340+(40*3)+40 + 40, 15 + 40 + 40 + 100, width=3, fill="#00FF00", outline="black")
                        self.label_green[take_player_num_coin].place(x=340+(40*3) + 40 + 10, y=15 + 40 + 100 + 5)

                    self.green_player[take_player_num_coin] = remade_coin


        if  color_coin != "yellow":
            for take_player_num_coin in range(len(self.cordinates_yellow)):
                if  self.cordinates_yellow[take_player_num_coin] == counter_coin:
                    if path_to_traverse_before_overlap == 6:
                        self.max_cross = 1
                    else:
                        self.tm -= 1

                    self.canvas_build.delete(self.yellow_player[take_player_num_coin])
                    self.label_yellow[take_player_num_coin].place_forget()
                    self.pos_yellow[take_player_num_coin] = -1
                    self.cordinates_yellow[take_player_num_coin] = -1

                    if take_player_num_coin == 0:
                        remade_coin = self.canvas_build.create_oval(340 + (40 * 3) + 40, 340+80+15, 340 + (40 * 3) + 40 + 40, 340+80+40+15, width=3, fill="yellow", outline="black")
                        self.label_yellow[take_player_num_coin].place(x=340+(40*3) + 40 + 10, y=30 + (40*6)+(40*3)+40+10)
                    elif take_player_num_coin == 1:
                        remade_coin = self.canvas_build.create_oval(340 + (40 * 3) + 40 + 60 + 40 + 20, 340+80+15, 340 + (40 * 3) + 40 + 60 + 40 + 40+20, 340+80+40+15, width=3, fill="yellow", outline="black")
                        self.label_yellow[take_player_num_coin].place(x=340+(40*3)+ 40 + 40+ 60 + 30, y=30 + (40*6)+(40*3)+40+10)
                    elif take_player_num_coin == 2:
                        remade_coin = self.canvas_build.create_oval(340 + (40 * 3) + 40 + 60 + 40 + 20, 340 + 80 + 60 + 40 + 15, 340 + (40 * 3) + 40 + 60 + 40 + 40 + 20, 340 + 80 + 60 + 40 + 40 + 15, width=3, fill="yellow", outline="black")
                        self.label_yellow[take_player_num_coin].place(x=340+(40*3)+ 40 + 40+ 60 + 30, y=30 + (40*6)+(40*3)+40+100+10)
                    else:
                        remade_coin = self.canvas_build.create_oval(340 + (40 * 3) + 40, 340+80+60+40+15, 340 + (40 * 3) + 40 + 40,340+80+60+40+40+15, width=3, fill="yellow", outline="black")
                        self.label_yellow[take_player_num_coin].place(x=340 + (40 * 3) + 40 + 10, y=30 + (40 * 6) + (40 * 3) + 40 + 100 + 10)

                    self.yellow_player[take_player_num_coin] = remade_coin

        if  color_coin != "sky_blue":
            for take_player_num_coin in range(len(self.cordinates_blue)):
                if  self.cordinates_blue[take_player_num_coin] == counter_coin:
                    if path_to_traverse_before_overlap == 6:
                        self.max_cross = 1
                    else:
                        self.tm -= 1

                    self.canvas_build.delete(self.blue_player[take_player_num_coin])
                    self.label_blue[take_player_num_coin].place_forget()
                    self.pos_blue[take_player_num_coin] = -1
                    self.cordinates_blue[take_player_num_coin]=-1

                    if take_player_num_coin == 0:
                        remade_coin = self.canvas_build.create_oval(100 + 40, 340+80+15, 100 + 40 + 40, 340+80+40+15, width=3, fill="#04d9ff", outline="black")
                        self.label_blue[take_player_num_coin].place(x=100+40+10, y=30 + (40*6)+(40*3)+40+10)
                    elif take_player_num_coin == 1:
                        remade_coin = self.canvas_build.create_oval(100 + 40 + 60 + 40+20, 340+80+15, 100 + 40 + 60 + 40 + 40+20, 340+80+40+15, width=3, fill="#04d9ff", outline="black")
                        self.label_blue[take_player_num_coin].place(x=100 + 40 + 60 +60 + 10, y=30 + (40*6)+(40*3)+40+10)
                    elif take_player_num_coin == 2:
                        remade_coin = self.canvas_build.create_oval(100 + 40 + 60 + 40 + 20, 340 + 80 + 60 + 40 + 15, 100 + 40 + 60 + 40 + 40 + 20, 340 + 80 + 60 + 40 + 40 + 15, width=3, fill="#04d9ff", outline="black")
                        self.label_blue[take_player_num_coin].place(x=100 + 40 + 60 + 60 + 10, y=30 + (40 * 6) + (40 * 3) + 40 + 60 + 40 + 10)
                    else:
                        remade_coin = self.canvas_build.create_oval( 100 + 40, 340+80+60+40+15, 100 + 40 + 40, 340+80+60+40+40+15, width=3, fill="#04d9ff", outline="black")
                        self.label_blue[take_player_num_coin].place(x=100+40+10, y=30 + (40*6)+(40*3)+40+60+40+10)

                    self.blue_player[take_player_num_coin] = remade_coin


    def basic_under_control(self,specific_coin,number_label,number_label_x,number_label_y,path_counter,counter_coin,color_coin):
        if color_coin == "red" and counter_coin >= 100:
            if int(counter_coin)+int(path_counter)<=106:
               counter_coin = self.red_tr(specific_coin, number_label, number_label_x, number_label_y, path_counter, counter_coin)

        elif color_coin == "green" and counter_coin >= 100:
            if  int(counter_coin) + int(path_counter) <= 106:
                counter_coin = self.green_tr(specific_coin, number_label, number_label_x, number_label_y,path_counter,counter_coin)

        elif color_coin == "yellow" and counter_coin >= 100:
            if  int(counter_coin) + int(path_counter) <= 106:
                counter_coin = self.yellow_tr(specific_coin, number_label, number_label_x, number_label_y,path_counter,counter_coin)

        elif color_coin == "sky_blue" and counter_coin >= 100:
            if  int(counter_coin) + int(path_counter) <= 106:
                counter_coin = self.blue_tr(specific_coin, number_label, number_label_x, number_label_y,path_counter,counter_coin)

        return counter_coin


    def red_tr(self, specific_coin, number_label, number_label_x, number_label_y, path_counter, counter_coin):
        while path_counter>0:
            counter_coin += 1
            path_counter -= 1
            self.canvas_build.move(specific_coin, 40, 0)
            number_label_x+=40
            number_label.place(x=number_label_x,y=number_label_y)
            self.gamePage.update()
            time.sleep(0.2)
        return counter_coin

    def green_tr(self, specific_coin, number_label, number_label_x, number_label_y, path_counter, counter_coin):
        while path_counter > 0:
            counter_coin += 1
            path_counter -= 1
            self.canvas_build.move(specific_coin, 0, 40)
            number_label_y += 40
            number_label.place(x=number_label_x, y=number_label_y)
            self.gamePage.update()
            time.sleep(0.2)
        return counter_coin

    def yellow_tr(self, specific_coin, number_label, number_label_x, number_label_y,path_counter,counter_coin):
        while path_counter > 0:
            counter_coin += 1
            path_counter -= 1
            self.canvas_build.move(specific_coin, -40, 0)
            number_label_x -= 40
            number_label.place(x=number_label_x, y=number_label_y)
            self.gamePage.update()
            time.sleep(0.2)
        return counter_coin

    def blue_tr(self, specific_coin, number_label, number_label_x, number_label_y,path_counter,counter_coin):
        while path_counter > 0:
            counter_coin += 1
            path_counter -= 1
            self.canvas_build.move(specific_coin, 0, -40)
            number_label_y -= 40
            number_label.place(x=number_label_x, y=number_label_y)
            self.gamePage.update()
            time.sleep(0.2)
        return counter_coin

    def win_pred(self,color_coin):
        destination_reached = 0 
        if color_coin == "red":
            temp_store = self.cordinates_red
            temp_delete = 0
        elif color_coin == "green":
            temp_store = self.cordinates_green
            temp_delete = 3
        elif color_coin == "yellow":
            temp_store = self.cordinates_yellow
            temp_delete = 2
        else:
            temp_store = self.cordinates_blue
            temp_delete = 1

        for take in temp_store:
            if take == 106:
                destination_reached = 1
            else:
                destination_reached = 0
                break

        if  destination_reached == 1:
            self.seek_req += 1
            if self.seek_req == 1:
                if self.comp_first == 1 and color_coin == "red":
                    messagebox.showinfo("I am Winner", "!")
                else:
                    messagebox.showinfo("You are Winner","!")
            elif self.seek_req == 2:
                if self.comp_first == 1 and color_coin == "red":
                    messagebox.showinfo("I am first runner", "!")
                else:
                    messagebox.showinfo("You are first runner", "!")
            elif self.seek_req == 3:
                if self.comp_first == 1 and color_coin == "red":
                    messagebox.showinfo("I am second runner", "!")
                else:
                    messagebox.showinfo("You are second runner", "!")

            self.val_block_pred[temp_delete][1]['state'] = DISABLED
            self.max_players.remove(temp_delete)

            if len(self.max_players) == 1:
                messagebox.showinfo("Game finished","Thank You")
                self.val_block_pred[0][1]['state'] = DISABLED
                return False
            else:
                self.tm-=1
        else:
            print("Winner is not declared")

        return True

    def comp_choice(self, ind="give"):
        if ind == "give":
            all_in = 1
            for i in range(4):
                if self.pos_red[i] == -1:
                    all_in = 1
                else:
                    all_in = 0
                    break
            
            if all_in == 1:
                if self.red_count == 6:
                    predicted_coin = choice([1,2,3,4])
                    self.comp_val.append(predicted_coin)
                    self.game__control("red", predicted_coin)
                else:
                    pass
            else:
                temp = self.pos_red
                take_ref = self.pos_blue
                
                if len(self.comp_val) == 1:
                    if self.red_count<6:
                        if (self.comp_start_val>3) and (temp[self.comp_val[0]-1] >=33 and temp[self.comp_val[0]-1]<=38):
                            self.comp_start_val = 2
                        self.game__control("red", self.comp_val[0]) 
                    else:
                        forward_perm = 0
                        for coin in take_ref:
                            if coin>-1 and coin<101:
                                if (coin != 40 or coin != 35 or coin != 27 or coin != 22 or coin != 14 or coin != 9 or coin !=1 or coin !=48) and coin-temp[self.comp_val[0]-1] >= 6 and coin-temp[self.comp_val[0]-1] <= 12:
                                    forward_perm = 1
                                    break
                                else:
                                    forward_perm = 0
                            else:
                                forward_perm = 0

                        if forward_perm == 0:
                            store = [1,2,3,4]
                            store.remove(self.comp_val[0])
                            predicted_coin = choice(store)
                            self.comp_val.append(predicted_coin)
                            self.game__control("red", predicted_coin)
                        else:
                            self.game__control("red", self.comp_val[0])
                else:
                    def normal_movement_according_condition():
                        normal_movement = 1
                        
                        for coin in self.comp_val:
                            if temp[coin-1]+self.red_count <= 106:
                                pass
                            else:
                                normal_movement = 0
                                break

                        if normal_movement:
                            temp_comp_val = [coin for coin in self.comp_val]
                        else:
                            temp_comp_val = [coin for coin in self.comp_val if temp[coin-1]+self.red_count <= 106]

                      
                        for coin in temp_comp_val:
                            if len(temp_comp_val)>1 and temp[coin-1]<101:                          
                                if (temp[coin-1] in take_ref) and (temp[coin-1] != 1 or temp[coin-1] != 9 or temp[coin-1] != 14 or temp[coin-1] != 22 or temp[coin-1] != 27 or temp[coin-1] != 35 or temp[coin-1] != 40 or temp[coin-1] != 48):
                                    temp_comp_val.remove(coin)
                                elif temp[coin-1]<=39 and temp[coin-1]+self.red_count>39:                                    
                                    for loc_coin_other in take_ref:
                                        if (loc_coin_other>=40 and loc_coin_other<=46) and (temp[coin-1]+self.red_count>loc_coin_other):
                                            temp_comp_val.remove(coin)
                                            break

                      
                        process_forward = 1
                        for coin in temp_comp_val:
                            if temp[coin-1]+self.red_count in take_ref:
                                process_forward = 0
                                self.game__control("red", coin)
                                break
                        
                        if process_forward:
                            take_len = len(temp_comp_val)
                            store = {}
                            if take_ref:
                                for robo in temp_comp_val:
                                    for coin_other in take_ref:
                                        if coin_other>-1 and coin_other<100:
                                            if take_len>1 and (temp[robo-1]>38 and coin_other<=38) or ((temp[robo-1] == 9 or temp[robo-1] == 14 or temp[robo-1] == 27 or temp[robo-1] == 35 or temp[robo-1] == 40 or temp[robo-1] == 48 or temp[robo-1] == 22) and (coin_other<=temp[robo-1] or (coin_other>temp[robo-1] and coin_other<=temp[robo-1]+3))):  
                                                take_len-=1
                                            else:
                                                store[temp[robo-1]-coin_other] = (robo, take_ref.index(coin_other)+1)
                            
                            
                            if store:
                                store_positive_dis = {}
                                store_negative_dis = {}
                                take_max = 0
                                take_min = 0
                                
                                try:
                                    store_positive_dis = dict((k,v) for k,v in store.items() if k>0)
                                    take_min = min(store_positive_dis.items())
                                except:
                                    pass
                                try:
                                    store_negative_dis = dict((k,v) for k,v in store.items() if k<0)
                                    take_max = max(store_negative_dis.items())
                                except:
                                    pass
                                
                                
                                work_comp_in_pos = 0
                                take_len = len(store_positive_dis)
                                index_from_last = -1

                                while take_len:
                                    if take_min and take_min[0] <= 6:
                        
                                        work_comp_in_pos = 1
                                        self.game__control("red", take_min[1][0])
                                        break
                                    else:
                                        index_from_last -= 1
                                        try:
                                            take_min = min(sorted(store_positive_dis.items())[index_from_last])
                                        except:
                                            break
                                    take_len -= 1


                              
                                work_comp_in_neg = 0
                                if not work_comp_in_pos:
                                    take_len = len(store_negative_dis)
                                    index_from_last = len(store_negative_dis)-1
                                    while take_len:
                                        if take_max and temp[take_max[1][0]-1] + self.red_count <= take_ref[take_max[1][1]-1]:
                                            work_comp_in_neg = 1
                                            self.game__control("red", take_max[1][0])
                                            break
                                        else:
                                            index_from_last -= 1
                                            try:
                                                take_max = max(sorted(store_negative_dis.items())[index_from_last])
                                            except:
                                                break
                                        take_len -= 1
                        
                                
                                if not work_comp_in_neg and not work_comp_in_pos:
                                    close_to_dest = temp_comp_val[0]
                                    for coin_index in range(1,len(temp_comp_val)):
                                        if temp[temp_comp_val[coin_index]-1] > temp[close_to_dest-1]:
                                            close_to_dest = temp_comp_val[coin_index]
                        
                                    self.game__control("red", close_to_dest)
                            else:
                                close_to_dest = temp_comp_val[0]
                                for coin_index in range(1,len(temp_comp_val)):
                                    if temp[temp_comp_val[coin_index]-1] > temp[close_to_dest-1]:
                                        close_to_dest = temp_comp_val[coin_index]
                                self.game__control("red", close_to_dest)
                        else:
                            pass
                        
                    if self.red_count<6:
                        normal_movement_according_condition()
                    else:
                        coin_proceed = 0
                        
                        for coin in self.comp_val:
                            if temp[coin-1] + self.red_count in self.pos_blue:
                                coin_proceed = coin
                                break

                        if not coin_proceed:
                            if -1 in self.pos_red:
                                temp_store = [1,2,3,4]
                                for coin in self.comp_val:
                                    temp_store.remove(coin)
                                take_pred = choice(temp_store)
                                self.comp_val.append(take_pred)
                                self.game__control("red", take_pred)
                            else:
                                normal_movement_according_condition()
                        else:
                            self.game__control("red", coin_proceed)
        else:
            self.pred_val_prediction("red")

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

if __name__ == '__main__':
    

    gamePage = Tk()
    gamePage.geometry("850x680")
    gamePage.maxsize(850,680)
    gamePage.minsize(850,680)
    gamePage.title("Ludo Game")
    try:
        icon_path = resource_path("Images/game_board.png")
        icon_image = PhotoImage(file=icon_path)
        gamePage.iconphoto(False, icon_image)
    except Exception as e:
        print(f"Error loading icon: {e}")

    number6 = ImageTk.PhotoImage(Image.open(resource_path("Images/number6.png")).resize((33, 33)))
    number5 = ImageTk.PhotoImage(Image.open(resource_path("Images/number5.png")).resize((33, 33)))
    number4 = ImageTk.PhotoImage(Image.open(resource_path("Images/number4.png")).resize((33, 33)))
    number3 = ImageTk.PhotoImage(Image.open(resource_path("Images/number3.png")).resize((33, 33)))
    number2 = ImageTk.PhotoImage(Image.open(resource_path("Images/number2.png")).resize((33, 33)))
    number1 = ImageTk.PhotoImage(Image.open(resource_path("Images/number1.png")).resize((33, 33)))


    ludoGame(gamePage,number6,number5,number4,number3,number2,number1)
    gamePage.mainloop()