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

        self.ostalos={4:1,3:2,2:3,1:4}
        self.korabliki_gravsa=20                     #zagalna kilkist korablikiv
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

    def perevirka_dla_gravsa(self,row,col):
        for dr in [-1,0,1]: #proverka kletok vokrug
            for dc in [-1,0,1]:
                if dr != 0 and dc != 0:   #perevirka diagonalei
                    ch_r,ch_c=row+dr,col+dc
                    if 0 <= ch_r < 10 and 0 <= ch_c < 10:
                        if self.graves_data[ch_r][ch_c]==1:
                            return False   #if e korabliki diagonalno
        return True

    def skikikorablikiv(self):  #ogranishenie korabliv
        visited=set()
        spisokorabliv={4:0,3:0,2:0,1:0}
        for r in range(10):
            for c in range(10): #prohodit vsi 100 klitinok
                if self.graves_data[r][c]==1 and (r,c) not in visited:   #if znaishli korablik
                    koordinati=[] #koordinati korabla
                    queue=[(r,c)]

                    while queue:
                        curr_r,curr_c=queue.pop(0) #beremo pershy klitinku z cheri
                        if (curr_r,curr_c) in visited:
                            continue
                        visited.add((curr_r,curr_c)) #dobavlaem v nash korabl
                        koordinati.append((curr_r,curr_c))

                        for dr,dc in [(-1,0),(0,1),(0,-1),(1,0)]:
                            nr,nc=curr_r+dr,curr_c+dc
                            if 0<=nr<10 and 0<=nc<10:
                                if self.graves_data[nr][nc]==1 and (nr,nc) not in visited: #if radom korablik,v chergu uogo
                                    queue.append((nr,nc))
                    size=len(koordinati)
                    if size in spisokorabliv:
                        spisokorabliv[size]+=1
                    else: spisokorabliv[size]=99 #if stav bilshe 4
        return spisokorabliv #povertaim povni korabliki



    def nazat(self,row,col,robot):    #dla togo shob nazimat na polebou
        if not robot:
            if self.war_start:
                return #war start i svoe pole nemozna chipati
            if self.graves_data[row][col] == 0 and self.korabliki_gravsa >0:
                if not self.perevirka_dla_gravsa(row,col):  #perevirka diagonali
                    self.main_label.config(text="duze blizko")   #!!!!!!!!
                    return
                self.graves_data[row][col]=1  #na vremia stavim korablik
                kor=self.skikikorablikiv()

                zaBagato=False    #perevirka limitov
                for size,count in kor.items():
                    if size > 4:
                        zaBagato=True
                    elif count > self.ostalos[size]: #korabli takogo tipa bilshe niz nada
                        zaBagato=True

                if zaBagato:
                    self.graves_data[row][col]=0
                    self.main_label.config(text="zabagato korabliv")   #!!!!!!!!!!!
                    return

                self.graves_buttons[row][col].config(bg="gray")
                self.korabliki_gravsa-=1
                self.main_label.config(text=f"Залишилось розставити палуб:{self.korabliki_gravsa}")
                if self.korabliki_gravsa == 0:
                    self.war_start = True
                self.main_label.config(text="gra pochalas")


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


    def korabliki_robot(self): #robot roztavliae
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
                for dr,dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                    nr,nc=r+dr,c+dc
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


class МояГра(War):
    def __init__(self,baza,kolir,text):
        self.vibraniy_kolir=kolir  #зберігає колір
        super().__init__(baza,text)
        #назва змінних не важливі. ВАЖЛИВИЙ ПОРЯДОК(ROOT/MAIN_LABEL)
        #назад-команда евгенія. перевіряє клітини
        #self-на постійні данні
        self.gaypole.attributes("-fullscreen",False)
        self.gaypole.geometry("1200x800")
        self.gaypole.lift()
    def outro(self,resultat,foto_resultat):
        win=tk.Toplevel(self.gaypole)
        win.title("кінець")
        win.geometry("400x450")
        win.config(bg="white")
        tk.Label(win,text=resultat,font=("Arial",20,"bold"), bg="white").pack(pady=10)
        try:
            self.img_out=tk.PhotoImage(file=foto_resultat)
            tk.Label(win,image=self.img_out,bg="white").pack(pady=10)
        except Exception:
            tk.Label(win,text="[НЕМА КАРТИНКИ]",bg="white",fg="red").pack(pady=10)
        tk.Label(win,text="повернутись в головне меню?",font=("Arial",15),bg="white").pack(pady=10)
        btn_frame=tk.Frame(win,bg="white")
        btn_frame.pack(pady=15)
        tk.Button(btn_frame,text="так",font=("Arial",15,"bold"),bg="lightgreen",
            command=lambda:[win.destroy(),self.gaypole.destroy()]).pack(side="left",padx=20)
        tk.Button(btn_frame,text="ні",font=("Arial",12),bg="lightcoral",
                  command=self.root.quit).pack(side="left",padx=20)
    def nazat(self,row,col,robot):
        super().nazat(row,col,robot)
        if not robot and not self.war_start:
            if self.graves_data[row][col]==1:
                self.graves_buttons[row][col].config(bg=self.vibraniy_kolir)
        if self.war_start:
            if not any(1 in r for r in self.robot_data):
                self.outro("скоро людина замінить іі","../win.png")
            elif not any(1 in r for r in self.graves_data):
                self.outro("скоро іі замінить людину","../lose.png")
