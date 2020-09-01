from tkinter import*
from tkinter import ttk   #ttk are actually separate files in tkinter, this updates the original with improved widgets.  
import random



class Application(Frame):                          #Frame is a previously defined class/widget designed to be a container for other widgets, cannot exist without tk
    def __init__ (self,master):                    # 'master' is just the augment, in this example it will be root eg: Application(root) which is basically Tk() 
        Frame.__init__(self,master)                # Frame is just the container that is being created
        self.grid()                                # __init__ will call all data and methods below eg : self.create_widget                     
        self.create_widgets()                      
        self.gold=0                                 
        self.exp=0                              
        self.lexp=0
        self.level=0
        self.area=["Forest of the Chaos Harlequins ","Forgotten Graveyard of Endal","Castle of the Blackest Knight","Haunted Farm of Yondor","Deathtrap Dungeon of Borgon"," Mysterious Swampland of Kuluth",
         "Swamp of the Slimy Hobbits", "Darkest Dungeons", "Ruins of the Fallen Gods", "Forlorn Islands of Lost Souls","Hidden Hideout of Ninedeadeyes", "Wildlands of Lady L Moore"," Woods of Ypres","Heart of Darkness",
         "Doomville", "The Red Jester's Torture Chamber","The Goblins Fortress of Snikrik,"," Temple of Apshai"," Dungeons of Doom", "Mountains of the Wild Berserker","Stronghold of Daggerfall","Walking Hills of Cthulhu" ]

        self.monster=["orcs","goblins","dragons","demons","kobolds","blobs","hobbits","zombies","gnomes","vampires","beholders","trolls","hill giants","ettins","mimics",
                      "succubuses","bone devils","clay golems","drows","gnolls","swamp hags"," night goblins","half-ogres","hobgoblins","bog imps","owlbears","ponies","winter wolves","harlequin","abomination"]
        
        self.description=["stupid","horny","heart broken","deranged","morbid","tiny","suicidal","sexy","skinny","racist","peaceful","silly","drunk","sadistic","young", "shy","talkative",
                          "lovestruck","sarcastic","homophobic","forelorn","happy","friendly","psychopathic","optimistic","mysterious","beautiful","malnourish","zealous","hot-headed"]

        self.power_ranking=("The Village Punchbag (It's a job, i guess )")
        
    def create_widgets(self):

        self.bttn= Button(self)
        self.bttn["text"]="Explore"
        self.bttn["command"]= self.adventure
        self.bttn.grid(row=0,column=0,columnspan=1,sticky=W)
        
        self.stat_lbl=Label(self,text="Gold:0    EXP:0    LEVEL:0")
        self.stat_lbl.grid(row=0,column=1,columnspan=2,sticky=E)
        
        self.story_txt=Text(self,width=45, height=5,wrap=WORD)
        self.story_txt.grid(row=3, column=0, columnspan=3, sticky = W)

        self.stat_lbl1=Label(self,text="Power ranking: Ready to begin your quest from zero to hero ? ")
        self.stat_lbl1.grid(row=5,column=0,columnspan=2,sticky=W)

    


    
    def adventure(self):

        adventure=random.choice(self.area)
        adventure1=str(adventure)
        encounter=random.choice(self.monster)
        descript=random.choice(self.description)
        descript1=str(descript)
        encounter1=str(encounter)
        number=random.randrange(2,5)
        number1=str(number)
        reward=random.randrange(1,10)
        reward1=str(reward)
        exp=random.randrange(1,20)
        exp1=str(exp)
        self.gold+=reward
        self.exp+=exp
        self.lexp+=exp

        if self.lexp >123+(self.level*10):
            self.level+=1
            self.lexp=0

        if self.level >2 and self.level <4:
            self.power_ranking="The Cannon Fodder (Ready to die ? ) "  

        if self.level >4 and self.level  <6:
            self.power_ranking="The Weakling Avenger (At least your tried )"

        if self.level >6 and self.level  <8:
            self.power_ranking="The Nice Guy (This is no compliment )"

        if self.level >8 and self.level  <10:
            self.power_ranking="The Beta Warrior (At least you won't die first )"

        if self.level >10 and self.level  <12:
            self.power_ranking="The Mighty Beta Warrior (Some nerds respect you )"

        if self.level >12 and self.level  <14:
            self.power_ranking="The Average Chump (Nothing to see here ) "

        if self.level >14 and self.level  <16:
            self.power_ranking="The Man with a Stick (Fear my wood )  "

        if self.level >16 and self.level  <18:
            self.power_ranking="The Man with a Big Stick (MORE WOOD )"

        if self.level >18 and self.level  <20:
            self.power_ranking="The Town's Guard (Obey my authority ) "

        if self.level >20 and self.level  <24:
            self.power_ranking="The Try-Hard Hero (You win some, you lose more )"

        if self.level >24 and self.level  <26:
            self.power_ranking="The Goblin Slayer (Your reputation grows )"

        if self.level >26 and self.level  <28:
            self.power_ranking="The Orc Breaker (Orcs cower in your presence )"

        if self.level >28 and self.level  <30:
            self.power_ranking=" The Average Hero (Good but not great,keep fighting )"

        if self.level >30 and self.level  <32:
            self.power_ranking=" The Demon Demolisher (Guts will be proud of you )"

        if self.level >32 and self.level  <34:
            self.power_ranking=" The Master Killer (A black belt in DEATH )" 

        if self.level >34 and self.level  <40:
            self.power_ranking=" The Champion of Man (The best a man can be )"

        if self.level >40 and self.level  <70:
            self.power_ranking=" Legendary Hero (Well done. You can retire now )"

        if self.level >70 and self.level  <90:
            self.power_ranking=" Old Warrior (Why are you still playing ? )"

        if self.level >90 and self.level  <90:
            self.power_ranking="It's Over 9000 !! ( Seriously, quit it )"

        if self.level >100 :
            self.power_ranking="God (We bow down to your greatness )"

        

            

            
        
        

        story ="You explore the "
        story += adventure1
        story +="."
        story += " You encounter "
        story +=number1
        story +=" "
        story+=descript1
        story +=" "
        story += encounter1
        story +="."
        story += " You slay the "
        story += encounter1
        story +="."
        story += " You gain "
        story += reward1
        story += " gold and "
        story += exp1
        story += " exp"
        story +="."

        rank= "Power ranking: "
        rank+= self.power_ranking

        stat="Gold:"
        stat+=str(self.gold)
        stat+="    "
        stat+="EXP"
        stat+=str(self.exp)
        stat+="    "
        stat+="LEVEL:"
        stat+=str(self.level)

        
        

        
        self.story_txt.delete(0.0,END)
        self.story_txt.insert(0.0,story)

        self.stat_lbl["text"]=stat

        self.stat_lbl1["text"]=rank
        



root = Tk()
root.title(" One Click RPG ")
root.geometry("380x150")
app=Application(root)

root.mainloop()




