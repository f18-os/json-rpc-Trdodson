#! /usr/bin/env python3

# Modified version ofjclient from minimal-jsonrpc-demo. Supposed to increment graph remotely, then send it back to be
# decoded and printed.

import socket
import json
from serialize import *
from node import *
from bsonrpc import JSONRpc
from bsonrpc import request, service_class
from bsonrpc.exceptions import FramingError
from bsonrpc.framing import (
	JSONFramingNetstring, JSONFramingNone, JSONFramingRFC7464)


# Class providing functions for the client to use:
@service_class
class ServerServices(object):

  @request
  def nop(self, txt):
    print(txt)
    return txt
  
  @request
  def sIncrement(self,jReq):
    jRoot = unflatten(jReq) # Unflatten a json into a tree
    
    jRoot = increment(jRoot) #Increment
    
    jRoot = json.dumps(flatten(jReq)) #Flatten it again into JSON.
    return(jRoot)


# Quick-and-dirty TCP Server:
ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss.bind(('localhost', 50001))
ss.listen(10)

while True:
  s, _ = ss.accept()
  # JSONRpc object spawns internal thread to serve the connection.
  JSONRpc(s, ServerServices(),framing_cls=JSONFramingNone)
