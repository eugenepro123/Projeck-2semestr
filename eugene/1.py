import tkinter as tk


class Vikno:
    def __init__(self,root):
        self.root=root
        self.root.title("Sea Battleship")
        self.btn= tk.Button(self.root,text="Морський бій")
        self.btn.pack(pady=150,padx=150)


if __name__=="__main__":
    root=tk.Tk()
    app=Vikno(root)
    root.mainloop()