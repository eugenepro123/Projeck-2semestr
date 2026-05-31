import tkinter as tk


class Vikno:
    def __init__(self,root):
        self.root=root
        self.root.title("Sea Battleship")
        self.root.geometry("500x500")
        #self.btn= tk.Button(self.root,text="Морський бій")
        #self.btn.pack(pady=150,padx=150)

        self.widget()

    def widget(self):#stvorenia knonpok
        self.label=tk.Label(self.root,text="Sea Battleship",font=("Arial",20)) #zrobili text
        self.label.pack(pady=20)

        self.button=tk.Button(self.root,text="Грати",font=("Arial",20),command=self.knopa)
        self.button.pack(pady=20)

    def knopa(self):
        self.label.config(text="Treba rozpochaty game")

        self.gaypole=tk.Toplevel(self.root)   #nashe pole dlia gri
        self.gaypole.title("Gaypole")

        self.gaypole.attributes("-fullscreen",True)

        gay_label=tk.Label(self.gaypole,text="Megaladon",font=("Arial",20))
        gay_label.pack(pady=20)

        close_button=tk.Button(self.gaypole,text="zakrit igru",command=root.destroy)
        close_button.pack(pady=20)









if __name__=="__main__":
    root=tk.Tk()
    app=Vikno(root)
    root.mainloop()