class FibonacciHeap:
    def __init__(self,tree):
        self.trees  = []

    def insert(self, value):
        i = 0
        while i <= len(self.trees):
            self.trees.append([value])
            break
        return self.trees


    def find_min(self):
        array_min = []
        for val in self.trees:
            array_min.append(val)
        a = sorted(array_min)
        return a[0]


    def delete_min(self):
        x = self.find_min()
        for v in self.trees:
            if x == v:
                print(v)
                min = v
                self.trees.remove(v)
                print("le minimum est suprimer")
                return min[0]

    def merge(self):
        delete = self.delete_min()
        print(delete)
        print(self.trees)
        for value in self.trees:
            if value:
                pass




tab = []
test = FibonacciHeap(tab)
a = test.insert(123)
b = test.insert(3)
c = test.insert(34)
d = test.insert(0)
p = test.merge()
