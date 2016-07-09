from thing import *
from item import *
from task import *

class worker(thing):
    def __init__(self,name,promote_con,origin,taskli):
        super(worker,self).__init__(THING_WORKER)
        self.name=name
        self.origin=origin

idle=worker('worker',dict(),None,[])
farmer=worker('farmer',{seed:1},idle,[farm])
hunter=worker('hunter',{bow:1},idle,[hunt,snipe])
miner=worker('miner',{pickaxe:1},idle,[mine])
lumber=worker('lumber',{axe:1},idle,[chop])
smith=worker('smith',{hammer:1,anvil:1},idle,[forge])
builder=worker('builder',dict(hammer=1,saw=1),idle,[build,repair])

worker_type=('worker','farmer','hunter','miner','lumber','smith','builder')

