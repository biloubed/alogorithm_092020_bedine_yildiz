# Creating fibonacci tree
class FibonacciTree:
    def __init__(self, value):
        self.value = value
        self.child = []
        self.order = 0

    # Adding tree at the end of the tree
    def add_at_end(self, t):
        self.child.append(t)
        self.order = self.order + 1

class FibonacciHeap:
    def insert(self, value):
        new_tree = FibonacciTree(value)
        self.trees.append(new_tree)
        if (self.least is None or value < self.least.value):
            self.least = new_tree
        self.count = self.count + 1


    def find_min(self):
        if self.least is None:
            return None
        return self.least.value

    def delete_min(self):
        smallest = self.least
        if smallest is not None:
            for child in smallest.child:
                self.trees.append(child)
            self.trees.remove(smallest)
            if self.trees == []:
                self.least = None
            else:
                self.least = self.trees[0]
                self.consolidate()
            self.count = self.count - 1
            return smallest.value


    def merge(self, fibonnaci_heap):
        aux = (floor_log(self.count) + 1) * [None]

        while self.trees != []:
            x = self.trees[0]
            order = x.order
            self.trees.remove(x)
            while aux[order] is not None:
                y = aux[order]
                if x.value > y.value:
                    x, y = y, x
                x.add_at_end(y)
                aux[order] = None
                order = order + 1
            aux[order] = x

        self.least = None
        for k in aux:
            if k is not None:
                self.trees.append(k)
                if (self.least is None
                        or k.value < self.least.value):
                    self.least = k


# arbre = []
# # arbre.append("bannae")
# # arbre.append("kiwi")
# # print(arbre)
# object = FibonacciHeap()
# object.insert(arbre,2)
# print(object)

fibonacci_heap = FibonacciHeap()
fibonacci_heap.insert(7)
fibonacci_heap.insert(3)
fibonacci_heap.insert(17)
fibonacci_heap.insert(24)
