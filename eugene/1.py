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

        self.button=tk.Button(self.root,text="Грати",font=("Arial",20),command=self.pochatok)
        self.button.pack(pady=20)

    """def knopa(self):
        self.label.config(text="Treba rozpochaty game")

        self.gaypole=tk.Toplevel(self.root)   #nashe pole dlia gri
        self.gaypole.title("Gaypole")

        self.gaypole.attributes("-fullscreen",True)

        gay_label=tk.Label(self.gaypole,text="Megaladon",font=("Arial",20))
        gay_label.place(relx=0.46,rely=0.05)     # koordinat ekranu u vidsotkax x=shirina y=visota

        label1 = tk.Label(self.gaypole, text="Твоє поле", font=("Arial", 16), bg="lightblue")
        label1.place(relx=0.15,rely=0.2)

        label2 = tk.Label(self.gaypole, text="Поле робота", font=("Arial", 16), bg="yellow")
        label2.place(relx=0.79,rely=0.2)

        close_button=tk.Button(self.gaypole,text="zakrit igru",command=root.destroy)
        close_button.place(relx=0.49,rely=0.9)"""
    def pochatok(self):
        self.label.config(text="Treba rozpochaty game")

        self.see=War(self.root)


class War:   #perepisav troshki kod tosho baran and robiv vse v odomu classi
    def __init__(self,root):
        self.root=root
        self.gaypole=tk.Toplevel(self.root)
        self.gaypole.title("Gaypole")
        self.gaypole.attributes("-fullscreen",True)

        self.knopa()

    def knopa(self):
        gay_label = tk.Label(self.gaypole, text="Megaladon", font=("Arial", 20))
        gay_label.place(relx=0.46, rely=0.05)  # koordinat ekranu u vidsotkax x=shirina y=visota

        label1 = tk.Label(self.gaypole, text="Твоє поле", font=("Arial", 16), bg="lightblue")
        label1.place(relx=0.15, rely=0.2)

        label2 = tk.Label(self.gaypole, text="Поле робота", font=("Arial", 16), bg="yellow")
        label2.place(relx=0.79, rely=0.2)

        close_button = tk.Button(self.gaypole, text="zakrit igru", command=root.destroy)
        close_button.place(relx=0.49, rely=0.9)







if __name__=="__main__":
    root=tk.Tk()
    app=Vikno(root)
    root.mainloop()