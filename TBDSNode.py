class TBDSNode:
    def __init__(self) -> None:
        self.children = {}
        self.value = None
    
    @property
    def children(self) -> dict:
        return self._children

    @children.setter
    def children(self, children: dict) -> None:
        self._children = children

    @property
    def value(self) -> str:
        return self._value

    @value.setter
    def value(self, value: str) -> None:
        self._value = value
