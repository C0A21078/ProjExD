import tkinter as tk
import tkinter.messagebox as tkm

def button_click(event):
    btn = event.widget
    num = btn["text"]
    if num == "=":
        eqn = entry.get()
        res = eval(eqn)
        entry.delete(0, tk.END)
        entry.insert(tk.END, res)
    else:
        ##tkm.showinfo("",f"{num}のボタンがクリックされました")
        entry.insert(tk.END, num)

#簡易的な電卓作ってみた！

if __name__ == "__main__":
   root = tk.Tk()
   root.title("簡易的な電卓作ってみた！")
   #root.geometry("300x500")
   
   entry = tk.Entry(root,justify="right", width=10, font=("Times New Roman",40))
   entry.grid(row=0, column=0, columnspan=3)
   
   r, c = 1, 0 #行列
   for i,num in enumerate([1,2,3,4,5,6,7,8,9,0,"=","+"]):
       btn = tk.Button(root, 
                       text=f"{num}", 
                       width=4, 
                       height=2,
                       font=("Times New Roman", 30)
                      )
       btn.bind("<1>", button_click)
       btn.grid(row=r, column=c)

       c += 1
       if (i+1)%3 == 0:
           r += 1
           c = 0
    
root.mainloop()
