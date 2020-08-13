from websocket_server import WebsocketServer
from flask import Flask, flash, request, redirect, url_for
import base64
import time

# Called for every client connecting (after handshake)
def new_client(client, server):
    # add function if new client connected
    print("New client connected and was given id %d" % client['id'])


# Called for every client disconnecting
def client_left(client, server):
    # add function if client disconnected
    print("Client(%d) disconnected" % client['id'])

# Called when a client sends a message
def message_received(client, server, message):
    
    # create a unique part of file name
    t = str(time.time())[:12]
    uni_name = ('').join(t.split('.'))
    
    # save image send by the client
    path = "" # put the directory path here 
    with open(path + "myfile" + uni_name + ".jpg", "wb") as f:
        img_bytes = base64.urlsafe_b64decode(message[23:])
        f.write(img_bytes)

PORT=5000
server = WebsocketServer(PORT)
server.set_fn_new_client(new_client)
server.set_fn_client_left(client_left)
server.set_fn_message_received(message_received)
server.run_forever()