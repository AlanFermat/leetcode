from collections import OrderedDict as od
class LRUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.mapping = od()
        self.c = capacity

        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.mapping:
            return -1
        else:
            self.mapping.move_to_end(key)
            return self.mapping[key]

        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.mapping:
            del self.mapping[key]
            self.mapping[key] = value
        else:
            if len(self.mapping) == self.c:
                self.mapping.popitem(False)
            self.mapping[key] = value
            

        
        
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)