"""Polynomial Representation and Addition using Linked Lists.

Course: IC-307D Data Structures & Algorithms LAB
Student: Jayesh Solanki | Roll No: IC-2K23-45
Unit 3: Linked Lists (CO1)
"""

from typing import List, Optional, Tuple


class PolyTermNode:
    """Node representing a single term in a polynomial: coeff * x^exp."""

    def __init__(
        self,
        coeff: float,
        exp: int,
        next_term: Optional["PolyTermNode"] = None,
    ) -> None:
        self.coeff: float = coeff
        self.exp: int = exp
        self.next: Optional["PolyTermNode"] = next_term


class PolynomialLinkedList:
    """Polynomial represented as a descending sorted linked list of non-zero terms."""

    def __init__(self) -> None:
        self.head: Optional[PolyTermNode] = None

    def insert_term(self, coeff: float, exp: int) -> None:
        """Insert a term into the polynomial maintaining descending exponent order."""
        if coeff == 0:
            return

        new_node = PolyTermNode(coeff, exp)
        if not self.head or exp > self.head.exp:
            new_node.next = self.head
            self.head = new_node
            return

        if self.head.exp == exp:
            self.head.coeff += coeff
            if self.head.coeff == 0:
                self.head = self.head.next
            return

        prev = self.head
        curr = self.head.next
        while curr and curr.exp > exp:
            prev = curr
            curr = curr.next

        if curr and curr.exp == exp:
            curr.coeff += coeff
            if curr.coeff == 0:
                prev.next = curr.next
        else:
            new_node.next = curr
            prev.next = new_node

    def to_list(self) -> List[Tuple[float, int]]:
        """Return list of (coeff, exp) tuples."""
        terms = []
        curr = self.head
        while curr:
            terms.append((curr.coeff, curr.exp))
            curr = curr.next
        return terms

    def __str__(self) -> str:
        """Pretty string representation of the polynomial."""
        if not self.head:
            return "0"
        parts = []
        curr = self.head
        while curr:
            c = curr.coeff
            e = curr.exp
            sign = "+ " if c > 0 and parts else ("- " if c < 0 and parts else ("-" if c < 0 else ""))
            abs_c = abs(c)
            coeff_str = f"{abs_c:g}"
            if e == 0:
                parts.append(f"{sign}{coeff_str}")
            elif e == 1:
                term = f"{coeff_str}x" if abs_c != 1 else "x"
                parts.append(f"{sign}{term}")
            else:
                term = f"{coeff_str}x^{e}" if abs_c != 1 else f"x^{e}"
                parts.append(f"{sign}{term}")
            curr = curr.next
        return " ".join(parts)

    def add(self, other: "PolynomialLinkedList") -> "PolynomialLinkedList":
        """Add two polynomials using a two-pointer merge traversal in O(m + n)."""
        result = PolynomialLinkedList()
        p1 = self.head
        p2 = other.head

        while p1 and p2:
            if p1.exp > p2.exp:
                result.insert_term(p1.coeff, p1.exp)
                p1 = p1.next
            elif p1.exp < p2.exp:
                result.insert_term(p2.coeff, p2.exp)
                p2 = p2.next
            else:
                sum_coeff = p1.coeff + p2.coeff
                if sum_coeff != 0:
                    result.insert_term(sum_coeff, p1.exp)
                p1 = p1.next
                p2 = p2.next

        while p1:
            result.insert_term(p1.coeff, p1.exp)
            p1 = p1.next

        while p2:
            result.insert_term(p2.coeff, p2.exp)
            p2 = p2.next

        return result


def demo() -> None:
    """Demonstrate polynomial operations."""
    p1 = PolynomialLinkedList()
    p1.insert_term(5, 3)
    p1.insert_term(4, 2)
    p1.insert_term(2, 0)
    print("P1:", p1)

    p2 = PolynomialLinkedList()
    p2.insert_term(5, 1)
    p2.insert_term(-5, 3)
    p2.insert_term(3, 2)
    print("P2:", p2)

    sum_p = p1.add(p2)
    print("P1 + P2:", sum_p)


if __name__ == "__main__":
    demo()
