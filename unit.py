from math import ceil
from random import *

POS_FRONT=0
POS_BACK=1

class unit(object):
    def __init__(self,pos,melee,will,damage,shoot,armor,power,speed):
        self.pos=pos
        self.melee=melee
        self.will=will
        self.damage=damage
        self.shoot=shoot
        self.armor=armor
        self.power=power
        self.speed=speed

class army(object):
    def __init__(self):
        self.front={}
        self.hero=[]
        self.back={}
        self.front_number=0
        self.back_number=0

    def leader(self,hero):
        self.hero.append(hero)
    
    def subtract(self,group):
        if self.back_number<group.back_number or self.front_number<group.front_number:
            return self
        for k in gourp.front.keys:
            self.front[k]-=group.front[k]
        for k in gourp.back.keys:
            self.back[k]-=group.back[k]


    def random_group(self,n):
        group=army()
        fn=0
        bn=0
        if self.front_number>=n:
            fn=n
            bn=0
        elif self.back_number>n-self.front_number:
            fn=self.front_number
            bn=n-self.front_number
        else
            return self
        
        if fn>0:
            pick_li=[]
            for key in self.front.keys:
                pick_li.append(self.front[key])
            for i in range(0,fn):
                r=randint(1,self.front_number)
                j=0
                for cata_num in pick_li:
                    if cata_num>r:
                        break
                    else:
                        j+=1
                        r-=cata_num
                pick_li[j]-=1
                group.front[self.front.keys[j]]=group.front[self.front.keys[j]]+1 if self.front.keys[j] in group.front else 1
        if bn>0:
            pick_li=[]
            for key in self.back.keys:
                pick_li.append(self.back[key])
            for i in range(0,fn):
                r=randint(1,self.back_number)
                j=0
                for cata_num in pick_li:
                    if cata_num>r:
                        break
                    else:
                        j+=1
                        r-=cata_num
                pick_li[j]-=1
                group.back[self.back.keys[j]]=group.back[self.back.keys[j]]+1 if self.back.keys[j] in group.back else 1

        return group

                    


    def dismiss(self,man,num):
        if man in self.front:
            self.front[man]-=1
            if self.front[man]<0:
                del self.front[man]
            self.front_number-=1
            return True
        elif man in self.back:
            self.back[man]-=1
            if self.back[man]<0:
                del self.back[man]
            self.back_number-=1
            return True
        return False

    def join(self,man,num):
        if man.pos==POS_FRONT:
            self.front[man]=self.front[man]+num if man in self.front else num
            self.front_number+=1
        else:
            self.back[man]=self.back[man]+num if man in self.back else num
            self.back_number+=1

def pay(dmg,army,dead_army):
    for i in range(0,min(dmg,army.front_num)):
        choose_to_dead=choose(army,True,front_num)
        army.front[choose_to_dead]-=1
        dead_army.[choose_to_dead]=dead_army[choose_to_dead]+1 if choose_to_dead in dead_army else 1
        if army.front[choose_to_dead]<0:
            del army.front[choose_to_dead]
        dmg-=1
    back_num=0
    for man in army.back.keys():
        back_num+=army.back[man]
    for i in range(0,min(dmg,back_num)):
        choose_to_dead=choose(army,False,back_num)
        army.back[choose_to_dead]-=1
        if army.back[choose_to_dead]<0:
            del army.back[choose_to_dead]
        dmg-=1

    return dmg>0

def get_range_dmg(army):
    dmg=0
    for man in army.back.keys():
        dmg+=man.shoot*army.back[man]
    for man in army.front.keys():
        dmg+=man.shoot*army.front[man]
    for hero in army.hero:
        dmg+=hero.shoot
    return dmg

def get_mgic_dmg(army):
    dmg=0
    for man in army.back.keys():
        dmg+=man.power*army.back[man]
    for man in army.front.keys():
        dmg+=man.power*army.front[man]
    for hero in army.hero:
        dmg+=hero.power
    return dmg
    

def get_armor(army):
    armor=0
    if len(army.front.keys())>0:
        for man in army.front.keys():
            armor+=army.front[man]*man.armor
        return armor
    elif len(army.back.keys())>0:
        for man in army.back.keys():
            armor+=army.back[man]*man.armor
        return armor
    return armor

def get_will(army):
    will=0
    for man in army.back.keys():
        will+=man.will*army.back[man]
    for man in army.front.keys():
        will+=man.will*army.front[man]
    for hero in army.hero:
        will+=hero.shoot
    return will

def caculate_range_dmg(army1,army2):
    return dmg=get_range_dmg(army1)+get_magic_dmg(army1)-ceil(1.5*get_armor(army2))-get_will(army2)


def fight(army1,army2,distance):
    dead_army1={}
    dead_army2={}
    log=[]
    
    before_siege=1
    
    while distance>0:
        distance-=1
        dmg1=caculate_range_dmg(army1,army2)
        dmg2=caculate_range_dmg(army2,army1)
        result1=pay(dmg1,army2,dead_army1)
        result2=pay(dmg2,army1,dead_army2)
        if result1:
            return 1
        if result2:
            return 2

