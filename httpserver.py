from socket import *
import os, time
import sys
import datetime
from config import *
from threading import * 
import threading

serverPort = int(sys.argv[1])
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
headers = {}
byte=None
postdata=None
resp=None
file_extension = {'.html':'text/html', '.txt':'text/plain', '.png':'image/png', '.gif': 'image/gif', '.jpg':'image/jpg', '.ico': 'image/x-icon', '.php':'application/x-www-form-urlencoded', '': 'text/plain', '.jpeg':'image/jpeg', '.pdf': 'application/pdf', '.js': 'application/javascript', '.css': 'text/css', '.mp3' : 'audio/mpeg', '.mp4': 'video/mp4'}
mode = {'.html':'r', '.txt':'r', '.png':'rb', '.gif': 'rb', '.jpg':'rb', '.ico': 'rb', '.php':'r', '': 'r', '.jpeg':'rb', '.pdf': 'r', '.js': 'r', '.css': 'r', '.mp3' : 'rb', '.mp4': 'rb'}
number_of_connections = 0

def checkdate(dategiven, filename):
    a = datetime.datetime.strptime(dategiven, "%a %d %b %Y %H:%M:%S %Z")
    b = datetime.datetime.fromtimestamp(os.path.getmtime(filename))
    if a > b:
        return True
    return False

def compareDate():
    id = headers["Cookie"].split("=")[0]
    expiry = sent_cookies[id]
    DateTime = datetime.datetime.now()
    currDate += DateTime.strftime("%a, %d %B %Y %I:%M:%S")
    if expiry > currDate:
        return False
    return True

def status200(reqli):
    extension = "." + (reqli[0][1][1:].split("."))[1]
    if len(reqli[0][1][1:]) >= Maxuri:
        return status414()
    try:
        if extension not in file_extension.keys():
            return status415()
    except:
        pass
    if reqli[0][0] == "GET":
        if os.path.isfile(reqli[0][1][1:]):
            perm = os.access(reqli[0][1][1:], os.R_OK)
            if not perm:
                return status403()
    try:
        if reqli[0][0] == "GET" or reqli[0][0] == "POST":
            f = open(reqli[0][1][1:], mode[extension])
            if mode[extension] == "rb":
                global byte
                byte = f.read()
            filecontent = f.read()
            f.close()
        if reqli[0][0] == "PUT":
            filecontent = '<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">\n<html><head>\n<title>200 OK</title>\n</head><body>\n<h1>OK</h1>\n<p>The File was Modified.</p>\n<hr>\n<address>HTTP Server at 127.0.0.1 Port '+ str(serverPort) +' </address>\n</body></html>'
            f = open(reqli[0][1][1:], 'w')
            f.write(body)
            f.close()
        if reqli[0][0] == "DELETE":
            filecontent = '<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">\n<html><head>\n<title>200 OK</title>\n</head><body>\n<h1>OK</h1>\n<p>The File was Deleted.</p>\n<hr>\n<address>HTTP Server at 127.0.0.1 Port '+ str(serverPort) +' </address>\n</body></html>'

    except Exception as e:
        if (reqli[0][1][1:] == oldaddr_301):
            return status301()
        else:
            return status404()
    try:
        if headers['If-Modified-Since'] and checkdate(headers['If-Modified-Since'], reqli[0][1][1:]):
            return status304()
        else:
            raise Exception()
    except:
        statuscode = '200'
        statusresponse = "OK"
        if mode[extension]:
            content = "Content-Length: " + str(os.path.getsize(reqli[0][1][1:]))
        contenttype = "Content-Type: " + file_extension[extension]

        resp = ""
        if len(reqli[0]) != 2:
            resp = "HTTP/1.1 " + statuscode + " " + statusresponse + "\n"
            resp += "Date: " + str(datetime.datetime.now(datetime.timezone.utc).strftime("%a, %d %b %Y %H:%M:%S GMT")) + "\n"
            resp = resp + "Server: HTTP Server\n"
            resp += "Last-Modified: Thu, 8 Oct 2020 20:56:29 GMT\n"
            resp += 'ETag: "5e-5b167522a27aa"\n'
            resp += "Accept-Ranges: bytes\n"
            resp += content + "\n"
            try:
                if not headers["Cookie"]:
                    if compareDate():
                        pass
                    else:
                        resp += SetCookie() + "\n"           
            except:
                resp += SetCookie() + "\n"
            resp += "Vary: Accept-Encoding\n"
            resp += contenttype + "\n"
            resp += "Vary: Accept-Encoding\n"
            resp += contenttype + "\n\n"
            

        if reqli[0][0] != "HEAD" and mode[extension]!="rb":
            resp = resp + filecontent + "\n"
        return resp
    



