from player   import Player;
from game_msg import GameMSG;

class Game():
    def __init__(self):
        self.players = []
        self.factory = ''

    def dataReceived(self, data):
        print(data)

    def setFactory(self, factory):
        self.factory = factory

    def sendMessage(self, message):
        for client in self.factory.clients:
            client.transport.write(message)

    def newClient(self, client):
        self.factory.clients.add(self)

    def connectionLost(self, client):
        self.factory.clients.remove(self)
