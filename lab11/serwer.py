#!/usr/bin/env python3
# -*- coding:utf8 -*-
from http.server import BaseHTTPRequestHandler, HTTPServer
import sys
import getopt


def main():
    hostName = ""
    serverPort = 9000
    plik = "index.html"
    folder = "."
    opts, args = getopt.getopt(sys.argv[1:], "i:d:p:a:h", [])
    for o, a in opts:
        if o in ("-i"):
            plik = a
        elif o in ("-d"):
            folder = a
        elif o in ("-p"):
            try:
                a = int(a)
                serverPort = a
            except ValueError:
                print("Podany port nie jest liczbą.")
                exit()
        elif o in ("-a"):
            hostName = a
        elif o in ("-h"):
            print("-i dla podania nazwy pliku, -d dla podania katalogu, -p dla ustawienia portu, -a dla ustawienia adresu")

    class MyServer(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            plikotw = open("{}/{}".format(folder, plik), "r")
            for line in plikotw:
                self.wfile.write(bytes(line, "utf-8"))
            plikotw.close()
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")


if __name__ == "__main__":
    main()

