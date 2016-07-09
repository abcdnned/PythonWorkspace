from thing import *

class item(thing):
    def __init__(self,name):
        super(item,self).__init__(THING_ITEM)
        self.name=name

wood=item('wood')
meat=item('mead')
gold=item('glod')
iron=item('iron')
silver=item('silver')
seed=item('seed')
axe=item('axe')
pickaxe=item('pickaxe')
bow=item('bow')
hammer=item('hammer')
anvil=item('anvil')
saw=item('saw')
chisel=item('chisel')
stone=item('stone')
