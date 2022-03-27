#!/usr/bin/env python3

VERSION="1.0"

WIDTH,HEIGHT=720,540
PAD=20
OFFSET=1

FGCOLOR,BGCOLOR="#C0C0C0","#121212"

from tkinter import Tk, Canvas
from PIL import Image, ImageTk, ImageDraw

root = Tk()

root.title("Snake v" + VERSION)
root.resizable(False, False)

canvas = Canvas(root, width=WIDTH+(PAD*2), height=HEIGHT+(PAD*4), background=BGCOLOR, highlightthickness=0)
canvas.create_rectangle(PAD-OFFSET, PAD*3-OFFSET, WIDTH+PAD+OFFSET, HEIGHT+(PAD*3)+OFFSET, outline=FGCOLOR)

canvas.pack()
root.mainloop()
