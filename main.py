from atirador import Atirador
from random import randint



def getPlayers():
    while True:
        print("Digite o número de jogadores")
        players = input()
        if int(players) > 10:
            print("Número Máximo de jogadores deve ser 10")
        elif int(players) < 2:
            print("Mínimo de 2 jogadores")
        else:
            return int(players)



class Main:
    def __init__(self):
        self.gameEnd = False
        self.nameList = ["Pelé", "Batoré", "Caboré", "Jaspion", "Jiraya", "Jiban", "Samurai", "Oitaviano", "Nhonho", "Dexter"]
        self.listPlayers = []
        self.p = getPlayers()
        self.count = 0
        self.previous = ' '

    def getTurn(self):
        shooter = self.listPlayers[randint(0, len(self.listPlayers) - 1)]
        taker = self.listPlayers[randint(0, len(self.listPlayers) - 1)]
        while shooter.name == taker.name:
            taker = self.listPlayers[randint(0, len(self.listPlayers) - 1)]
        return shooter, taker

    def loop(self):
        for i in range(0, self.p):
            self.listPlayers.append(Atirador(self.nameList.pop(randint(0, len(self.nameList) - 1))))
            print("Jogador " + self.listPlayers[i].name + " entrou na sala")
        while self.gameEnd is not True:
            if len(self.listPlayers) == 1:
                print(self.listPlayers[0].name + " ganhou o jogo")
                self.gameEnd = True
            shooter, taker = self.getTurn()
            while self.previous == shooter.name:
                shooter, taker = self.getTurn()
            print(shooter.name + " atira em " + taker.name)
            turno = Atirador.atira(shooter, taker)
            print(taker.name + ' ' + str(turno))
            if taker.vida <= 0:
                print(taker.name + ' morreu')
                self.listPlayers.remove(taker)
            self.previous = shooter.name
m = Main()
m.loop()