def status201(reqli):
    f = open(reqli[0][1][1:], "w")
    f.write(body)
    f.close()
    filecontent = '<html>\n<body>\n<h1>The file was created.</h1>\n</body>\n</html>'
    resp = ''
    resp += 'HTTP/1.1 201 Created\n'
    resp += "Date "+ str(datetime.datetime.now(datetime.timezone.utc).strftime("%a, %d %b %Y %H:%M:%S GMT")) + "\n"
    resp = resp + "Server: HTTP Server\n"
    resp += "Content-Length: " + str(len(filecontent)) + "\n"
    resp += "Content-Type: text/html; charset=iso-8859-1\n"
    resp += "Connection: Closed\n\n"
    resp += filecontent + "\n"
    return resp

def status204():
    f = open(reqli[0][1][1:], 'w')
    f.write(body)
    f.close()
    filecontent = '<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">\n<html><head>\n<title>204 No Content</title>\n</head><body>\n<h1>No Content</h1>\n<p>Content is required</p>\n<hr>\n<address>HTTP Server at 127.0.0.1 Port '+ str(serverPort) +' </address>\n</body></html>'
    resp = ''
    resp += "HTTP/1.1 204 No Content\n"
    resp += "Date "+ str(datetime.datetime.now(datetime.timezone.utc).strftime("%a, %d %b %Y %H:%M:%S GMT")) + "\n"
    resp += "Content-Length: " + str(len(filecontent)) + "\n"
    resp += "Content-Type: text/html; charset=iso-8859-1\n"
    resp += "Connection: Close\n\n"
    resp += filecontent + "\n"
    return resp   

def status301():
    filecontent = '<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">\n<html><head>\n<title>301 Moved Permanently</title>\n</head><body>\n<h1>Moved Permanently</h1>\n<p>The document has moved <a href="http://127.0.0.1:' + str(serverPort)+'/' + str(newaddr_301) + '">here</a>.</p>\n<hr>\n<address>HTTP Server at 127.0.0.1 Port ' +str(serverPort) +'</address>\n</body></html>'
    resp = ""
    resp +="HTTP/1.1 301 Moved Permanently\n"
    resp += "Date: " + str(datetime.datetime.now(datetime.timezone.utc).strftime("%a, %d %b %Y %H:%M:%S GMT")) + "\n"
    resp += "Server: HTTP Server\n"
    resp += "Content-Length: " + str(len(filecontent)) + "\n"
    resp += "Connection: close\n"
    resp += "Location: " + "http://127.0.0.1:" + str(serverPort)+ "/" + str(newaddr_301) + "\n"
    resp += "Content-Type: text/html; charset=iso-8859-1\n\n"
    if reqli[0][0] != "HEAD":
        resp += filecontent + "\n"
    return resp



def status304():
    resp = ""
    resp += "HTTP/1.1 304 Not Modified\n"
    resp += "Date: " + str(datetime.datetime.now(datetime.timezone.utc).strftime("%a, %d %b %Y %H:%M:%S GMT")) + "\n"
    resp += "Server: HTTP Server\n\n"
    return resp

