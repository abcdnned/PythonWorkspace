from thing import *
from math import ceil
from building import *
from item import *
from jinja2 import Environment,FileSystemLoader
from gameshell import GameShell
from gameshell import PAGE_SIZE
from worker import *
from clan import Clan
import threading
import cPickle as pickle
import pygame

DAY_SECS=5

def saveObject(obj, filename):
    with open(filename, 'w') as output:
        pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)

DATA_CLAN='clan.sv'

def loadClan():
    with open(DATA_CLAN,'r') as i:
        return pickle.load(i)

env=Environment(loader=FileSystemLoader('./templates'))

class subpanel(object):

    def __init__(self):
        self.page_curr=-1
        self.page_max=-1

    def getkey(self):
        pass

    def after(self,k):
        if k==pygame.K_UP:
            self.page_curr=max(0,self.page_curr-1)
        elif k==pygame.K_DOWN:
            self.page_curr=min(self.get_page_max(),self.page_curr+1)
        self.afterafter(k)

    def afterafter(self,k):
        pass

    def enter(self):
        self.page_curr=0

    def get_page_max(self):
        return 1

    def quit(self):
        self.page_curr=-1
        self.page_max=-1

    def render(self,cache):
        pass


class PropertyPanel(subpanel):

    def property_type(self):
        return THING_ITEM

    def getkey(self):
        return pygame.K_p

    def get_page_max(self):
        count=len(filter(lambda i:i[0].cata==self.property_type(),Clan.thing.items()))
        return ceil(float(count)/(2*PAGE_SIZE))-1

    def render(self):
        l=[]
        its=filter(lambda i:i[0].cata==self.property_type(),Clan.thing.items())
        s=''
        for i in range(0,len(its)):
            s+=fillblank('='.join([its[i][0].name,str(its[i][1])]))
            if (i+1)%3==0:
                l.append(s)
                s=''
        if len(s)>0:
            l.append(s)
        c=self.page_curr*PAGE_SIZE
        return l[c:c+PAGE_SIZE]
        
class Wpanel(PropertyPanel):
    def getkey(self):
        return pygame.K_w

    def property_type(self):
        return THING_WORKER

class Ppanel(PropertyPanel):
    def getkey(self):
        return pygame.K_p

class Tpanel(subpanel):
    def getkey(self):
        return pygame.K_t
    
    def render(self):
        for task_cata in TASKS:



ppanel=Ppanel()
tpanel=Tpanel()
wpanel=Wpanel()

COLUMN_WIDTH=30 

def fillblank(s):
    for i in range(0,PAGE_SIZE-len(s)):
        s+=' '
    return s

class SagaShell(GameShell):
    SAVE_ALL=0
        
    def load(self):
        loadClan()
        
        self.title='DAYS={:<20}WALL={:<20}FOOD={:<20}POPULATION={:<20}'.format(Clan.days,Clan.wall,Clan.food,Clan.population)

    def init(self):
        Clan.population=10
        Clan.food=1000
        Clan.wall=100
        Clan.days=1
        Clan.thing=dict()
        Clan.thing[idle]=10
        Clan.thing[axe]=5
        Clan.thing[seed]=5
        Clan.thing[pickaxe]=5
        Clan.thing[wood]=50
        Clan.thing[stone]=50
        Clan.thing[gold]=100
        Clan.starv=0

        self.save()

    def consume(self):
        Clan.food=max(0,Clan.food-Clan.population)
        if Clan.food==0:
            Clan.starv+=1
        elif Clan.starv>0:
            Clan.starv=0

    def promote(self,cl):
        n=1
        product=farmer
        elements=[[worker,1]]
        Clan.thing[farmer]=Clan.thing[farmer]+n if farmer in Clan.thing else n

    def assign(self,cl):
        n=1
        man_type=farmer
        task_type=farm
        task_arg=cl[3:]
        task_type.assign(farmer,n,task_arg)


    def command(self,cmd):
        cl=cmd.split(' ')
        exec 'self.'+cl[0]+'(cl[1:])'


    def produce(self):
        pass        

    def tick(self):
        threading.Timer(DAY_SECS,self.tick).start()
        Clan.days+=1
        self.updateTitle()
        self.consume()
        self.produce()
        self.render()
    
    def check(self):
        return False

    def save(self):
        saveObject(Clan,DATA_CLAN)

    def updateTitle(self):
        self.title='DAYS={:<20}WALL={:<20}FOOD={:<20}POPULATION={:<20}'.format(Clan.days,Clan.wall,Clan.food,Clan.population)

    def interact(self,event):
        if event.type==pygame.KEYDOWN:
            if self.mod==0:
                for panel in self.panels:
                    if panel.getkey()==event.key:
                        panel.enter()
                        self.mod=1
                        self.curr_panel=panel
                        self.curr_panel.page_curr=min(self.curr_panel.page_curr,self.curr_panel.get_page_max())
                        self.cache=self.curr_panel.render()
                        self.render()
                        break
            elif self.mod==1:
                if event.key==self.curr_panel.getkey():
                    self.curr_panel.quit()
                    self.mod=0
                    self.cache=[]
                    self.curr_panel=None
                    self.render()
                else :
                    self.curr_panel.after(event.key)
                    self.render()


    def getTitle(self):
        return 'ClanSaga'

    def __init__(self):
        super(SagaShell,self).__init__()
        for i in range(0,PAGE_SIZE):
            self.addline(str(i))
        self.foot=["w=worker list  p=property list"]
        if not self.check():
            self.init()
        self.load()

        self.panels=[]
        self.panels.append(ppanel)
        self.panels.append(tpanel)
        self.panels.append(wpanel)

        self.curr_panel=None
        
    def prepare(self):
        self.tick()

game = SagaShell()
game.start()
