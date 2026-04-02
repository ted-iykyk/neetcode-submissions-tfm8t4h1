class MyHashMap:

    def __init__(self):
        self.hashmap = [[]] * 10000000

    def put(self, key: int, value: int) -> None:
        print(key, value)
        if len(self.hashmap[key]):
            print("exists", self.hashmap[key])
            self.hashmap[key][0] = value
            
        else:
            print("not exists", self.hashmap[key])
            self.hashmap[key] = [value]
        print(self.hashmap[key])

    def get(self, key: int) -> int:
        print(self.hashmap[key], key)
        if len(self.hashmap[key]):
            return self.hashmap[key][0]
        return -1
        

    def remove(self, key: int) -> None:
        self.hashmap.pop(key)
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)