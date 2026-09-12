# Last updated: 9/12/2026, 10:23:22 AM
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class StreamChecker:

    def __init__(self, words):
        self.root = TrieNode()
        self.stream = []

        # build reversed trie
        for word in words:
            node = self.root
            for ch in reversed(word):
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.is_end = True

    def query(self, letter):
        self.stream.append(letter)

        node = self.root

        # traverse stream backwards
        for ch in reversed(self.stream):
            if ch not in node.children:
                return False

            node = node.children[ch]

            if node.is_end:
                return True

        return False