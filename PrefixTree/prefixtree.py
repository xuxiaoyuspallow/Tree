class Trie(object):
    def __init__(self):
        self.tree = {}

    def insert(self,word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        tree = self.tree
        for c in word:
            if c not in tree:
                tree[c] = {}
            tree = tree[c]
        tree['exist'] = True

    def search(self,word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        :param word:
        :return:
        """
        tree = self.tree
        for c in word:
            if c not in tree:
                return False
            tree = tree[c]
        return tree.get('exist')

    def startswith(self,prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        :param prefix:
        :return:
        """
        tree = self.tree
        for c in prefix:
            if c not in tree:
                return False
            tree = tree[c]
        return True


def test():
    trie = Trie()
    trie.insert('hello')
    trie.insert('world')
    assert trie.search('hello')
    assert trie.search('world')
    assert not trie.search('hell')
    assert not trie.search('hellop')
    assert not trie.search('worl')
    assert not trie.search('worlda')
    assert trie.startswith('hello')
    assert trie.startswith('hell')
    assert trie.startswith('he')
    assert trie.startswith('wor')
    assert trie.startswith('world')
    assert not trie.startswith('world!')
    assert not trie.startswith('hellow')

if __name__ == '__main__':
    test()