#! /usr/bin/env python3
# Methods for "flattening" a graph into a dictionary, and turning it back into a tree.
from node import *
import json

def flatten(root):
    tDict = {}
    cList = []
    
    # Children field will be list of dictionaries.
    if root.children:
        for c in root.children:
            cDict = {
                "name": c.name,
                "val": c.val,
                "children": None
            }
            cList.append(cDict)
    else:
        cList = None

    # Now turn the node and its kids into a dict.
    tDict["name"] = root.name
    tDict["val"] = root.val
    tDict["children"] = cList
    
    return tDict
    
    
def unflatten(jFile):
    with open(jFile) as lFile:
      j = json.load(lFile)
    lFile.close()
    
    jlist = j["children"]
    
    leaf1 = node(jlist[0]["name"])
    leaf1.val = jlist[0]["val"]
    
    leaf2 = node(jlist[1]["name"])
    leaf1.val = jlist[1]["val"]
    
    leaf3 = node(jlist[2]["name"])
    leaf1.val = jlist[2]["val"]
    
    root = node(j["name"], [leaf1,leaf2,leaf3])
    root.val = j["val"]
    
    root.show()
    return root
