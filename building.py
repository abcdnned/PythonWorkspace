building_list=('wall','capfire','shelter','storehouse','workshop','hunter hall','weaponry','smithy','barrack')

class order(object):
    def __init__(self,item,number):
        self.item=item
        self.number=number

class building(object):
    def __init__(self,name,cata,maxhp):
        self.name=name
        self.cata=cata
        self.lv=1
        self.maxhp=maxhp
        self.hp=maxhp
        self.orders=[]

    def upgrade(self):
        self.lv+=1

    def produce(self):
        pass

    def order(self,order):
        self.orders.append(order)

class Wall(building):
    def __init__(self):
        super(Wall,self).__init__('wall',BUILDING_BARRIR,500)

    def upgrade(self):
        self.lv+=1
        self.maxhp+=200
        self.hp=self.maxhp


