class Atirador:

    def __init__(self, name):
        self.name = name
        self.vida = 5
        self.status = "V"

    def atira(self, target):
        target.vida -= 1
        return target.vida
