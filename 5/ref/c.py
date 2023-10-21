import socket
import json
import base64

from Crypto import Random
from Crypto.Hash import SHA


#create socket 
comSocket = socket.socket()

#connect with server 
svrIP = "127.0.0.1"
comSocket.connect((svrIP,2500))
print('\tConnected to '+svrIP)

#user enter uid 
uid = input(("id: "))

#send uid 
#"e.g) "I am Alice"
msg1=  json.dumps ( {'uid': uid })
comSocket.send(msg1.encode()) 
print ("\tSent : ", msg1)

#receive nonce from socket 
msg2= comSocket.recv(1024).decode()
nonceStr=json.loads( msg2)['nonce'].encode()
nonce=base64.b64decode( nonceStr )
print ("\tReceived : ", msg2)

#enter password
pw = input("password: ").encode()
#hash password with nonce 
h=SHA.new( pw+nonce).digest()
hStr=base64.b64encode(h).decode()
msg3=  json.dumps ( {'h': hStr })

#send hash value 
comSocket.send(msg3.encode()) 
print ("\tSent : ", msg3)

