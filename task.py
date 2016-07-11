from worker import *

TASK_TYPE=('idle','snipe','mine','chop','farm','hunt','forge','build','repair')

#product type
PRO=0

#log type
LOG=0
WARN=1

TASKS=[]

class archive(object):
    def __init__(self):
        self.log=[]
        self.product=[]


    def addlog(self,loglv,content):
        self.log.append([loglv,content])

    def addproduct(self,product_type,product,number):
        self.product.append([pridcut_type,product,number])

class task(object):

    def __init__(self,name):
        self.name=name
        self.members={}

    ori=task('donothing')
    
    @staticmethod
    def of(arg):
        return ori

    def assign(self,man,num):
        self.members[man]=self.members[man]+num if man in self.members else num

    def proceed(self):
        pass

class mine(task):
    def proceed(self,*arg):
        pro=archive()
        if arg[0]=='stone':
            stone_num=self.members[miner]*10 if miner in self.members else 0
            pro.addproduct(PRO,stone,stone_num)
        elif arg[0]=='iron':
            iron_num=self.members[miner]*4 if miner in self.members else 0
            pro.addproduct(PRO,iron,iron_num)
        elif arg[0]=='silver':
            silver_num=self.members[miner]*1 if miner in self.memebers else 0
            pro.addproduct(PRO,silver,silver_num)
        return pro

class chop(task):
    def proceed(self,*arg):
        wood_sum=0
        wood_sum+=self.members[lumber]*5 if lumber in self.members else 0
        pro=archive()
        pro.addprodcut(PRO,wood,wood_sum)
        return pro

class farm(task):
    def proceed(self,*arg):
        food_sum=0
        food_sum+=self.members[farmer]*5 if farmer in self.members else 0
        pro=archive()
        pro.addproduct(PRO,food,food_sum)
        return pro

idle=task('idle')
farm=task('farm')
chop=task('chop')
mine=task('mine')
forge=task('forge')
build=task('build')
repair=task('repair')
hunt=task('hunt')
snipe=task('snipe')


    
