import SimpleHTTPServer
import SocketServer
import config

class theHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = "firstpage.html"
        return SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

objHandler = theHandler

print("LISTEN on %s => %d" % (config.HOST,config.PORT))

webServer =  SocketServer.TCPServer((config.HOST,config.PORT), theHandler)

try:
    webServer.serve_forever()
except KeyboardInterrupt:
    pass

webServer.server_close()
print("Server stopped.")

