class MyHashMap:

    def __init__(self):
        self.hashmap = [[]] * 1000001

    def put(self, key: int, value: int) -> None:
        if len(self.hashmap[key]):
            self.hashmap[key][0] = value
            
        else:
            self.hashmap[key] = [value]
        print(self.hashmap[key])

    def get(self, key: int) -> int:
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