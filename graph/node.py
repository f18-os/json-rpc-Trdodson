class node:
    def __init__(self, name, children = []):
        self.name = name
        self.children = children
        self.val = 0
    def show(self, level=0):
        print("%s%s val=%d:" % (level*"  ", self.name, self.val))
        for c in self.children: 
            c.show(level + 1)
    def toJson(self): #method from: https://stackoverflow.com/questions/7509258/encoding-a-binary-tree-structure-to-json-format
        return {
            "name": self.name,
            "val": self.val,
            "children": self.children[0].toJson() if self.children else None,
        }

def increment(graph):
    graph.val += 1;
    for c in graph.children:
        increment(c)

