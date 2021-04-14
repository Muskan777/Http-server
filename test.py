import requests
from threading import *
import sys
from socket import *
import os, stat

myobj = {'somekey': 'somevalue'}
filecontent = "Hello"
maxfilecontent = "The most viewed pages of Wikipedia before 2007 remain unknown, though the multiyear ranking of most viewed pages gives views for top 100 pages since 2007The most viewed pages of Wikipedia before 2007 remain unknown, though the multiyear ranking of most viewed pages gives views for top 100 pages since 2007The most viewed pages of Wikipedia before 2007 remain unknown, though the multiyear ranking of most viewed pages gives views for top 100 pages since 2007The most viewed pages of Wikipedia before 2007 remain unknown, though the multiyear ranking of most viewed pages gives views for top 100 pages since 2007The most viewed pages of Wikipedia before 2007 remain unknown, though the multiyear ranking of most viewed pages gives views for top 100 pages since 2007The most viewed pages of Wikipedia before 2007 remain unknown, though the multiyear ranking of most viewed pages gives views for top 100 pages since 2007The most viewed pages of Wikipedia before 2007 remain unknown, though the multiyear ranking of most viewed pages gives views for top 100 pages since 2007The most viewed pages of Wikipedia before 2007 remain unknown, though the multiyear ranking of most viewed pages gives views for top 100 pages since 2007"
port = sys.argv[1]
serverName = '127.0.0.1'
serverPort = int(sys.argv[1])

def gethead():
    i = 0
    while i <=10:
        requests.get("http://localhost:" + port + "/form.html")
        i += 1
    j = 0
    while j <=10:
        requests.head("http://localhost:" + port + "/form.html")
        j += 1

def putdel():
    i = 0
    while i <= 10:
        requests.put("http://localhost:" + port + "/newfile.txt", data=filecontent)
        i += 1
    j = 0
    while j <= 10:
        requests.delete("http://localhost:" + port + "/newfile.txt")
        j += 1

def stage1():
    requests.get("http://127.0.0.1:" + port + "/index.html")
    requests.head("http://127.0.0.1:" + port + "/index.html")
    requests.put("http://127.0.0.1:" + port + "/newfile.txt", data=filecontent)
    requests.delete("http://127.0.0.1:" + port + "/newfile.txt")
    requests.post("http://127.0.0.1:" + port + "/form.html", data = myobj)
    gethead()