def status400():
    filecontent = '<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">\n<html><head>\n<title>400 Bad Request</title>\n</head><body>\n<h1>Bad Request</h1>\n<p>Your browser sent a request that this server could not understand.<br />\n</p>\n<hr>\n<address>HTTP Server Server at 10.42.0.1 Port ' + str(serverPort) +'</address>\n</body></html>'
    resp = ''
    resp = resp + "HTTP/1.1 400 Bad Request\n"
    resp += "Date "+ str(datetime.datetime.now(datetime.timezone.utc).strftime("%a, %d %b %Y %H:%M:%S GMT")) + "\n"
    resp += "Content-Length: " + str(len(filecontent)) + "\n"
    resp += "Connection: close\n"
    resp += "Content-Type: text/html; charset=iso-8859-1\n\n"
    if reqli[0][0] != "HEAD":
        resp += filecontent + "\n"
    return resp

def status403():
    filecontent = '<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">\n<html><head>\n<title>403 Forbidden</title>\n</head><body>\n<h1>Forbidden</h1>\n<p>You dont have permission to access this resource.</p>\n<hr>\n<address>HTTP Server at 127.0.0.1 Port '+ str(serverPort) +'</address>\n</body></html>'
    resp = ""
    resp += "HTTP/1.1 403 Forbidden\n"
    resp += "Date: " + str(datetime.datetime.now(datetime.timezone.utc).strftime("%a, %d %b %Y %H:%M:%S GMT")) + "\n"
    resp += "Server: HTTP Server\n"
    resp += "Content-Length: " + str(len(filecontent)) + "\n"
    resp += "Content-Type: text/html; charset=iso-8859-1\n\n"
    if reqli[0][0] != "HEAD":
        resp += filecontent + "\n"
    return resp

def status404():
    filecontent = '<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">\n<html><head>\n<title>404 Not Found</title>\n</head><body>\n<h1>Not Found</h1>\n<p>The requested URL was not found on this server.</p>\n<hr>\n<address>HTTP Server at 127.0.0.1 Port '+ str(serverPort) +' </address>\n</body></html>'
    resp = ''
    resp += "HTTP/1.1 404 Not Found\n"
    resp += "Date "+ str(datetime.datetime.now(datetime.timezone.utc).strftime("%a, %d %b %Y %H:%M:%S GMT")) + "\n"
    resp += "Content-Length: " + str(len(filecontent)) + "\n"
    resp += "Content-Type: text/html; charset=iso-8859-1\n"
    resp += "Connection: Close\n\n"
    if reqli[0][0] != "HEAD":
        resp += filecontent + "\n"
    return resp

def status408():
    resp = ''
    filecontent = '<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">\n<html><head>\n<title>408 Request Timeout</title>\n</head><body>\n<h1>Request Timeout</h1>\n<p>Server timeout waiting for the HTTP request from the client.</p>\n<hr>\n<address>HTTP Server Server at 10.42.0.1 Port 80</address>\n</body></html>'
    resp += 'HTTP/1.1 408 Request Timeout\n'
    resp += "Date "+ str(datetime.datetime.now(datetime.timezone.utc).strftime("%a, %d %b %Y %H:%M:%S GMT")) + "\n"
    resp = resp + "Server: HTTP Server\n"
    resp += "Content-Length: " + str(len(filecontent)) + "\n"
    resp += "Content-Type: text/html; charset=iso-8859-1\n"
    resp += "Connection: Closed\n\n"
    resp += filecontent + "\n"
    return resp

def status411():
    filecontent = '<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">\n<html><head>\n<title>411 Length Required</title>\n</head><body>\n<h1>Length Required</h1>\n<p>Content-Length is required for Put request</p>\n<hr>\n<address>HTTP Server at 127.0.0.1 Port '+ str(serverPort) +' </address>\n</body></html>'
    resp = ''
    resp += "HTTP/1.1 411 Length Required\n"
    resp += "Date "+ str(datetime.datetime.now(datetime.timezone.utc).strftime("%a, %d %b %Y %H:%M:%S GMT")) + "\n"
    resp += "Content-Length: " + str(len(filecontent)) + "\n"
    resp += "Content-Type: text/html; charset=iso-8859-1\n"
    resp += "Connection: Close\n\n"
    resp += filecontent + "\n"
    return resp    

