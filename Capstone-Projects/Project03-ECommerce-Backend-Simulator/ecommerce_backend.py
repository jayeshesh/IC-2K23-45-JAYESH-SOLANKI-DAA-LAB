"""Capstone Project 3: E-Commerce Backend Simulator.

Combines:
- Product Catalog indexed by Price / ID (BST)
- User Shopping Cart with Undo Item Addition (Stack)
- Real-time Order Processing Engine (Queue)
- Product Recommendation Engine / "Frequently Bought Together" (Graph)

Course: IC-307D Data Structures & Algorithms LAB
Student: Jayesh Solanki | Roll No: IC-2K23-45
"""

from typing import Dict, List, Optional, Set


class ProductNode:
    def __init__(self, pid: int, title: str, price: float) -> None:
        self.pid: int = pid
        self.title: str = title
        self.price: float = price
        self.left: Optional["ProductNode"] = None
        self.right: Optional["ProductNode"] = None


class ProductCatalogBST:
    """Product catalog indexed by product ID using BST."""

    def __init__(self) -> None:
        self.root: Optional[ProductNode] = None

    def insert(self, pid: int, title: str, price: float) -> None:
        self.root = self._insert(self.root, pid, title, price)

    def _insert(self, node: Optional[ProductNode], pid: int, title: str, price: float) -> ProductNode:
        if not node:
            return ProductNode(pid, title, price)
        if pid < node.pid:
            node.left = self._insert(node.left, pid, title, price)
        elif pid > node.pid:
            node.right = self._insert(node.right, pid, title, price)
        return node

    def lookup(self, pid: int) -> Optional[ProductNode]:
        curr = self.root
        while curr:
            if pid == curr.pid:
                return curr
            elif pid < curr.pid:
                curr = curr.left
            else:
                curr = curr.right
        return None


class ECommerceBackend:
    """Full backend simulation combining Catalog (BST), Cart (Stack), Orders (Queue), and Recs (Graph)."""

    def __init__(self) -> None:
        self.catalog: ProductCatalogBST = ProductCatalogBST()
        self.cart_stack: List[ProductNode] = []  # Stack for LIFO undo cart modifications
        self.order_queue: List[Dict[str, any]] = []  # FIFO order processing queue
        self.recommendation_graph: Dict[int, Set[int]] = {}  # Co-purchase graph

    def add_product(self, pid: int, title: str, price: float) -> None:
        self.catalog.insert(pid, title, price)

    def add_to_cart(self, pid: int) -> bool:
        prod = self.catalog.lookup(pid)
        if not prod:
            return False
        self.cart_stack.append(prod)
        return True

    def undo_last_cart_item(self) -> Optional[str]:
        if not self.cart_stack:
            return None
        removed = self.cart_stack.pop()
        return removed.title

    def checkout(self, customer_name: str) -> int:
        if not self.cart_stack:
            raise ValueError("Cart is empty.")
        items = list(self.cart_stack)
        total_price = sum(item.price for item in items)
        order_id = len(self.order_queue) + 1
        order = {
            "order_id": order_id,
            "customer": customer_name,
            "items": [item.title for item in items],
            "total": total_price,
        }
        self.order_queue.append(order)

        # Update recommendation graph for co-purchased items
        item_ids = [item.pid for item in items]
        for i in item_ids:
            if i not in self.recommendation_graph:
                self.recommendation_graph[i] = set()
            for j in item_ids:
                if i != j:
                    self.recommendation_graph[i].add(j)

        self.cart_stack.clear()
        return order_id

    def process_next_order(self) -> Optional[Dict[str, any]]:
        if not self.order_queue:
            return None
        return self.order_queue.pop(0)

    def get_recommendations(self, pid: int) -> List[str]:
        co_purchased = self.recommendation_graph.get(pid, set())
        recs = []
        for r_pid in co_purchased:
            prod = self.catalog.lookup(r_pid)
            if prod:
                recs.append(prod.title)
        return recs


def demo() -> None:
    ec = ECommerceBackend()
    ec.add_product(101, "Laptop", 65000.0)
    ec.add_product(102, "Wireless Mouse", 1200.0)
    ec.add_product(103, "Mechanical Keyboard", 3500.0)

    # User adds to cart
    ec.add_to_cart(101)
    ec.add_to_cart(102)
    ec.add_to_cart(103)
    print("Undo last added item:", ec.undo_last_cart_item())  # Undoes Keyboard

    # Checkout
    oid = ec.checkout("Jayesh Solanki")
    print(f"Order placed with ID: {oid}")

    # Another co-purchase
    ec.add_to_cart(101)
    ec.add_to_cart(103)
    ec.checkout("Aarav")

    print("\nRecommendations for buyers of 'Laptop':", ec.get_recommendations(101))
    print("Processing order FIFO:", ec.process_next_order())


if __name__ == "__main__":
    demo()
