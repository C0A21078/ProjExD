import tkinter as tk
import maze_maker as mm

def key_down(event):
    global key
    key = event.keysym
    #print(f"{key}が押されました")  バインドしているかどうかの確認⇒ターミナル

def key_up(event):
    global key
    key = ""

def main_proc():
    global cx, cy, mx, my
    #delta = {
    #         "Up"   : [0,  -1],
    #         "Down" : [0,  +1],
    #         "Left" : [-1,  0],
    #         "Right": [+1,  0],
    #}
    #try:
    #    if maze_bg[mx+delta][key][0][mx+delta][key][0] == 0:
    #        my, mx = my+delta[key][1], mx+delta[key][0]
    #except:
    #    pass
    
    #cx, cy= cx+delta[key][0], cy+delta[key][1]

    if key == "Up"    and maze_bg[my-1][mx] == 0: my -= 1
    if key == "Down"  and maze_bg[my+1][mx] == 0: my += 1
    if key == "Left"  and maze_bg[my][mx-1] == 0: mx -= 1
    if key == "Right" and maze_bg[my][mx+1] == 0: mx += 1

    cx, cy = mx*100+50, my*100+50
    canvas.coords("tori", cx, cy)
    root.after(100, main_proc)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")


    canvas = tk.Canvas(root,
                       width= 1500,
                       height= 900,
                       bg="black"
                       )
    canvas.pack()
    maze_bg = mm.make_maze(15, 9)
    mm.show_maze(canvas, maze_bg)
    #print(maze_bg)  #確認,迷路

    tori = tk.PhotoImage(file="fig/8.png")
    #cx, cy = 300, 400
    mx, my = 1, 1
    
    cx, cy = mx*100+50, my*100+50
    canvas.create_image(cx, cy, image=tori, tag="tori")

    key = ""
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)

    main_proc()     
    root.mainloop()
