#!/usr/bin/env python3
# -*- coding:utf8 -*-
from http.server import BaseHTTPRequestHandler, HTTPServer
import sys
import getopt
import os
from urllib.parse import urlparse


def main():
    hostName = ""
    serverPort = 9000
    plik = "index.html"
    folder = os.getcwd()  # + "/"
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

    #os.chroot(folder) os.chroot() nie działał na moim komputerze

    class MyServer(BaseHTTPRequestHandler):
        def do_GET(self):
            sciezka = urlparse(self.path).path
            #zabezpieczyć ścieżkę
            # if os.access("/{}".format(sciezka), os.R_OK):
            if os.access("{}/{}".format(folder, sciezka), os.R_OK):
                self.send_response(200)
                if sciezka[-4:] == ".txt":
                    self.send_header("Content-type", "text/plain")
                elif sciezka[-4:] == ".pdf":
                    self.send_header("Content-type", "application/pdf")
                else:
                    self.send_header("Content-type", "text/html")
                self.end_headers()
                # os.chroot()
                czyJestPlikiem = True
                sciezka = "{}{}".format(folder, sciezka)
                pomocfolderwyzej = list(os.scandir("/".join(sciezka.split("/")[:-1])))
                for x in pomocfolderwyzej:
                    if x.name == sciezka.split("/")[-1]:
                        if x.is_dir():
                            czyJestPlikiem = False
                        else:
                            czyJestPlikiem = True
                if sciezka[:-1] == folder:
                    czyJestPlikiem = False
                if czyJestPlikiem:
                    plikotw = open(sciezka, "rb")
                    self.wfile.write(plikotw.read())
                    plikotw.close()
                else:
                    self.wfile.write(bytes("<html><body>", "utf-8"))
                    for x in list(os.scandir(sciezka)):
                        self.wfile.write(bytes("<p><a href=\"{}\">{}</a>    {}  {}</p>".format(x.name, x.name, x.stat().st_mtime, x.stat().st_size), "utf-8"))
                    self.wfile.write(bytes("</body></html>", "utf-8"))
            else:
                self.send_error(404)
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

