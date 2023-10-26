from tkinter import *

ScreenX = 400
ScreenY = 400

root = Tk()
root.title("Dvoryanchikov | Laba3/drawing-lines/NaturalAlgorithm")
root.geometry(str(ScreenX)+'x'+str(ScreenY))
root.resizable(False, False)

cnv = Canvas(bg="white", width=ScreenX, height=ScreenY)
cnv.pack(anchor=N, fill="both", expand=1)

def ClearScreen(event):
    cnv.delete("all")

def ClearСursor(event):
    cnv.delete("ln")

def Сursor(event):
    x = event.x
    y = event.y
    cnv.delete("ln")
    cnv.create_line(x,0,x,ScreenY, fill="red", tag="ln")
    cnv.create_line(0, y, ScreenX, y, fill="red", tag="ln")
    cnv.create_text(x - 90, y - 17, font="TimesNewRoman 10", anchor=NW, text="x: " + str(x) + " | y: " + str(y),
                    fill="#00BFFF", tag="ln")
    cnv.create_text(40, 10, text="x: " + str(x) + " | y: " + str(y), fill="#00BFFF", tag="ln")

x0 = 0
y0 = 0
def PointXY(event):
    global x0
    global y0
    x0 = event.x
    y0 = event.y
    cnv.create_oval(x0-5, y0-5, x0+5, y0+5, fill="#80CBC4", outline="#004D40")
    cnv.create_text(x0, y0+12, text="0 | x: " + str(x0) + " | y: " + str(y0), fill="#00BFFF")

x1 = 0
y1 = 0
def Point_X_Y(event):
    global x1
    global y1
    x1 = event.x
    y1 = event.y
    cnv.create_oval(x1-5, y1-5, x1+5, y1+5, fill="#80CBC4", outline="#004D40")
    cnv.create_text(x1, y1+12, text="1 | x: " + str(x1) + " | y: " + str(y1), fill="#00BFFF")

def Point(x, y):
    cnv.create_rectangle(x, y, x + 1, y + 1, fill="#80CBC4", outline="#004D40")

def NaturalAlgorithm(event):
    x = x0
    y = y0
    dx = x1 - x0
    dy = y1 - y0
    m = 0
    e = m-1/2
    i = 0
    j = 0
    Point(x,y)

    if dx != 0:
        # Алгоритм для 1 части круга
        if (abs(dy / dx) <= 1) and (dy / dx >= 0):
            m = dy / dx
            while i<=dx:
                if e>=0:
                    y = y + 1
                    e = e + abs(m) - 1
                else:
                    e = e + abs(m)
                x = x + 1
                Point(x, y)
                i = i + 1

        # Алгоритм для 4 части круга
        if (abs(dy / dx) <= 1) and (dy / dx <= 0):
            m = dy / dx
            while i>=dx:
                if e<0:
                    y = y + 1
                    e = e - abs(m) + 1
                else:
                    e = e - abs(m)
                x = x - 1
                Point(x, y)
                i = i - 1

        # Алгоритм для 5 части круга
        if (abs(dy / dx) < 1) and (dy / dx >= 0):
            m = dy / dx
            while i >= dx:
                if e < 0:
                    y = y - 1
                    e = e - abs(m) + 1
                else:
                    e = e - abs(m)
                x = x - 1
                Point(x, y)
                i = i - 1

        # Алгоритм для 8 части круга
        if (abs(dy / dx) <= 1) and (dy / dx <= 0):
            m = dy / dx
            while i <= dx:
                if e >= 0:
                    y = y - 1
                    e = e + abs(m) - 1
                else:
                    e = e + abs(m)
                x = x + 1
                Point(x, y)
                i = i + 1

    if dy != 0:
    # Алгоритм для 2 части круга
        if (abs(dx / dy) <= 1) and (dx / dy >= 0):
            m = dx / dy
            while j<=dy:
                if e>=0: #Меняется в зависимости от оси Y отражения по
                    x = x + 1 #Для положительной Оси Y
                    e = e + abs(m) - 1
                else:
                    e = e + abs(m)
                y = y + 1
                Point(x, y)
                j = j + 1

        # Алгоритм для 3 части круга
        if (abs(dx / dy) <= 1) and (dx / dy <= 0):
            m = dx / dy
            while j<=dy:
                if e>=0:
                    x = x - 1
                    e = e + abs(m) - 1
                else:
                    e = e + abs(m)
                y = y + 1
                Point(x, y)
                j = j + 1

        # Алгоритм для 6 части круга
        if (abs(dx / dy) <= 1) and (dx / dy >= 0):
            m = dx / dy
            while j>=dy:
                if e<0: #Меняется в зависимости от оси Y отражения по
                    x = x - 1 #Для положительной Оси Y
                    e = e - abs(m) + 1
                else:
                    e = e - abs(m)
                y = y - 1
                Point(x, y)
                j = j - 1

        # Алгоритм для 7 части круга
        if (abs(dx / dy) < 1) and (dx / dy <= 0):
            m = dx / dy
            while j>=dy:
                if e<0:
                    x = x + 1
                    e = e - abs(m) + 1
                else:
                    e = e - abs(m)
                y = y - 1
                Point(x, y)
                j = j - 1






root.bind("<Left>", PointXY)
root.bind("<B1-Motion>", Сursor)
root.bind("<B3-Motion>", ClearСursor)
root.bind("<Right>", Point_X_Y)
root.bind("<Return>", NaturalAlgorithm)
root.bind("<Delete>", ClearScreen)
root.mainloop()