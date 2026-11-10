"""Symbol Table for a Mini-Compiler using BST.

Course: IC-307D Data Structures & Algorithms LAB
Student: Jayesh Solanki | Roll No: IC-2K23-45
Unit 6: Trees (CO3) Application
"""

from typing import Any, Dict, List, Optional


class SymbolInfo:
    def __init__(self, name: str, var_type: str, scope_level: int, value: Any = None) -> None:
        self.name: str = name
        self.var_type: str = var_type
        self.scope_level: int = scope_level
        self.value: Any = value


class SymbolNode:
    def __init__(self, symbol: SymbolInfo) -> None:
        self.symbol: SymbolInfo = symbol
        self.left: Optional["SymbolNode"] = None
        self.right: Optional["SymbolNode"] = None


class SymbolTableBST:
    """Symbol Table backed by Binary Search Tree for identifier resolution and type tracking."""

    def __init__(self) -> None:
        self.root: Optional[SymbolNode] = None

    def insert(self, name: str, var_type: str, scope_level: int, value: Any = None) -> None:
        sym = SymbolInfo(name, var_type, scope_level, value)
        self.root = self._insert(self.root, sym)

    def _insert(self, node: Optional[SymbolNode], sym: SymbolInfo) -> SymbolNode:
        if not node:
            return SymbolNode(sym)
        if sym.name < node.symbol.name:
            node.left = self._insert(node.left, sym)
        elif sym.name > node.symbol.name:
            node.right = self._insert(node.right, sym)
        else:
            # Update symbol in same scope
            node.symbol = sym
        return node

    def lookup(self, name: str) -> Optional[SymbolInfo]:
        curr = self.root
        while curr:
            if name == curr.symbol.name:
                return curr.symbol
            elif name < curr.symbol.name:
                curr = curr.left
            else:
                curr = curr.right
        return None

    def list_symbols(self) -> List[Dict[str, Any]]:
        res: List[Dict[str, Any]] = []
        def _in(n: Optional[SymbolNode]):
            if n:
                _in(n.left)
                res.append({
                    "name": n.symbol.name,
                    "type": n.symbol.var_type,
                    "scope": n.symbol.scope_level,
                    "value": n.symbol.value,
                })
                _in(n.right)
        _in(self.root)
        return res


def demo() -> None:
    st = SymbolTableBST()
    st.insert("counter", "int", 0, 100)
    st.insert("pi", "float", 0, 3.14159)
    st.insert("flag", "bool", 1, True)

    print("Symbol Table Lookup 'pi':")
    sym = st.lookup("pi")
    if sym:
        print(f"  Name: {sym.name}, Type: {sym.var_type}, Value: {sym.value}")

    print("\nAll Symbols (Sorted by Identifier):")
    for s in st.list_symbols():
        print(f"  {s['name']:<10} | Type: {s['type']:<6} | Scope: {s['scope']} | Value: {s['value']}")


if __name__ == "__main__":
    demo()