def status413():
    filecontent = '<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">\n<html>\n<head>\n<title>413 Payload Too Large</title>\n</head>\n<body>\n<h1>Payload Too Large</h1>\n<p>The requested File size is too Large</p>\n<hr>\n<address>HTTP Server at 127.0.0.1 Port '+ str(serverPort) +' </address>\n</body>\n</html>'
    resp = ''
    resp += "HTTP/1.1 413 Payload Too Large\n"
    resp += "Date "+ str(datetime.datetime.now(datetime.timezone.utc).strftime("%a, %d %b %Y %H:%M:%S GMT")) + "\n"
    resp += "Content-Length: " + str(len(filecontent)) + "\n"
    resp += "Content-Type: text/html; charset=iso-8859-1\n"
    resp += "Connection: Close\n\n"
    resp += filecontent + "\n"
    return resp
    

def status414():
    filecontent = '<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">\n<html><head>\n<title>414 Request-URI Too Long</title>\n</head><body>\n<h1>Request-URI Too Long</h1>\n<p>The requested URL\'s length exceeds the capacity limit for this server.<br /></p>\n<hr>\n<address>HTTP Server at 127.0.0.1 Port '+ str(serverPort) +' </address>\n</body></html>'
    resp = ''
    resp = resp + "HTTP/1.1 414 URI Too Long\n"
    resp += "Content-Length: " + str(len(filecontent)) + "\n"
    resp += "Content-Type: text/html; charset=iso-8859-1\n"
    resp += "Server: HTTP Server\n"
    resp += "Connection: Close\n\n"
    resp += filecontent + "\n"
    return resp

def status415():
    filecontent = '<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">\n<html><head>\n<title>415 Unsupported Media Type</title>\n</head><body>\n<h1>Unsupported Media Type</h1>\n<p>The requested media type is not supported.<br /></p>\n<hr>\n<address>HTTP Server at 127.0.0.1 Port '+ str(serverPort) +' </address>\n</body></html>'
    resp = ''
    resp = resp + "HTTP/1.1 415 Unsupported Media Type\n"
    resp += "Content-Length: " + str(len(filecontent)) + "\n"
    resp += "Content-Type: text/html; charset=iso-8859-1\n"
    resp += "Server: HTTP Server\n"
    resp += "Connection: Close\n\n"
    resp += filecontent + "\n"
    return resp

def status501(reqli):
    filecontent = '<html><head>\n<title>501 Not Implemented</title>\n</head><body>\n<h1>Not Implemented</h1>\n<p>'+ reqli[0][0]+' not supported for current URL.<br />\n</p>\n<hr>\n<address>HTTP Server at 127.0.0.1 Port ' + str(serverPort) +' </address>\n</body></html>'
    resp = ''
    resp = resp + "HTTP/1.1 501 Not Implemented\n"
    resp += "Date "+ str(datetime.datetime.now(datetime.timezone.utc).strftime("%a, %d %b %Y %H:%M:%S GMT")) + "\n"
    resp += "Allow: GET,POST,OPTIONS,HEAD\n"
    resp += "Content-Length: " + str(len(filecontent)) + "\n"
    resp += "Content-Type: text/html; charset=iso-8859-1\n\n"
    if reqli[0][0] != "HEAD":
        resp += filecontent + "\n"
    return resp

def status505():
    filecontent = '<html><head>\n<title>505 HTTP Version Not Supported</title>\n</head><body>\n<h1>HTTP Version Not Supported</h1>\n<p>This HTTP version is not supported<br/>\n</p>\n<hr>\n<address>HTTP Server at 127.0.0.1 Port ' + str(serverPort) +' </address>\n</body></html>'
    resp = ''
    resp += "505 HTTP Version Not Supported\n"
    resp += "Date "+ str(datetime.datetime.now(datetime.timezone.utc).strftime("%a, %d %b %Y %H:%M:%S GMT")) + "\n"
    resp += "Server: HTTP Server\n"
    resp += "Content-Length: " + str(len(filecontent)) + "\n"
    resp += "Content-Type: text/html; charset=iso-8859-1\n"
    resp += "Connection: Closed\n\n"
    resp += filecontent + "\n"
    return resp




