import pygame

SCREEN_SIZE = (1000, 630)
PAGE_SIZE =31 
MAX_SIZE = 2000
CLEAN_SIZE = 500
FONT_HEIGHT = 16
LMARGIN=10
TITLESTART=5
TOPMARGIN=35
BOTTON_LINE=500
PADDING=5

LASTCMD_CAP=9

LINE_CAP=100

black=(0,0,0)
grey=(200,200,200)

leader='>'

class GameShell(object):

    def __init__(self):
        pygame.init()
        self.lines = []
        self.lastcmd=[]
        self.title=''
        self.cmdc=0
        self.cmdsize=0
        self.cursor = 0
        self.ll=''
        self.c2 = 0
        self.mod=0
        self.cache = []
        self.font =pygame.font.SysFont("monospace", 15,True,False) 
        self.screen = None
        self.foot=[]

    def render(self):
        self.screen.fill(black)
        y=TOPMARGIN
        FONT_HEIGHT=self.font.get_linesize()
        BOTTON_LINE=TOPMARGIN+FONT_HEIGHT*PAGE_SIZE+PADDING
        i=0
        if self.mod==0 or self.mod==2:
            self.screen.blit(self.font.render(self.title,True,grey),(LMARGIN,TITLESTART))
        maxfoot=max(10,len(self.foot))
        while y<=600:
            if self.mod==0 or self.mod==2:
                if self.cursor+i < min(self.cursor+PAGE_SIZE-maxfoot,len(self.lines)):
                    self.screen.blit(self.font.render(self.lines[self.cursor+i],True,grey),(LMARGIN,y))
                else:
                    break
            elif self.mod==1:
                if self.c2+i < min(PAGE_SIZE-maxfoot,len(self.cache)):
                    self.screen.blit(self.font.render(self.cache[self.c2+i],True,grey),(LMARGIN,y))
                else:
                    break
            y+=FONT_HEIGHT
            i+=1

        y=TOPMARGIN+FONT_HEIGHT*(PAGE_SIZE-len(self.foot))
        for i in range(0,len(self.foot)):
            self.screen.blit(self.font.render(self.foot[i],True,grey),(LMARGIN,y))
            y+=FONT_HEIGHT
        self.screen.blit(self.font.render(self.ll,True,grey),(LMARGIN,BOTTON_LINE))
        pygame.display.update()


    def getTitle(self):
        return 'GameShell'

    def interact(self,event):
        pass

    def command(self,cmd):
        pass

    def prepare(self):
        pass

    def addline(self,line):
        for l in line.split('\n'):
            if len(l) > LINE_CAP:
                for i in range(0,len(l)/LINE_CAP):
                    self.lines.append(l[i*LINE_CAP:(i+1)*LINE_CAP if i<len(l)-1 else l[i*LINE_CAP:]])
            else:
                self.lines.append(line)
        if len(self.lines)-self.cursor<PAGE_SIZE:
            self.cursor+=1

    def start(self):
        self.screen=pygame.display.set_mode(SCREEN_SIZE)
        pygame.display.set_caption(self.getTitle())
        self.render()
        
        self.prepare()

        game_exit=False
        while not game_exit:
            event=pygame.event.poll()
            if event.type==pygame.QUIT:
                game_exit=True
            elif event.type==pygame.KEYDOWN:
                if self.mod==0:
                    if event.key==pygame.K_DOWN: 
                        self.cursor=min(self.cursor+1,len(self.lines)-PAGE_SIZE)
                        self.render()
                    elif event.key==pygame.K_UP:
                        self.cursor=max(self.cursor-1,0)
                        self.render()
                    elif event.key==pygame.K_PAGEDOWN:
                        self.cursor=min(self.cursor+PAGE_SIZE-1,len(self.lines)-PAGE_SIZE)
                        self.render()
                    elif event.key==pygame.K_PAGEUP:
                        self.cursor=max(self.cursor-PAGE_SIZE-1,0)
                        self.render()
                    elif event.key==pygame.K_RETURN:
                        self.mod=2
                        self.ll=leader
                        self.render()
                    elif event.key==pygame.K_END:
                        self.cursor=len(self.lines)-PAGE_SIZE
                        self.render()
                    elif event.key==pygame.K_HOME:
                        self.cursor=0
                        self.render()
                elif self.mod==2:
                    if event.key==pygame.K_RETURN:
                        if len(self.ll) > 1:
                            self.lastcmd.insert(0,self.ll[1:])
                            if self.cmdsize==LASTCMD_CAP:
                                self.lastcmd=self.lastcmd[:-1]
                            else:
                                self.cmdsize+=1
                            self.command(self.ll[1:])
                        self.ll=''
                        self.cmdc=-1
                        self.mod=0
                        self.render()
                    elif event.key==pygame.K_ESCAPE:
                        self.ll=''
                        self.cmdc=-1
                        self.mod=0
                        self.render()
                    elif event.key==pygame.K_DOWN:
                        self.cmdc-=1
                        if self.cmdc<0:
                            self.cmdc=self.cmdsize-1
                        self.ll=leader+self.lastcmd[self.cmdc]
                        self.render()
                    elif event.key==pygame.K_UP:
                        self.cmdc=(self.cmdc+1)%self.cmdsize
                        self.ll=leader+self.lastcmd[self.cmdc]
                        self.render()
                    else:
                        if event.key==pygame.K_BACKSPACE: 
                            if len(self.ll)>1:
                                self.ll=self.ll[:-1]
                        else:
                            self.ll=self.ll+event.unicode
                        self.render()

            self.interact(event)


        pygame.quit()

