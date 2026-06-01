import tkinter as tk
import random

class Vikno:
    def __init__(self,root):
        self.root=root
        self.root.title("Sea Battleship")
        self.root.geometry("500x500")

        self.widget()

    def widget(self):#stvorenia knonpok
        self.label=tk.Label(self.root,text="Sea Battleship",font=("Arial",20)) #zrobili text
        self.label.pack(pady=20)

        self.button=tk.Button(self.root,text="Грати",font=("Arial",20),command=self.pochatok)
        self.button.pack(pady=20)

    def pochatok(self):
        self.label.config(text="Treba rozpochaty game")

        self.see=War(self.root,self.label)


class War:   #perepisav troshki kod tosho baran and robiv vse v odomu classi
    def __init__(self,root,main_label):
        self.root=root
        self.main_label=main_label
        self.gaypole=tk.Toplevel(self.root)
        self.gaypole.title("Gaypole")
        self.gaypole.attributes("-fullscreen",True)

        self.graves_data=[[0]*10 for i in range(10)]         #matruzi dla poliv
        self.robot_data = [[0] * 10 for i in range(10)]

        self.graves_buttons=[[None]*10 for i in range(10)]    #zapamiatovuvania knop
        self.robot_buttons=[[None]*10 for i in range(10)]

        self.korabliki_gravsa=20  #zagalna kilkist korablikiv
        self.war_start=False #pokazue chi war start

        self.knopa()
        self.robot_sili=[] #cherga koordinat dla korablika v iakii popali

        self.korabliki_robot()

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
            if self.war_start:
                return #war start i svoe pole nemozna chipati
            if self.graves_data[row][col] == 0 and self.korabliki_gravsa >0:
                self.graves_buttons[row][col].config(bg="gray")
                self.graves_data[row][col]=1 # tut korablik
                self.korabliki_gravsa-=1
                self.main_label.config(text=f"Залишилось розставити палуб:{self.korabliki_gravsa}")
                if self.korabliki_gravsa == 0:
                    self.war_start = True
        else:
            if not self.war_start:
                self.main_label.config(text="Treba postavit 20 korablikiv")
                return

            if self.robot_data[row][col] in[2,3]: #strilba po robotu
                return
            if self.robot_data[row][col]==1:   #popali
               self.robot_buttons[row][col].config(bg="red")
               self.robot_data[row][col]=3
            else:
               self.robot_buttons[row][col].config(bg="darkblue",text="•")
               self.robot_data[row][col]=2 #lox pomazav

               self.root.after(500, self.ataka_robota)


    def korabliki_robot(self):
        sh_size=[4,3,3,2,2,2,1,1,1,1]

        for s in sh_size:
            placed=False
            while not placed:
                napramok=random.choice(["Horison","Vertikal"]) #vibiraem vipadkovi napramok
                if napramok=="Horison":
                    r=random.randint(0,9)
                    c=random.randint(0,9- s +1) #shob ne vilis za pravii krai
                else:
                    r=random.randint(0 , 9- s +1)  #shob ne vilis vniz
                    c=random.randint(0,9)


                if self.perevirka_mizsa(r,c, s, napramok):  #perevirka susidnih klitinok
                    for i in range(s):
                        if napramok=="Horison":
                            self.robot_data[r][c+i]=1
                        else:
                            self.robot_data[r+i][c]=1
                    placed=True #korablik popliv,lets go dali



    def perevirka_mizsa(self,row,col,size,napramok):      #perevirka chi mozna stavit
        for i in range(size):
            m_r=row+(i if napramok=="Vertikal" else 0)
            m_c=col+(i if napramok=="Horison" else 0 )

            for dr in [-1,0,1]:   #perevirka vsi 8 klitinok navkolo
                for dc in [-1,0,1]:
                    ch_r=m_r+dr
                    ch_c=m_c+dc

                    if 0<=ch_r<10 and 0<=ch_c<10:  #if koordinati v mezah 10
                        if self.robot_data[ch_r][ch_c]==1:   #korablik vse e
                            return False
        return True
    def bilakorablika(self,start_r,start_c):  # bude znahodit klitinki bila pidbitih korabliv
        korabl=[]
        queue=[[start_r,start_c]]
        visit=set()

        while queue:
            r,c=queue.pop(0)
            if(r,c) in visit:
                continue
            visit.add((r,c))

            if self.graves_data[r][c] in [1,3]:  #if v siu klitinsi podbitiu or silii korablik
                korabl.append((r,c))
                for dr,ds in [(-1,0),(1,0),(0,-1),(0,1)]:
                    nr,nc=r+dr,c+ds
                    if 0<=nr<10 and 0<=nc<10:
                        if (nr,nc) not in visit:
                            queue.append((nr,nc))
        return korabl
    def obvodka(self,korabl):
        for r,c in korabl:
            for dr in [-1,0,1]:
                for dc in [-1,0,1]:
                    nr=r+dr
                    nc=c+dc
                    if 0<=nr<10 and 0<=nc<10:  #klitinka pusta,robot stavit promax
                        if self.graves_data[nr][nc]==0:
                            self.graves_data[nr][nc]=2
                            self.graves_buttons[nr][nc].config(bg="lightblue")




    def ataka_robota(self):
        r,c= -1,-1
        while self.robot_sili:
            poss_r,poss_c=self.robot_sili.pop(0) #beremo pershu sil iz spisku
            if self.graves_data[poss_r][poss_c] not in [2,3]:   #perevirka chi tuda ne strilali
                r,c=poss_r,poss_c
                break

        if r==-1 and c==-1: #vistrel navmania
            while True:
                r = random.randint(0, 9)
                c = random.randint(0, 9)
                if self.graves_data[r][c] not in [2, 3]:
                    break
        if self.graves_data[r][c] == 1:     #obrabotka postrilu
            self.graves_buttons[r][c].config(bg="darkred", text="x")
            self.graves_data[r][c] = 3

            pot =self.bilakorablika(r,c) #perevirka chi korabel potonuv povnistu
            potonuv=True
            for kr,kc in pot:
                if self.graves_data[kr][kc]==1:
                    potonuv=False
            if potonuv:
                self.obvodka(pot)
                self.robot_sili.clear()
            else:
                for dr,dc in [(-1,0),(0,-1),(1,0),(0,1)]: #znahodimo susidiv korablika

                    nast_r=r+dr
                    nast_c=c+dc
                    if 0<=nast_r<10 and 0<=nast_c<10: #chi ne vihodit za mezi
                        if self.graves_data[nast_r][nast_c] not in [2,3]:
                            self.robot_sili.append((nast_r,nast_c))
            self.root.after(500, self.ataka_robota)
        else: #promax
            self.graves_buttons[r][c].config(bg="blue",text="•")
            self.graves_data[r][c]=2












if __name__=="__main__":
    root=tk.Tk()
    app=Vikno(root)
    root.mainloop()