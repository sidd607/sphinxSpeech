from autobahn.twisted.websocket import WebSocketServerProtocol, WebSocketServerFactory

class MyServerProtocol(WebSocketServerProtocol):

    def onConnect(self, request):
        print('Client Connecting: {0}', format(request.peer))

    def onOpen(self):
        print "WebSocket Connection Open"

    def onMessage(self, payload, isBinary):
        if isBinary:
            with open('data/recording.raw', 'ab') as f:
                f.write(payload)
            print("Binary Message Recieved: {0}", format(len(payload)))

        else:
            print("Text Message: {0}", format(payload.decode('utf8')))

        self.sendMessage(payload, isBinary)

    def onClose(self, wasClean, code, reason):
        print "Connection Closed"



if __name__ == "__main__":
    import sys

    from twisted.python import log
    from twisted.internet import reactor

    log.startLogging(sys.stdout)

    factory = WebSocketServerFactory(u"ws://127.0.0.1:9000")
    factory.protocol = MyServerProtocol

    reactor.listenTCP(9000, factory)
    reactor.run()
