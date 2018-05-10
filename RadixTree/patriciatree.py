"""
ref:
1. https://en.wikipedia.org/wiki/Radix_tree
2. https://medium.com/basecs/compressing-radix-trees-without-too-many-tears-a2e658adb9a0
"""

class PatriciaTree(object):
    """
    when redixtree's radix == 2, it is patricia tree,
    which means a patricia tree processes its keys one bit at a time.
    """
    def __init__(self):
        self.tree ={}

    def decode_binary(self,char):
        """
        decode string to binay string
        :rtype:str
        """
        return bin(ord(char))[2:]

