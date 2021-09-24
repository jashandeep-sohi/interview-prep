"""
>>> replace(["cat","bat","rat"], "the cattle was rattled by the battery")
'the cat was rat by the bat'

>>> replace(["a","b","c"], "aadsfasf absbs bbab cadsfafs")
'a a b c'

>>> replace(["a", "aa", "aaa", "aaaa"], "a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa")
'a a a a a a a a bbb baba a'

>>> replace(["catt","cat","bat","rat"], "the cattle was rattled by the battery")
'the cat was rat by the bat'

>>> replace(["ac","ab"], "it is abnormal that this solution is accepted")
'it is ab that this solution is ac'

>>> t = Trie()
>>> t.add("hello")
>>> t.add("hell")
>>> t.add("help")
>>> t.add("helm")
>>> list(t.subwords())

"""

import collections

class Trie(object):

    def __init__(self):
        self.word = False
        self.children: dict[str, Trie] = collections.defaultdict(lambda: Trie())

    def __repr__(self):
        return repr(dict(self.children))

    def add(self, word):
        node = self
        for c in word:
            node = node.children[c]

        node.word = True

    def subwords(self):
        for c, n in self.children.items():
            if n.word:
                yield c

            for x in n.subwords():
                yield c + x

    def find(self, word):
        node = self
        for c in word:
            if c not in node.children:
                return None
            node = node.children[c]

        return node


    def smallest_match(self, word):
        node = self
        chars = []
        for c in word:
            if c not in node.children:
                return None

            node = node.children[c]
            chars.append(c)

            if node.word:
                return "".join(chars)

        return None



def replace(dictionary, sentence):
    t = Trie()

    for word in dictionary:
        t.add(word)

    new = []
    for word in sentence.split():
        m = t.smallest_match(word)

        if m is not None:
            new.append(m)
        else:
            new.append(word)

    return " ".join(new)
