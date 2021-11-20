class Node:
    def __init__(self, tabla):
        self.children = None
        self.parents = None
        self.tabla = tabla

    def set_children(self, children):
        if self.children is not None:
            print("This node's children has already been set.")
        self.children = children

    def set_parents(self, parents):
        if self.parents is not None:
            print("This node's parents has already been set.")
        self.parents = parents

    def is_leaf(self):
        if self.children is None:
            raise RuntimeError("Children are not set yet.")
        return len(self.children) == 0

    def is_root(self):
        if self.parents is None:
            raise RuntimeError("Parents are not set yet.")
        return len(self.parents) == 0

    def is_branch(self):
        return not self.is_leaf() and not self.is_root()

    #def is_win(self, hanyadik, cel):
        #TODO
