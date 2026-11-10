"""File System Simulator (Hierarchical Tree Structure).

Course: IC-307D Data Structures & Algorithms LAB
Student: Jayesh Solanki | Roll No: IC-2K23-45
Unit 6: Trees (CO3) Application
"""

from typing import Dict, List, Optional


class FSNode:
    def __init__(self, name: str, is_dir: bool = True, parent: Optional["FSNode"] = None) -> None:
        self.name: str = name
        self.is_dir: bool = is_dir
        self.parent: Optional["FSNode"] = parent
        self.children: Dict[str, "FSNode"] = {}


class FileSystemSimulator:
    """N-ary tree hierarchical file system simulator supporting mkdir, touch, cd, and tree/ls."""

    def __init__(self) -> None:
        self.root: FSNode = FSNode("/", is_dir=True)
        self.current: FSNode = self.root

    def mkdir(self, dir_name: str) -> None:
        if dir_name in self.current.children:
            raise FileExistsError(f"Directory '{dir_name}' already exists.")
        self.current.children[dir_name] = FSNode(dir_name, is_dir=True, parent=self.current)

    def touch(self, file_name: str) -> None:
        if file_name in self.current.children:
            raise FileExistsError(f"File '{file_name}' already exists.")
        self.current.children[file_name] = FSNode(file_name, is_dir=False, parent=self.current)

    def cd(self, path: str) -> None:
        if path == "/":
            self.current = self.root
        elif path == "..":
            if self.current.parent:
                self.current = self.current.parent
        elif path in self.current.children:
            target = self.current.children[path]
            if not target.is_dir:
                raise NotADirectoryError(f"'{path}' is not a directory.")
            self.current = target
        else:
            raise FileNotFoundError(f"Path '{path}' not found.")

    def list_dir(self) -> List[str]:
        return sorted(self.current.children.keys())

    def get_tree_view(self, node: Optional[FSNode] = None, prefix: str = "") -> List[str]:
        if node is None:
            node = self.root
        lines = [f"{prefix}{node.name}{'/' if node.is_dir else ''}"]
        if node.is_dir:
            for child in sorted(node.children.values(), key=lambda c: c.name):
                lines.extend(self.get_tree_view(child, prefix + "  "))
        return lines


def demo() -> None:
    fs = FileSystemSimulator()
    fs.mkdir("home")
    fs.mkdir("etc")
    fs.cd("home")
    fs.mkdir("user")
    fs.cd("user")
    fs.touch("notes.txt")
    fs.touch("project.py")
    fs.cd("/")

    print("File System Tree:")
    for line in fs.get_tree_view():
        print(line)


if __name__ == "__main__":
    demo()
