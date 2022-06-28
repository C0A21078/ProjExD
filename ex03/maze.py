import tkinter as tk
#5
def key_down(event):
    global key
    key = event.keysym
    #print(f"{key}が押されました")  バインドしているかどうかの確認⇒ターミナル

#6
def key_up(event):
    global key
    key = ""

#7
def main_proc():
    global cx, cy
    #delta = {                   #key:押されているkeyの値[x, y]
    #         ""     : [0,   0],
    #        "Up"   : [0, -20],
    #         "Down" : [0, +20],
    #         "Left" : [-20, 0],
    #         "Right": [+20, 0],
    #        }
    #cx, cy= cx+delta[key][0], cy+delta[key][1]
    if key == "Up": cy -= 20
    if key == "Down": cy +=20
    if key == "Left": cx -=20
    if key == "Right": cx +=20

    canvas.coords("tori", cx, cy)
    root.after(10, main_proc)


if __name__ == "__main__":
    #1
    root = tk.Tk()
    root.title("迷えるこうかとん")

    #2
    canvas = tk.Canvas(root,
                       width= 1500,
                       height= 900,
                       bg="black"
                       )
    canvas.pack()

    #3
    tori = tk.PhotoImage(file="fig/8.png")
    cx, cy = 300, 400
    canvas.create_image(cx, cy, image=tori, tag="tori")

    #4
    key = ""
    #5
    root.bind("<KeyPress>", key_down)
    #6
    root.bind("<KeyRelease>", key_up)

    main_proc()     
    root.mainloop()
