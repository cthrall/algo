import hashlib
import sys

class Hash(object):
    def __init__(self, key):
        key = str(key)
        self._hash = hashlib.md5(key)
        self._digest = self._hash.hexdigest()

class Entry(object):
    def __init__(self, key, value):
        self._hash = Hash(key)
        self._key = key
        self._value = value

class Hashtable(object):
    def __init__(self):
        self._list = []

    def __setitem__(self, key, value):
        entry = Entry(key, value)
        self._list.append(entry)
        self._list.sort(cmp=lambda x, y: cmp(x._hash._digest,
                                            y._hash._digest))

    def __getitem__(self, key):
        h = Hash(key)
        for entry in self._list:
            if entry._hash._digest == h._digest:
                return entry._value

        return None

def main(args):
    t = Hashtable()
    t[3] = 'three'
    t[2] = 'two'
    t[1] = 'one'

    print(t[1])
    print(t[2])
    print(t[3])
    
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))
