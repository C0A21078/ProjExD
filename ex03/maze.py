import tkinter as tk
import maze_maker as mm

def key_down(event):
    global key
    key = event.keysym
def key_up(event):
    global key
    key = ""

def main_proc():
    global cx, cy, mx, my
    if key == "Up"    and maze_bg[my-1][mx] == 0: my -= 1
    if key == "Down"  and maze_bg[my+1][mx] == 0: my += 1
    if key == "Left"  and maze_bg[my][mx-1] == 0: mx -= 1
    if key == "Right" and maze_bg[my][mx+1] == 0: mx += 1
    cx, cy = mx*100+50, my*100+50
    canvas.coords("tori", cx, cy)
    root.after(100, main_proc)
    
    canvas.create_rectangle(mx*100+100,my*100+100,mx*100,my*100,fill="skyblue",width=0,tag="tori")
    canvas.delete(tori)  #一旦消す
    canvas.create_image(mx*100+40,my*100+40,image = tori)



if __name__ == "__main__":
    root = tk.Tk()
    root.title("ヘンゼルとグレーテルに影響を受けたこうかとん")
    canvas = tk.Canvas(root,
                       width= 1500,
                       height= 900,
                       bg="black"
                       )
    canvas.pack()
    maze_bg = mm.make_maze(15, 9)
    mm.show_maze(canvas, maze_bg)
    tori = tk.PhotoImage(file="fig/8.png")

    mx, my = 1, 1
    cx, cy = mx*100+50, my*100+50
    canvas.create_image(cx, cy, image=tori, tag="tori")

    key = ""
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)

    main_proc()     
    root.mainloop()
