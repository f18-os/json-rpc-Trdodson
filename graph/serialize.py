#! /usr/bin/env python3
# Methods for "flattening" a graph into a dictionary.
import node

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
    
    
