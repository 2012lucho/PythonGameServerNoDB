from player   import Player;
from game_msg import GameMSG;

class Game():
    def __init__(self):
        self.players      = []
        self.factory      = ''
        self.player_count = 0

    def dataReceived(self, data):
        print(data)

    def setFactory(self, factory):
        self.factory = factory

    def sendMessage(self, message):
        for client in self.factory.clients:
            client.transport.write(message)

    def newClient(self, client):
        self.player_count += 1
        player = Player(self.player_count, client)
        self.players.append(player)
        self.factory.clients.add(client)

        msg = GameMSG()
        msg.data = { "id":player.id }
        self.sendMessage( str(msg.getMsg()) )

    def connectionLost(self, client):
        self.factory.clients.remove(client)
