class ADictMeta(type):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.mydict = {}

    def __delitem__(self, key):
        del self.mydict[key]

    def __setitem__(self, key, value):
        self.mydict[key] = value

    def __getitem__(self, key):
        return self.mydict[key]

    def clear(self):
        self.mydict.clear()

    def pop(self, *args, **kwargs):
        return self.mydict.pop(*args, **kwargs)

    def popitem(self):
        return self.mydict.popitem()

    def setdefault(self, *args, **kwargs):
        return self.mydict.setdefault(*args, **kwargs)

    def update(self, *args, **kwargs):
        self.mydict.update(*args, **kwargs)

    def __contains__(self, key):
        return key in self.mydict

    def get(self, *args, **kwargs):
        return self.mydict.get(*args, **kwargs)

    def items(self):
        return self.mydict.items()

    def keys(self):
        return self.mydict.keys()

    def values(self):
        return self.mydict.values()

    def __len__(self):
        return len(self.mydict)

    def __iter__(self):
        return iter(self.mydict)

class Adict(metaclass=ADictMeta):
    pass

Adict['foo'] = '42'
print(dict(Adict))
print({**Adict, 'key2': 'value2'})

d = Adict
d.setdefault("bar", 43)
print({**Adict}) 

d.get(Adict)
print({**Adict})