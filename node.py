from state import State
from win_state import WinState

class Node:
    def __init__(self, state):
        self.children = None
        self.parents = None
        self.state = state
        self.end = None

    def set_children(self, children):
        '''
            Egy csúcs gyerekeit fogja tartalmazni, a graph osztályban állítjuk be.
            A gráf felépítésénél használjuk.
        '''
        if self.children is not None:
            print("This node's children has already been set.")
        self.children = children

    def set_parents(self, parents):
        '''
            Egy csúcs szüleit fogja tartalmazni, a graph osztályban állítjuk be.
            A gráf felépítésénél használjuk.
        '''
        if self.parents is not None:
            print("This node's parents has already been set.")
        self.parents = parents

    def is_leaf(self) -> bool:
        '''
            Megmondja, hogy egy csúcs levél-e.
            A gráf felépítésénél használjuk.
        '''
        return self.state.who_win() != WinState.UNDECIDED

    def is_root(self):
        '''
            Megmondja, hogy egy csúcs gyökér-e.
            A gráf felépítésénél használjuk.
        '''
        if self.parents is None:
            raise RuntimeError("Parents are not set yet.")
        return len(self.parents) == 0

    def is_branch(self):
        '''
            Megmondja, hogy egy csúcs köztes csúcs-e (se nem levél, se nem gyökér.
            Igazából nem is használjuk, de szegényke ne maradjon már ki akkor...
        '''
        return not self.is_leaf() and not self.is_root()







