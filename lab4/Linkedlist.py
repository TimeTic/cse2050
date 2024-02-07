from typing import Any, Optional
class Node():
    def __init__(self, item: Any, link: Optional['Node'] = None ) -> None:
        self.item = item
        self.link = link

    def ___repr__(self) -> str:
        return f"Node{(self.item)}"
    
    class Linkedlist():
        