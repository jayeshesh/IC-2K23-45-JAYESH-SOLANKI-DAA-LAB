"""Playlist Manager using Circular Linked List.

Course: IC-307D Data Structures & Algorithms LAB
Student: Jayesh Solanki | Roll No: IC-2K23-45
Unit 3: Linked Lists (CO1) Application
"""

from typing import List, Optional


class SongNode:
    """Node representing a track in the playlist."""

    def __init__(
        self,
        title: str,
        artist: str,
        duration_sec: int,
        next_song: Optional["SongNode"] = None,
    ) -> None:
        self.title: str = title
        self.artist: str = artist
        self.duration_sec: int = duration_sec
        self.next: Optional["SongNode"] = next_song


class PlaylistManager:
    """Audio Playlist Manager with continuous cyclic playback using Circular Linked List."""

    def __init__(self) -> None:
        self.head: Optional[SongNode] = None
        self.current_song: Optional[SongNode] = None
        self._count: int = 0

    def __len__(self) -> int:
        return self._count

    def add_song(self, title: str, artist: str, duration_sec: int) -> None:
        """Add song to the end of playlist."""
        new_song = SongNode(title, artist, duration_sec)
        if not self.head:
            new_song.next = new_song
            self.head = self.current_song = new_song
        else:
            tail = self.head
            while tail.next != self.head:  # type: ignore
                tail = tail.next  # type: ignore
            new_song.next = self.head
            tail.next = new_song  # type: ignore
        self._count += 1

    def next_track(self) -> Optional[str]:
        """Advance to next song cyclically."""
        if not self.current_song:
            return None
        self.current_song = self.current_song.next
        return f"Now Playing: '{self.current_song.title}' by {self.current_song.artist}"  # type: ignore

    def current_track(self) -> Optional[str]:
        """Get current song info."""
        if not self.current_song:
            return "Playlist is empty."
        return f"Now Playing: '{self.current_song.title}' by {self.current_song.artist}"

    def list_songs(self) -> List[str]:
        """List all tracks in order."""
        if not self.head:
            return []
        songs = []
        curr = self.head
        idx = 1
        while True:
            songs.append(f"{idx}. {curr.title} - {curr.artist} ({curr.duration_sec}s)")
            curr = curr.next  # type: ignore
            idx += 1
            if curr == self.head:
                break
        return songs


def demo() -> None:
    """Demonstrate playlist manager."""
    pm = PlaylistManager()
    pm.add_song("Imagine", "John Lennon", 183)
    pm.add_song("Bohemian Rhapsody", "Queen", 354)
    pm.add_song("Hotel California", "Eagles", 391)

    print("Playlist Tracks:")
    for track in pm.list_songs():
        print(" ", track)

    print("\nPlayback Simulation:")
    print(" ", pm.current_track())
    print(" ", pm.next_track())
    print(" ", pm.next_track())
    print("  [Looping back to start]")
    print(" ", pm.next_track())


if __name__ == "__main__":
    demo()
