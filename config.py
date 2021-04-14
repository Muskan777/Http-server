#
# KeepAlive: Whether or not to allow persistent connections (more than
# one request per connection). Set to "Off" to deactivate.
#

keepAlive = "off"

##
# MaxKeepAliveRequests: The maximum number of requests to allow
# during a persistent connection. Set to 0 to allow an unlimited amount.
# We recommend you leave this number high, for maximum performance.
#
MaxKeepAliveRequests = 50

# Timeout: The number of seconds before receives and sends time out.
Timeout = 3000

# KeepAlive: Whether or not to allow persistent connections (more than
# one request per connection). Set to "Off" to deactivate.
KeepAlive = False

# HostnameLookups: Log the names of clients or just their IP addresses
# e.g., www.apache.org (on) or 204.62.129.132 (off).
# The default is off because it'd be overall better for the net if people
# had to knowingly turn this feature on, since enabling it means that
# each client request will result in AT LEAST one lookup request to the
# nameserver.


Maxuri = 300

MaxPayloadLength = 400

HostnameLookups = False

ErrorLog = 'error.log'

AccessLog = 'access.log'

oldaddr_301 = "redirect.html"
newaddr_301 = "COEP/redirect.html"

#avaliable cookies and sent cookies info:
cookies = {
    "mycookie": "xyzabc",
    "yummy_cookie": "choco",
    "tasty_cookie": "strawberry",
    "pqrstu" : "vwxyz",
}

sent_cookies = {}

#Log format = hostip - [date/month/year hr:min:sec -timezone] "request filename HTTP/1.1" responsecode filelength

