"""Directory Manager / Autocomplete Dictionary using Trie.

Course: IC-307D Data Structures & Algorithms LAB
Student: Jayesh Solanki | Roll No: IC-2K23-45
Unit 6: Trees (CO3) Application / Bonus
"""

from typing import Dict, List, Optional


class TrieNode:
    def __init__(self) -> None:
        self.children: Dict[str, "TrieNode"] = {}
        self.is_end_of_word: bool = False


class AutocompleteTrie:
    """Prefix-Tree (Trie) for dictionary word lookup and autocompletion."""

    def __init__(self) -> None:
        self.root: TrieNode = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word.lower():
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_end_of_word = True

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word.lower():
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.is_end_of_word

    def autocomplete(self, prefix: str) -> List[str]:
        """Find all stored words beginning with the given prefix."""
        curr = self.root
        for char in prefix.lower():
            if char not in curr.children:
                return []
            curr = curr.children[char]

        results: List[str] = []
        def _dfs(node: TrieNode, current_path: str):
            if node.is_end_of_word:
                results.append(prefix.lower() + current_path)
            for ch in sorted(node.children.keys()):
                _dfs(node.children[ch], current_path + ch)

        _dfs(curr, "")
        return results


def demo() -> None:
    trie = AutocompleteTrie()
    words = ["algorithm", "algo", "algebra", "apple", "app", "application", "binary", "tree"]
    for w in words:
        trie.insert(w)

    print("Words with prefix 'alg':", trie.autocomplete("alg"))
    print("Words with prefix 'app':", trie.autocomplete("app"))
    print("Words with prefix 'b':", trie.autocomplete("b"))


if __name__ == "__main__":
    demo()