def generateResponse(reqli):
    global resp
    if reqli[0][0] == "GET":
        if reqli[0][2] != "HTTP/1.1":
            if reqli[0][2][:5] == "HTTP/":
                resp = status505()
            else:
                resp = status400()
        else:
            resp = status200(reqli)
    elif reqli[0][0] == "HEAD":
        if reqli[0][2] != "HTTP/1.1":
            if reqli[0][2][:5] == "HTTP/":
                resp = status505()
            else:
                resp = status400()
        else:
            resp = status200(reqli)

    elif reqli[0][0] == "POST":
        if reqli[0][2] != "HTTP/1.1":
            if reqli[0][2][:5] == "HTTP/":
                resp = status505()
            else:
                resp = status400()
        elif len(reqli[0][1][1:]) >= Maxuri:
            resp = status414()
        elif len(postdata) >= MaxPayloadLength:
            resp = status413()
        else:
            resp = status200(reqli)

    elif reqli[0][0] == "PUT":
        if reqli[0][2] != "HTTP/1.1":
            if reqli[0][2][:5] == "HTTP/":
                resp = status505()
            else:
                resp = status400()
        elif len(reqli[0][1][1:]) >= Maxuri:
            resp = status414()
        elif len(body) >= MaxPayloadLength:
            resp = status413()
        else:
            try:
                if headers['Content-Length']:
                    if len(body) == 1:
                        resp = status204()
                    elif not os.path.isfile(reqli[0][1][1:]):
                        resp = status201(reqli)
                    else:
                        perm = os.access(reqli[0][1][1:], os.W_OK)
                        if not perm:
                            return status403()
                        resp = status200(reqli)
            except:
                resp = status411()

    elif reqli[0][0] == "DELETE":
        if reqli[0][2] != "HTTP/1.1":
            if reqli[0][2][:5] == "HTTP/":
                resp = status505()
            else:
                resp = status400()
        elif len(reqli[0][1][1:]) >= Maxuri:
            resp = status414()
        elif os.path.isfile(reqli[0][1][1:]):
            if os.path.getsize(reqli[0][1][1:]) == 0:
                resp = status204()
                os.remove(reqli[0][1][1:])
            else:
                resp = status200(reqli)
                if resp[9:12] == "200":
                    os.remove(reqli[0][1][1:])
        else:
            resp = status404()
    else:
        resp = status501(reqli)

def SetCookie():
    for x in cookies:
        if x not in sent_cookies:
            id = x
            DateTime = (datetime.datetime.now() + datetime.timedelta(days=1))
            value=cookies[id]
            date = DateTime.strftime("%a, %d %B %Y %I:%M:%S ")
            if id not in sent_cookies.keys():
                sent_cookies[id] = date
            break
        else:
            continue
    if id:
        cookie = "Set-Cookie: "
        cookie += id + "="
        cookie += value
        cookie += "; "
        cookie += "Expires="
        DateTime = (datetime.datetime.now() + datetime.timedelta(days=1))
        cookie += DateTime.strftime("%a, %d %B %Y %I:%M:%S")
        cookie += "GMT;"
        return cookie
    else:
        return None

def parseRequest(req):
    reqli = req.split('\r\n')
    reql = reqli.copy()
    for i in range(len(reqli)):
        reqli[i] = reqli[i].split()
    try:
        if reqli[0][1] == "/":
            reqli[0][1] = '/index.html'
    except:
        pass
    i = 1
    while len(reqli[i]) != 0:
        headers[reqli[i][0][:-1]] = ''
        for j in range(1, len(reqli[i])):
            headers[reqli[i][0][:-1]] += reqli[i][j] + ' '
        headers[reqli[i][0][:-1]] = headers[reqli[i][0][:-1]][:-1]
        i += 1
        
    global body
    body = ''
    i += 1
    while i < len(reql):
        body += reql[i] + "\n"
        i +=1 
    return reqli