def stage2():
    #GET status codes
    #200
    a = requests.get("http://127.0.0.1:" + port + "/index.html")
    #304
    a = requests.get("http://127.0.0.1:" + port + "/index.html", headers = {'If-Modified-Since': 'Wed 4 Nov 2020 08:48:00 GMT'})
    #400
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName,serverPort))
    data = ""
    data += "GET /index.html HtTP/1.0\r\nContent-Type: text/plain\r\nAccept: /\r\nHost: 127.0.0.1:12000\r\nAccept-Encoding: gzip, deflate, br\r\nConnection: keep-alive\r\nContent-Length: 13\r\nCookie: yummy_cookie=choco\r\nUser-Agent: My testing file\r\n\r\n"
    clientSocket.send(data.encode())
    modifiedSentence = clientSocket.recv(10000)
    clientSocket.close()
    #403
    os.chmod('forbidden.html', stat.S_IWUSR | stat.S_IWGRP | stat.S_IWOTH)
    a = requests.get("http://127.0.0.1:" + port + "/forbidden.html")
    #404
    a = requests.get("http://127.0.0.1:" + port + "/fdjgk.html")
    #414
    requests.get("http://127.0.0.1:" + port + "/fdsajlfjdfjhajkhfkjdahfjkahjfkdhakjfdhkajhfjkahfdjhakjfhajdfjkajkfdhakjfasfasjfdsjfalfdjaofklfajldsdfjalkjlaksjflkasjfjalfjsjfsakjfdsdjflkasjdfljskdfjlsadfjlsdakjflksdajfldsajflkdjsafljsalfjalfjalkfjlasjfldsjaflkjsdlfkjklrajfdifarennrelajlktjwtljrltjlrejltjlrejtlrjtlkwaijrf4lrgljreltjlrtjdfjlkjf.html")
    #415
    requests.get("http://127.0.0.1:" + port + "/index.asd")

    #POST Status codes
    #200
    requests.post("http://127.0.0.1:" + port + "/form.html", data = myobj)
    #400
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName,serverPort))
    data = ""
    data += "POST /index.html HtTP/1.1\r\nContent-Type: text/plain\r\nAccept: /\r\nHost: 127.0.0.1:12000\r\nAccept-Encoding: gzip, deflate, br\r\nConnection: keep-alive\r\nContent-Length: 13\r\nCookie: yummy_cookie=choco\r\nUser-Agent: My testing file\r\n\r\n"
    clientSocket.send(data.encode())
    modifiedSentence = clientSocket.recv(10000)
    clientSocket.close()
    #404
    requests.post("http://127.0.0.1:" + port + "/form2.html", data = myobj)
    #413
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName,serverPort))
    data = ""
    data += "POST /form.html HTTP/1.1\r\nContent-Type: text/html\r\nAccept: /\r\nHost: 127.0.0.1:12000\r\nAccept-Encoding: gzip, deflate, br\r\nConnection: keep-alive\r\nContent-Type: text/html\r\nCookie: yummy_cookie=choco\r\nUser-Agent: My testing file\r\n\r\nThe most viewed pages of Wikipedia before 2007 remain unknown, though the multiyear ranking of most viewed pages gives views for top 100 pages since 2007The most viewed pages of Wikipedia before 2007 remain unknown, though the multiyear ranking of most viewed pages gives views for top 100 pages since 2007The most viewed pages of Wikipedia before 2007 remain unknown, though the multiyear ranking of most viewed pages gives views for top 100 pages since 2007The most viewed pages of Wikipedia before 2007 remain unknown, though the multiyear ranking of most viewed pages gives views for top 100 pages since 2007The most viewed pages of Wikipedia before 2007 remain unknown, though the multiyear ranking of most viewed pages gives views for top 100 pages since 2007The most viewed pages of Wikipedia before 2007 remain unknown, though the multiyear ranking of most viewed pages gives views for top 100 pages since 2007The most viewed pages of Wikipedia before 2007 remain unknown, though the multiyear ranking of most viewed pages gives views for top 100 pages since 2007The most viewed pages of Wikipedia before 2007 remain unknown, though the multiyear ranking of most viewed pages gives views for top 100 pages since 2007\r\n"
    clientSocket.send(data.encode())
    modifiedSentence = clientSocket.recv(10000)
    clientSocket.close()

    #HEAD Status codes
    #200
    requests.head("http://127.0.0.1:" + port + "/index.html")
    #400
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName,serverPort))
    data = ""
    data += "HEAD /index.html HtTP/1.1\r\nContent-Type: text/plain\r\nAccept: /\r\nHost: 127.0.0.1:12000\r\nAccept-Encoding: gzip, deflate, br\r\nConnection: keep-alive\r\nContent-Length: 13\r\nCookie: yummy_cookie=choco\r\nUser-Agent: My testing file\r\n\r\n"
    clientSocket.send(data.encode())
    modifiedSentence = clientSocket.recv(10000)
    clientSocket.close()
    #304
    requests.head("http://127.0.0.1:" + port + "/index.html", headers = {'If-Modified-Since': 'Wed 4 Nov 2020 08:48:00 GMT'})
    #404
    requests.head("http://127.0.0.1:" + port + "/form2.html")
    #414
    requests.head("http://127.0.0.1:" + port + "/fdsajlfjdfjhajkhfkjdahfjkahjfkdhakjfdhkajhfjkahfdjhakjfhajdfjkajkfdhakjfasfasjfdsjfalfdjaofklfajldsdfjalkjlaksjflkasjfjalfjsjfsakjfdsdjflkasjdfljskdfjlsadfjlsdakjflksdajfldsajflkdjsafljsalfjalfjalkfjlasjfldsjaflkjsdlfkjklrajfdifarennrelajlktjwtljrltjlrejltjlrejtlrjtlkwaijrf4lrgljreltjlrtjdfjlkjf.html")
    #415
    requests.head("http://127.0.0.1:" + port + "/index.asd")


    #PUT Status Codes
    #201
    requests.put("http://127.0.0.1:" + port + "/newfile.txt", data=filecontent)
    #200
    requests.put("http://127.0.0.1:" + port + "/newfile.txt", data=filecontent)
    #204
    requests.put("http://127.0.0.1:" + port + "/newfile.txt", data='')
    #400
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName,serverPort))
    data = ""
    data += "PUT /index.html HtTP/1.1\r\nContent-Type: text/plain\r\nAccept: /\r\nHost: 127.0.0.1:12000\r\nAccept-Encoding: gzip, deflate, br\r\nConnection: keep-alive\r\nContent-Length: 13\r\nCookie: yummy_cookie=choco\r\nUser-Agent: My testing file\r\n\r\n"
    clientSocket.send(data.encode())
    modifiedSentence = clientSocket.recv(10000)
    clientSocket.close()
    #403
    requests.put("http://127.0.0.1:" + port + "/writenot.html", data=filecontent)
    #413
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName,serverPort))
    data = ""
    data += "PUT /newfile.txt HTTP/1.1\r\nContent-Type: text/plain\r\nAccept: /\r\nHost: 127.0.0.1:12000\r\nAccept-Encoding: gzip, deflate, br\r\nConnection: keep-alive\r\nContent-Type: text/html\r\nCookie: yummy_cookie=choco\r\nUser-Agent: My testing file\r\n\r\n"
    clientSocket.send(data.encode())
    modifiedSentence = clientSocket.recv(10000)
    clientSocket.close()
    #413
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName,serverPort))
    data = ""
    data += "PUT /newfile.txt HTTP/1.1\r\nContent-Type: text/plain\r\nAccept: /\r\nHost: 127.0.0.1:12000\r\nAccept-Encoding: gzip, deflate, br\r\nConnection: keep-alive\r\nContent-Type: text/html\r\nCookie: yummy_cookie=choco\r\nUser-Agent: My testing file\r\n\r\nThe most viewed pages of Wikipedia before 2007 remain unknown, though the multiyear ranking of most viewed pages gives views for top 100 pages since 2007The most viewed pages of Wikipedia before 2007 remain unknown, though the multiyear ranking of most viewed pages gives views for top 100 pages since 2007The most viewed pages of Wikipedia before 2007 remain unknown, though the multiyear ranking of most viewed pages gives views for top 100 pages since 2007The most viewed pages of Wikipedia before 2007 remain unknown, though the multiyear ranking of most viewed pages gives views for top 100 pages since 2007The most viewed pages of Wikipedia before 2007 remain unknown, though the multiyear ranking of most viewed pages gives views for top 100 pages since 2007The most viewed pages of Wikipedia before 2007 remain unknown, though the multiyear ranking of most viewed pages gives views for top 100 pages since 2007The most viewed pages of Wikipedia before 2007 remain unknown, though the multiyear ranking of most viewed pages gives views for top 100 pages since 2007The most viewed pages of Wikipedia before 2007 remain unknown, though the multiyear ranking of most viewed pages gives views for top 100 pages since 2007\r\n"
    clientSocket.send(data.encode())
    modifiedSentence = clientSocket.recv(10000)
    clientSocket.close()
    #414
    requests.put("http://127.0.0.1:" + port + "/fdsajlfjdfjhajkhfkjdahfjkahjfkdhakjfdhkajhfjkahfdjhakjfhajdfjkajkfdhakjfasfasjfdsjfalfdjaofklfajldsdfjalkjlaksjflkasjfjalfjsjfsakjfdsdjflkasjdfljskdfjlsadfjlsdakjflksdajfldsajflkdjsafljsalfjalfjalkfjlasjfldsjaflkjsdlfkjklrajfdifarennrelajlktjwtljrltjlrejltjlrejtlrjtlkwaijrf4lrgljreltjlrtjdfjlkjf.html", data = filecontent)
    #415
    requests.put("http://127.0.0.1:" + port + "/index.asd", data = filecontent)

    #DELETE Status Codes
    #200
    requests.delete("http://127.0.0.1:" + port + "/newfile.txt")
    #204
    requests.delete("http://127.0.0.1:" + port + "/temp.txt")
    #400
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName,serverPort))
    data = ""
    data += "DELETE /index.html HtTP/1.1\r\nContent-Type: text/plain\r\nAccept: /\r\nHost: 127.0.0.1:12000\r\nAccept-Encoding: gzip, deflate, br\r\nConnection: keep-alive\r\nContent-Length: 13\r\nCookie: yummy_cookie=choco\r\nUser-Agent: My testing file\r\n\r\n"
    clientSocket.send(data.encode())
    modifiedSentence = clientSocket.recv(10000)
    clientSocket.close()
    #404
    requests.delete("http://127.0.0.1:" + port + "/fdk.txt")
    putdel()
    stage1()


    #Other status
    #501
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName,serverPort))
    data = ""
    data += "GETT /index.html HTTP/1.1\r\nContent-Type: text/plain\r\nAccept: /\r\nHost: 127.0.0.1:12000\r\nAccept-Encoding: gzip, deflate, br\r\nConnection: keep-alive\r\nContent-Length: 13\r\nCookie: yummy_cookie=choco\r\nUser-Agent: My testing file\r\n\r\n"
    clientSocket.send(data.encode())
    modifiedSentence = clientSocket.recv(10000)
    clientSocket.close()

    
def stage3():
    for i in range(40):
        t1 = Thread(target = requests.get, args = ("http://127.0.0.1:" + port + "/index.html", ))
        t1.start()
        t3 = Thread(target = stage2)
        t3.start()
        t3.join()
        t1.join()

stage3()
    