class RandomizedSet:

    def __init__(self):
        self.map={}
        self.ml=[]

    def insert(self, val: int) -> bool:
        res=val not in self.map
        if res:
            self.map[val]=len(self.ml)
            self.ml.append(val)
        return res
    


    def remove(self, val: int) -> bool:

        res=val in self.map
        if res:
            idx=self.map[val]
            ls=self.ml[-1]
            self.ml[idx]=ls
            self.ml.pop()
            self.map[ls]=idx
            del self.map[val]
        return res

        

    def getRandom(self) -> int:

        return random.choice(self.ml)
        

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()