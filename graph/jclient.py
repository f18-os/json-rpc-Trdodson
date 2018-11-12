#! /usr/bin/env python3

# minimalistic client example from 
# https://github.com/seprich/py-bson-rpc/blob/master/README.md#quickstart

import socket
import json
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

# Build a tree:
leaf1 = node("leaf1")
leaf2 = node("leaf2")
root = node("root", [leaf1, leaf2])

enc = root.toJson()
print(server.nop(enc))

# Execute in server:
result = server.swapper("Hello")
# "!dlroW olleH"

rpc.close() # Closes the socket 's' also
  
