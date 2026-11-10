"""Social Network / Friendship Graph (Friends-of-Friends & Connected Components).

Course: IC-307D Data Structures & Algorithms LAB
Student: Jayesh Solanki | Roll No: IC-2K23-45
Unit 7: Graphs (CO3) Application
"""

from typing import Dict, List, Set


class SocialNetworkGraph:
    """Graph model for users and friendship connections."""

    def __init__(self) -> None:
        self.adj: Dict[str, Set[str]] = {}

    def add_user(self, name: str) -> None:
        if name not in self.adj:
            self.adj[name] = set()

    def add_friendship(self, u: str, v: str) -> None:
        self.add_user(u)
        self.add_user(v)
        self.adj[u].add(v)
        self.adj[v].add(u)

    def get_direct_friends(self, user: str) -> Set[str]:
        return self.adj.get(user, set())

    def get_friends_of_friends(self, user: str) -> Set[str]:
        """Find friends of friends who are not already direct friends or self."""
        if user not in self.adj:
            return set()
        direct = self.adj[user]
        fof: Set[str] = set()
        for friend in direct:
            for mutual in self.adj.get(friend, set()):
                if mutual != user and mutual not in direct:
                    fof.add(mutual)
        return fof

    def get_connected_components(self) -> List[List[str]]:
        """Identify isolated clusters / communities in the social graph."""
        visited: Set[str] = set()
        components: List[List[str]] = []

        for user in self.adj:
            if user not in visited:
                comp: List[str] = []
                queue = [user]
                visited.add(user)
                while queue:
                    u = queue.pop(0)
                    comp.append(u)
                    for v in self.adj[u]:
                        if v not in visited:
                            visited.add(v)
                            queue.append(v)
                components.append(sorted(comp))
        return components


def demo() -> None:
    sn = SocialNetworkGraph()
    # Cluster 1
    sn.add_friendship("Jayesh", "Aarav")
    sn.add_friendship("Aarav", "Rohan")
    sn.add_friendship("Rohan", "Priya")
    # Cluster 2 (isolated)
    sn.add_friendship("Kavita", "Suresh")

    print("Direct friends of Jayesh:", sn.get_direct_friends("Jayesh"))
    print("Friend recommendations for Jayesh:", sn.get_friends_of_friends("Jayesh"))
    print("Social Clusters (Connected Components):", sn.get_connected_components())


if __name__ == "__main__":
    demo()
