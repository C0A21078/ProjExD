import tkinter as tk

if __name__ == "__main__":
    #1
    root = tk.Tk()
    root.title("迷えるこうかとん")
    #2
    root.mainloop()
    canvas = tk.Canvas(root,
                       width= 1500,
                       height= 900,
                       bg="cyan"
                       )
    canvas.pack()
    canvas = tk.Canvas(root)
    koukaton = tk.PhotoImage(file="./fig/5.png")
    cx, cy = 300, 400
    canvas.create_image(cx, cy, image=koukaton, tag="koukaton")
