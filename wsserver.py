#!/usr/bin/env python
# -*- coding: utf-8 -*-

from twisted.internet import protocol, reactor, endpoints
from txws import WebSocketFactory
from game import Game

game = Game()

class ClientProtocol(protocol.Protocol):

    def __init__(self, factory):
        self.factory = factory
        game.setFactory(self.factory)

    def dataReceived(self, data):
        game.dataReceived(data)

    def connectionLost(self, reason):
        game.connectionLost(self)

    def connectionMade(self):
        game.newClient(self)


class ClientFactory(protocol.Factory):

    def __init__(self):
        self.clients = set()

    def buildProtocol(self, addr):
        return ClientProtocol(self)

endpoints.serverFromString(reactor, "tcp:9998").listen(
    WebSocketFactory(ClientFactory()))
reactor.run()
