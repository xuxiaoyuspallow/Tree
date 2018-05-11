"""
ref:
1. https://en.wikipedia.org/wiki/Radix_tree
2. https://medium.com/basecs/compressing-radix-trees-without-too-many-tears-a2e658adb9a0
3. http://www.allisons.org/ll/AlgDS/Tree/PATRICIA/
"""
"""
The following example shows the growth of a PATRICIA tree under a sequence of insertions:

empty           -- initial state

       12345    -- number character positions
insert ababb    -- the key
----> ababb
insert ababa;
search ends at ababb~=ababa;
1st difference is at position 5, so...
----> [5]      -- i.e. test position #5
     .   .
   a.     . b
   .       .
  ababa     ababb
insert ba;
has no position #5;
can skip key positions but must test in order, so...
--------> [1]
         .   .
        .     .
       .       .
    [5]         ba
   .   .
  .     .
 .       .
ababa     ababb
insert aaabba;
search ends at ababb~=aaabba;
can skip key positions but must test in order, so...
--------> [1]
         .   .
        .     .
       .       .
    [2]         ba
   .   .
  .     .
 .       .
aaabba    [5]
         .   .
        .     .
       .       .
      ababa     ababb
insert ab;
ab is also a prefix of ababa and ababb;
must have ability to terminate at an intermediate node, as with Tries.
-------> [1]
        .   .
       .     .
      .       .
    [2]        ba
   .   .
  .     .
 .       .
aaabba   [3]--->ab
         .
        .
       .
      [5]
     .   .
    .     .
   .       .
  ababa     ababb
"""
class Node(object):
    def __init__(self):
        self.value = ""
        self.exist = None


class PatriciaTree(object):
    """
    when redixtree's radix == 2, it is patricia tree,
    which means a patricia tree processes its keys one bit at a time.
    Usually, patricia tree is implemented as bitwise for different usage,
    but this implementation will be string version to understand its theory.

    It may behavior like below:
    >>> d={}
    >>> d['ababb']= {'exist':1}   #insert ababb
    >>> d
    {'ababb': {'exist':1}}
    >>> d['abab']={'a':{'exist':1},'b':{'exist':1}}  #insert ababa
    >>> del d['ababb']
    >>> d
    {'abab': {'a': {'exist':1}, 'b': {'exist':1}}}
    >>> d['ba']= {'exist':1}    # insert ba
    >>> d
    {'ba': {'exist':1}, 'abab': {'a': {'exist':1}, 'b': {'exist':1}}}
    >>> d['a']={'bab':{'a':{'exist':1},'b':{'exist':1}},'aabba':{'exist':1}}  # insert aaabba
    >>> del d['abab']
    >>> d
    {'ba': {'exist':1}, 'a': {'bab': {'a': {'exist':1}, 'b': {'exist':1}}, 'aabba': {'exist':1}}}
    >>> d['a']['b']={'ab':{'a':{'exist':1},'b':{'exist':1}}}   # insert ab
    >>> del d['a']['bab']
    >>> d
    {'ba': {'exist':1}, 'a': {'b': {'ab': {'a': {'exist':1}, 'b': {'exist':1}}}, 'aabba': {'exist':1}}}

    """
    def __init__(self):
        self.tree ={}

    def insert(self,word,tree):
        # if not word:
        #     return tree
        # if not tree or (len(tree)==1 and tree.get('exist')):
        #     if tree.get('exist'):
        #         del tree['exist']
        #     tree[word] = {'exist': 1}
        #     return tree
        for value in tree:
            if not value.startswith(word[0]):
                continue
            for i in range(len(word)):
                if value.startswith(word[:len(word)-i]):
                    tree[word[:len(word)-i]] = self.helper2(value[len(word)-i:],tree[value])
                    tree[word[:len(word)-i]].update(self.helper(word[len(word)-i:],tree[word[:len(word)-i]]))
                    del tree[value]
                    return tree
        tree[word] = {'exist':1}
        return tree

    def helper(self,word,tree):
        if not word:
            return tree
        if not tree or (len(tree)==1 and tree.get('exist')):
            if tree.get('exist'):
                del tree['exist']
            tree[word] = {'exist': 1}
            return tree
        elif len(tree) >= 1 and not tree.get('exist'):
            # res = {}
            # res[word] = tree
            # return res
            tree[word] = {'exist':1}
            return tree

    def helper2(self,word,tree):
        res = {}
        res[word] = tree
        return res

    def search(self,word,tree):
        for i in range(len(word)):
            if word[:len(word)-i] in tree:
                if tree[word[:len(word)-i]].get('exist') and i == 0:
                    return True
                return self.search(word[len(word)-i:],tree[word[:len(word)-i]])
        return False

if __name__ == '__main__':
    obj = PatriciaTree()
    # obj.tree =  {'ba': {'exist':1}, 'a': {'bab': {'a': {'exist':1}, 'b': {'exist':1}}, 'aabba': {'exist':1}}}
    # print(obj.search('ababbb',obj.tree))
    obj.insert('ababba',obj.tree)
    obj.insert('ababaa',obj.tree)
    obj.insert('ab',obj.tree)
    obj.insert('ba',obj.tree)
    obj.insert('aaabba',obj.tree)
    obj.insert('ab',obj.tree)
    print(obj.tree)

