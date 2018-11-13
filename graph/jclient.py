#! /usr/bin/env python3
# Modified version ofjclient from mimimal-jsonrpc-demo. Supposed to send a serialized tree
# To be incremented by a server.

import socket
import json
from serialize import *
from node import *
from bsonrpc import JSONRpc
from bsonrpc.exceptions import FramingError
from bsonrpc.framing import (
	JSONFramingNetstring, JSONFramingNone, JSONFramingRFC7464)

# Cut-the-corners TCP Client:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 50001))

rpc = JSONRpc(s,framing_cls=JSONFramingNone)
server = rpc.get_peer_proxy()

# Build the graph:
leaf1 = node("leaf1")
leaf2 = node("leaf2")
root = node("root", [leaf1, leaf1, leaf2])

#Flatten the graph.
flatTree = flatten(root)

jTree = json.dumps(flatTree) #JSON encoded graph.

#Write the request to a file.
with open('request.json','w') as jFile:
    json.dump(flatTree, jFile)
jFile.close()

fileName = 'request.json'

result = server.sIncrement('request.json')
print(result)

rpc.close() # Closes the socket 's' also
