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

    root.mainloop()
