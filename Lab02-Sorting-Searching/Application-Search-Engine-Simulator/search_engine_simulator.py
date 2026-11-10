"""Dictionary search simulator: binary search, chaining, and linear probing."""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from sorting_algorithms import binary_search


def normalize(word):
    if not isinstance(word, str) or not word.strip():
        raise ValueError("word must be a non-empty string")
    return word.strip().casefold()


def next_prime(number):
    number = max(5, number)
    while True:
        for divisor in range(2, int(number ** 0.5) + 1):
            if number % divisor == 0: break
        else: return number
        number += 1


class ChainingHashTable:
    """Hash table in which each slot stores a list of key/value pairs."""
    def __init__(self, capacity=11):
        self.capacity = next_prime(capacity)
        self.buckets = [[] for _ in range(self.capacity)]
        self.size = 0
        self.collision_count = 0

    def _hash(self, key):
        value = 0
        for char in key: value = (value * 31 + ord(char)) % self.capacity
        return value

    def _insert_raw(self, key, value):
        bucket = self.buckets[self._hash(key)]
        for i, (old_key, _) in enumerate(bucket):
            if old_key == key:
                bucket[i] = (key, value)
                return
        if bucket: self.collision_count += 1
        bucket.append((key, value))
        self.size += 1

    def _resize(self):
        old = [item for bucket in self.buckets for item in bucket]
        self.capacity = next_prime(self.capacity * 2)
        self.buckets, self.size = [[] for _ in range(self.capacity)], 0
        for key, value in old: self._insert_raw(key, value)

    def add(self, key, value):
        key = normalize(key)
        if (self.size + 1) / self.capacity > 0.75: self._resize()
        self._insert_raw(key, value)

    def get(self, key):
        key = normalize(key)
        for old_key, value in self.buckets[self._hash(key)]:
            if old_key == key: return value
        return None

    def remove(self, key):
        key = normalize(key)
        bucket = self.buckets[self._hash(key)]
        for i, (old_key, _) in enumerate(bucket):
            if old_key == key:
                bucket.pop(i); self.size -= 1
                return True
        return False


class LinearProbingHashTable:
    """Open-addressed hash table using the next free slot on collision."""
    DELETED = object()

    def __init__(self, capacity=11):
        self.capacity = next_prime(capacity)
        self.slots = [None] * self.capacity
        self.size = 0
        self.collision_count = 0

    def _hash(self, key):
        value = 0
        for char in key: value = (value * 31 + ord(char)) % self.capacity
        return value

    def _find(self, key):
        start, first_deleted = self._hash(key), None
        for step in range(self.capacity):
            index = (start + step) % self.capacity
            item = self.slots[index]
            if item is None:
                return (first_deleted if first_deleted is not None else index), False
            if item is self.DELETED:
                if first_deleted is None: first_deleted = index
            elif item[0] == key:
                return index, True
        return (first_deleted, False) if first_deleted is not None else (None, False)

    def _resize(self):
        old = [item for item in self.slots if item is not None and item is not self.DELETED]
        self.capacity = next_prime(self.capacity * 2)
        self.slots, self.size = [None] * self.capacity, 0
        for key, value in old:
            index, _ = self._find(key)
            self.slots[index] = (key, value)
            self.size += 1

    def add(self, key, value):
        key = normalize(key)
        if (self.size + 1) / self.capacity > 0.65: self._resize()
        index, found = self._find(key)
        if index is None:
            self._resize()
            index, found = self._find(key)
        if not found and self.slots[index] is not None: self.collision_count += 1
        self.slots[index] = (key, value)
        if not found: self.size += 1

    def get(self, key):
        index, found = self._find(normalize(key))
        return self.slots[index][1] if found else None

    def remove(self, key):
        index, found = self._find(normalize(key))
        if not found: return False
        self.slots[index] = self.DELETED
        self.size -= 1
        return True


class DictionarySearchEngine:
    """Synchronize a sorted dictionary and both hash-table variants."""
    def __init__(self, entries=()):
        self.sorted_entries = []
        self.chaining = ChainingHashTable()
        self.linear_probing = LinearProbingHashTable()
        for word, meaning in entries: self.add(word, meaning)

    def add(self, word, meaning):
        key = normalize(word)
        self.remove(key)
        self.sorted_entries.append((key, meaning))
        self.sorted_entries.sort(key=lambda item: item[0])
        self.chaining.add(key, meaning)
        self.linear_probing.add(key, meaning)

    def remove(self, word):
        key = normalize(word)
        index = binary_search(self.sorted_entries, key, key=lambda item: item[0])
        if index == -1: return False
        self.sorted_entries.pop(index)
        self.chaining.remove(key)
        self.linear_probing.remove(key)
        return True

    def lookup(self, word, strategy="binary"):
        key = normalize(word)
        if strategy == "binary":
            index = binary_search(self.sorted_entries, key, key=lambda item: item[0])
            return self.sorted_entries[index][1] if index != -1 else None
        if strategy == "chaining": return self.chaining.get(key)
        if strategy in {"linear", "linear-probing"}: return self.linear_probing.get(key)
        raise ValueError("strategy must be binary, chaining, or linear-probing")


def main():
    dictionary = DictionarySearchEngine([
        ("array", "A collection of elements stored in indexed order."),
        ("graph", "A set of vertices connected by edges."),
        ("queue", "A FIFO data structure."),
        ("stack", "A LIFO data structure."),
        ("tree", "A hierarchical data structure."),
    ])
    print("DICTIONARY SEARCH ENGINE")
    print("Strategies: binary, chaining, linear-probing")
    while True:
        word = input("\nWord to look up (or 'exit'): ").strip()
        if word.casefold() == "exit": return
        try:
            strategy = input("Search strategy: ").strip().lower()
            meaning = dictionary.lookup(word, strategy)
            print(meaning if meaning is not None else "Word not found.")
        except ValueError as exc:
            print(f"Input error: {exc}")


if __name__ == "__main__":
    main()