def logfile(reqli, resp, postdata):
    x = datetime.datetime.now()
    #Writing into a log file
    #127.0.0.1 - frank [10/Oct/2000:13:55:36 -0700] "GET /apache_pb.gif HTTP/1.0" 200 2326
    #[Sun Oct 25 21:48:13.024675 2020] [core:error] [pid 1642:tid 140220884317952] [client ::1:34924] AH00135: Invalid method in request GETT /index.html HTTP/1.1
    try:
        f = open("access.log", "a")
        j = open("error.log", "a")
        if reqli[0][0] != "POST":
            if resp[9:12] == "501":
                f.write('127.0.0.1 - - [' + x.strftime("%d") + '/' + x.strftime("%b") + '/' + x.strftime("%Y") + ':' + x.strftime("%H") + ':' + x.strftime("%M") + ':' + x.strftime("%S") + ' +' + x.strftime("%z") +'] "' + reqli[0][0] + ' /' + reqli[0][1][1:] + ' HTTP/1.1"' +  resp[9:12] + ' ' + str(os.stat(reqli[0][1][1:]).st_size) + ' "-" "' + headers['User-Agent'] + '"\n') 
                j.write('127.0.0.1 - - [' + x.strftime("%d") + '/' + x.strftime("%b") + '/' + x.strftime("%Y") + ':' + x.strftime("%H") + ':' + x.strftime("%M") + ':' + x.strftime("%S") + ' +' + x.strftime("%z") +'] "' + reqli[0][0] + ' /' + reqli[0][1][1:] + ' HTTP/1.1"' +  resp[9:12] + ' ' + str(os.stat(reqli[0][1][1:]).st_size) + ' "-" "' + headers['User-Agent'] + '"\n')
            elif resp[9:12] == "404":
                f.write('127.0.0.1 - [' + x.strftime("%d") + '/' + x.strftime("%b") + '/' + x.strftime("%Y") + ':' + x.strftime("%H") + ':' + x.strftime("%M") + ':' + x.strftime("%S") + ' -' + x.strftime("%z") +'] "' + reqli[0][0] + ' /' + reqli[0][1][1:] + ' HTTP/1.1"' +  resp[9:12] + ' "-" "' + headers['User-Agent'] + '"\n')
                j.write('127.0.0.1 - [' + x.strftime("%d") + '/' + x.strftime("%b") + '/' + x.strftime("%Y") + ':' + x.strftime("%H") + ':' + x.strftime("%M") + ':' + x.strftime("%S") + ' -' + x.strftime("%z") +'] "' + reqli[0][0] + ' /' + reqli[0][1][1:] + ' HTTP/1.1"' +  resp[9:12] + ' "-" "' + headers['User-Agent'] + '"\n')
            elif resp[9:12] == "400":
                f.write('127.0.0.1 - [' + x.strftime("%d") + '/' + x.strftime("%b") + '/' + x.strftime("%Y") + ':' + x.strftime("%H") + ':' + x.strftime("%M") + ':' + x.strftime("%S") + ' -' + x.strftime("%z") +'] "' + reqli[0][0] + ' /' + reqli[0][1][1:] + ' HTTP/1.1"' +  resp[9:12] + ' ' + '-\n')
                j.write('127.0.0.1 - [' + x.strftime("%d") + '/' + x.strftime("%b") + '/' + x.strftime("%Y") + ':' + x.strftime("%H") + ':' + x.strftime("%M") + ':' + x.strftime("%S") + ' -' + x.strftime("%z") +'] "' + reqli[0][0] + ' /' + reqli[0][1][1:] + ' HTTP/1.1"' +  resp[9:12] + ' ' + '-\n')
            elif resp[9:12] == "414" or resp[9:12] == "415":
                f.write('127.0.0.1 - [' + x.strftime("%d") + '/' + x.strftime("%b") + '/' + x.strftime("%Y") + ':' + x.strftime("%H") + ':' + x.strftime("%M") + ':' + x.strftime("%S") + ' -' + x.strftime("%z") +'] "' + reqli[0][0] + ' /' + reqli[0][1][1:] + ' HTTP/1.1"' +  resp[9:12] + ' "-" "' + headers['User-Agent'] + '"\n')
                if resp[9:12] == "415":
                    j.write('127.0.0.1 - [' + x.strftime("%d") + '/' + x.strftime("%b") + '/' + x.strftime("%Y") + ':' + x.strftime("%H") + ':' + x.strftime("%M") + ':' + x.strftime("%S") + ' -' + x.strftime("%z") +'] "' + reqli[0][0] + ' /' + reqli[0][1][1:] + ' HTTP/1.1"' +  resp[9:12] + ' "-" "' + headers['User-Agent'] + '"\n')
            else:
                f.write('127.0.0.1 - - [' + x.strftime("%d") + '/' + x.strftime("%b") + '/' + x.strftime("%Y") + ':' + x.strftime("%H") + ':' + x.strftime("%M") + ':' + x.strftime("%S") + ' +' + x.strftime("%z") +'] "' + reqli[0][0] + ' /' + reqli[0][1][1:] + ' HTTP/1.1"' +  resp[9:12] + ' ' + str(os.stat(reqli[0][1][1:]).st_size) + ' "-" "' + headers['User-Agent'] + '"\n') 
        else:
            if reqli[0][0] == "DELETE":
                f.write('127.0.0.1 - - [' + x.strftime("%d") + '/' + x.strftime("%b") + '/' + x.strftime("%Y") + ':' + x.strftime("%H") + ':' + x.strftime("%M") + ':' + x.strftime("%S") + ' +' + x.strftime("%z") +'] "' + reqli[0][0] + ' /' + reqli[0][1][1:] + ' HTTP/1.1"' +  resp[9:12] + ' - "-" "' + headers['User-Agent'] + '"\n')
            elif reqli[0][0] == "POST":
                f.write('127.0.0.1 - - [' + x.strftime("%d") + '/' + x.strftime("%b") + '/' + x.strftime("%Y") + ':' + x.strftime("%H") + ':' + x.strftime("%M") + ':' + x.strftime("%S") + ' +' + x.strftime("%z") +'] "' + reqli[0][0] + ' /' + reqli[0][1][1:] + ' HTTP/1.1"' +  resp[9:12] + ' ' + str(os.stat(reqli[0][1][1:]).st_size) + ' "-" "' + headers['User-Agent'] + '"\n' + postdata.replace("&", "\n") + '\n') 
            else:
                f.write('127.0.0.1 - - [' + x.strftime("%d") + '/' + x.strftime("%b") + '/' + x.strftime("%Y") + ':' + x.strftime("%H") + ':' + x.strftime("%M") + ':' + x.strftime("%S") + ' +' + x.strftime("%z") +'] "' + reqli[0][0] + ' /' + reqli[0][1][1:] + ' HTTP/1.1"' +  resp[9:12] + ' ' + str(os.stat(reqli[0][1][1:]).st_size) + ' "-" "' + headers['User-Agent'] + '"\n')
        f.close()
        j.close() 
    except:
        pass


def quitserver():
    stop = input()
    if stop == "quit":
        print("Server stopped")
        os._exit(os.EX_OK) 


if __name__ == "__main__":
    quitthread = Thread(target = quitserver, args = ())
    quitthread.start()
    while True:
        connectionSocket, addr = serverSocket.accept()
        start_time = time.time()
        print('new request received from')
        print(addr)
        print('connectionSocket is')
        print(connectionSocket)
        req = connectionSocket.recv(1024)
        req = req.decode()
        if req[0:4] == "POST":
            postdata = req[req.rindex("\r\n"):]
        reqli = parseRequest(req)
        t1 = Thread(target = generateResponse, args = (reqli, ))
        t1.start()
        time.sleep(0.001)
        logfile(reqli, resp, postdata)
        number_of_connections =  threading.active_count() 
        if number_of_connections - 2 > MaxKeepAliveRequests:
            f = open("error.log", "a")
            f.write("Maximum no of connections exceeded\n")
            f.close()
        if resp is None:
            resp = "manish"
        
        end_time = time.time()
        if end_time - start_time > Timeout:
            resp = status408()
        connectionSocket.send(resp.encode())
        if byte:
            connectionSocket.send(byte)
            byte=None
        connectionSocket.close()