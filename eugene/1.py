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

    def pochatok(self):
        self.label.config(text="Treba rozpochaty game")

        self.see=War(self.root)


class War:   #perepisav troshki kod tosho baran and robiv vse v odomu classi
    def __init__(self,root):
        self.root=root
        self.gaypole=tk.Toplevel(self.root)
        self.gaypole.title("Gaypole")
        self.gaypole.attributes("-fullscreen",True)

        self.graves_data=[[0]*10 for i in range(10)]         #matruzi dla poliv
        self.robot_data = [[0] * 10 for i in range(10)]

        self.graves_buttons=[[None]*10 for i in range(10)]    #zapamiatovuvania knop
        self.robot_buttons=[[None]*10 for i in range(10)]

        self.knopa()

    def knopa(self):

        gay_label = tk.Label(self.gaypole, text="Megaladon", font=("Arial", 20))
        gay_label.place(relx=0.46, rely=0.05)  # koordinat ekranu u vidsotkax x=shirina y=visota
#pola gravsa
        label1 = tk.Label(self.gaypole, text="Твоє поле", font=("Arial", 16), bg="lightblue")
        label1.place(relx=0.2, rely=0.1)

        graves_frame = tk.Frame(self.gaypole, bg="lightblue")
        graves_frame.place(relx=0.03, rely=0.2)
        self.sitka(graves_frame, self.graves_buttons, isrb=False)


#pole robota
        label2 = tk.Label(self.gaypole, text="Поле робота", font=("Arial", 16), bg="yellow")
        label2.place(relx=0.7, rely=0.1)

        robot_frame = tk.Frame(self.gaypole, bg="lightblue")
        robot_frame.place(relx=0.53, rely=0.2)
        self.sitka(robot_frame, self.robot_buttons, isrb=True)

        close_button = tk.Button(self.gaypole, text="zakrit igru", command=self.gaypole.destroy)
        close_button.place(relx=0.49, rely=0.9)

    def sitka(self,frame,knopi_mat,isrb):
        for r in range(10):
            for c in range(10):   #lambda zamoroshey do momentu cliku
                btn=tk.Button(
                    frame,
                    width=8,height=3,bg="white",
                    command=lambda row=r,col=c,robot=isrb: self.nazat(row,col,robot) )

                btn.grid(row=r,column=c,padx=1,pady=1)

                knopi_mat[r][c]=btn

    def nazat(self,row,col,robot):    #dla togo shob nazimat na polebou
        if not robot:
            self.graves_buttons[row][col].config(bg="gray")
            self.graves_data[row][col]=1 # tut korablik
        else:
            self.robot_buttons[row][col].config(bg="Red",text="X")
            self.robot_data[row][col]=3 #pidbili


if __name__=="__main__":
    root=tk.Tk()
    app=Vikno(root)
    root.mainloop()