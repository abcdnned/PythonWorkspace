import gameshell


class SagaShell(gameshell.GameShell):

    def re(self):
        self.cache = ['line1', 'line2', 'line3']
        self.mod = 1
        self.render()

    def getTitle(self):
        return 'ClanSaga'

game = SagaShell()
game.start()
game.re()