class golovnemenu:
    def __init__(self,baza):
        self.baza=baza
        self.baza.title("морський бій") #зверху
        self.baza.geometry("1000x1000")
        self.baza.config(bg="royalblue")
        self.baza.pack_propagate(False) #щоб розмір не залежал від довжини
        self.intro_vikno()#старт
    def intro_vikno(self):
        self.nazwa=tk.Label(self.baza,text="💥морський бій💥",font=("Arial",26,"bold"),bg="royalblue",fg="white")#сама рамка(текст.картинка) зручно переміщувати
        self.nazwa.pack(pady=30) #пркріплює по центру(відступ !-)
        try:
            self.foto=tk.PhotoImage(file="../korabel.png")
            self.kartinka_label=tk.Label(self.baza,image=self.foto,bg="darkblue") #щоб не було некрасивої рамки
            self.kartinka_label.pack(pady=10)
        except Exception:
            self.kartinka_label=tk.Label(self.baza,text="[картинка не заванатжилась ಥ_ಥ]",font=(15),bg="royalblue",fg="white")
            self.kartinka_label.pack(pady=20)
        self.start=tk.Button(self.baza,text="грати",font=("Arial",15,"bold"),bg="darkgreen",fg="white",padx=20,pady=10,relief="flat") #рель-контуур
        self.start.config(command=self.vibir_koloru_vikno)#сама кнопка ''прив1язуємо'' команду і при взаємодії відкривається вікно
        self.start.pack(pady=30)
    def vibir_koloru_vikno(self):
        self.nazwa.pack_forget()
        self.kartinka_label.pack_forget()
        self.start.pack_forget()
        self.kolir_label=tk.Label(self.baza,text="ОБЕРИ КОЛІР СВОГО ФЛОТУ",font=("Arial",20,"bold"),bg="royalblue",fg="white")
        self.kolir_label.pack(pady=40)
        self.btn_pink=tk.Button(self.baza,text="🌸рожевий🌸",font=("Arial",15,"bold"),bg="lightpink",fg="white",pady=10,relief="flat")
        self.btn_pink.config(command=lambda:self.start_pislia_intro("pink"))#lambada-команда в один рядок. запускає не одразу
        self.btn_pink.pack(pady=10,fill="x",padx=100) #fill-розтяг
        self.btn_yellow=tk.Button(self.baza,text="💛жовтий💛",font=("Arial",15,"bold"),bg="lightyellow",fg="black",pady=10,relief="flat")
        self.btn_yellow.config(command=lambda:self.start_pislia_intro("yellow"))
        self.btn_yellow.pack(pady=10,fill="x",padx=100)
        self.btn_green=tk.Button(self.baza,text="💚зелений💚",font=("Arial",15,"bold"),bg="lightgreen",fg="white",pady=10,relief="flat")
        self.btn_green.config(command=lambda:self.start_pislia_intro("green"))
        self.btn_green.pack(pady=10,fill="x",padx=100)
    def start_pislia_intro(self, vibraniy_kolir):
        self.kolir_label.pack_forget()
        self.btn_pink.pack_forget()
        self.btn_yellow.pack_forget()
        self.btn_green.pack_forget()
        self.igroviy_text=tk.Label(self.baza,text="підготовка до бою",font=("Arial",15,"bold"),bg="royalblue",fg="white")
        self.igroviy_text.pack(pady=10)
        self.see=МояГра(self.baza,vibraniy_kolir,self.igroviy_text)
if __name__=="__main__":#наге в пріорітеті
    baza=tk.Tk()#саме головне вікно
    app=golovnemenu(baza)#кидає в деф
    baza.mainloop()#очікування кліків
