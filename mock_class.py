#!/usr/bin/env python


class C3Linearizor(object):
    def extract_good_head(self, ls):
        head = lambda l: l[0]
        tail = lambda l: l[1:]
        is_good = lambda _head, ls: not any(_head in tail(l) for l in ls)
        for l in ls:
            if len(l)==0:
                continue
            elif is_good(head(l), ls):
                h = head(l)
                return h, map(lambda l: [c for c in l if c != h], ls)
        return None, []
    def merge(self, ls):
        merged_lists = []
        while ls is not None and not all(len(l)==0 for l in ls):
            h, ls = self.extract_good_head(ls)
            if h is None: 
                break
            else: 
                merged_lists.append(h)
        return merged_lists
    def linearize(self, c):
        #print('Using C3 Linearization Algorithm')
        ls = [self.linearize(cc) for cc in c.parents] + [c.parents]
        return [c] + self.merge(ls)


class MockClass(C3Linearizor):
    def __init__(self, name, *parents):
        self.name = name
        self.parents = list(parents)
    @property
    def ancestors(self):
        _ancestors = [self]
        if len(self.parents) > 0:
            for cc in self.parents:
                if not cc in _ancestors:
                    _ancestors.extend(cc.ancestors)
        return _ancestors
    def __str__(self):
        fmt_is_child_of = lambda ps: '(' + ', '.join(p.name for p in ps) + ')'
        return self.name + (fmt_is_child_of(self.parents) if self.parents else '')
    def get_mro(self):
        # In Python, the C3 Linearization Algorithm is used to generate the MRO
        # for a subclass. This is the default algorithm used here to generate 
        # the MRO of a MockClass.
        return super(self.__class__, self).linearize(self)
    def mro_names(self):
        return [c.name for c in self.get_mro()]
    def print_mro(self):
        for cname in self.mro_names(): print cname


# To change the linearization algorithm, create a new linearizor class, say the
# right-first depth-first search used in multiple inheritance of traits in
# the Scala language:
class RFDFLinearizor(object):
    def rec_rfds(self, l):
        front = lambda ll: ll[:-1]
        back = lambda ll: ll[-1]
        def inner_rec(il, acc):
            if len(il) == 0:
                return acc
            else:
                return inner_rec(list(filter(lambda c: c!=back(il), front(il))), [back(il)] + acc)
        return inner_rec(l, [])
    def linearize(self, c):
        #print('Using RFDF Linearization Algorithm')
        return self.rec_rfds(c.ancestors)


#...and subclass it along with MockClass:
class RFDFMockClass(RFDFLinearizor, MockClass):
    def __init__(self, name, *parents):
        MockClass.__init__(self, name, *parents)
# Objects of type RFDFMockClass will use the RFDF algorithm to determine their MRO. 

