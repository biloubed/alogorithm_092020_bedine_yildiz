class FibonacciHeap:
    def __init__(self,tree):
        self.tree   = []
        self.branch = []
        self.order  = 0


    def insert(self, value):
        i = 0
        while i <= len(self.tree):
            self.branch.append(value)
            self.tree.append(self.branch)
            break
        return self.tree

    def find_min(self):
        array_min = []
        for val in self.tree:
            print(val[2])
        #     array_min.append(val[0])
        #     array_min.append(val[1])
        # print(array_min)


    # def delete_min(self):
    #     smallest = self.least
    #     if smallest is not None:
    #         for child in smallest.child:
    #             self.trees.append(child)
    #         self.trees.remove(smallest)
    #         if self.trees == []:
    #             self.least = None
    #         else:
    #             self.least = self.trees[0]
    #             self.consolidate()
    #         self.count = self.count - 1
    #         return smallest.value
    #
    #
    # def merge(self, fibonnaci_heap):
    #     aux = (floor_log(self.count) + 1) * [None]
    #
    #     while self.trees != []:
    #         x = self.trees[0]
    #         order = x.order
    #         self.trees.remove(x)
    #         while aux[order] is not None:
    #             y = aux[order]
    #             if x.value > y.value:
    #                 x, y = y, x
    #             x.add_at_end(y)
    #             aux[order] = None
    #             order = order + 1
    #         aux[order] = x
    #
    #     self.least = None
    #     for k in aux:
    #         if k is not None:
    #             self.trees.append(k)
    #             if (self.least is None
    #                     or k.value < self.least.value):
    #                 self.least = k

tab = []
test = FibonacciHeap(tab)
a    = test.insert(1)

# c    = test.find_min()
print(a)
