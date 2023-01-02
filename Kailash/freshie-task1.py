class solve():
    def __init__(self, lst, s):
        self.nlist = lst
        self.d = {}
        self.ct = 0
        self.s = s
    def find(self):
        for i in range(0, len(self.nlist)):
            for j in range(0, len(self.nlist)):
                if self.nlist[i] + self.nlist[j] == self.s:
                    self.d[self.ct] = [i, j]
                    self.ct += 1
        print(self.d)


j = solve([10,20,10,40,50,60,70],50)
j.find()
