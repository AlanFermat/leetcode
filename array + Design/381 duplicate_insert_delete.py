import random
class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = {}
        self.storage= []
        

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        self.storage.append(val)
        if self.dict.get(val, -1) == -1:
            self.dict[val] = [len(self.storage) - 1]
            return True
        else:
            self.dict[val].append(len(self.storage) - 1)
            return False
            
        

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if self.dict.get(val, -1) != -1:
            last_num = self.storage[-1] # exchange it with the last element in the list
            # just delete the last_num
            if val == last_num:
                if self.dict[val][0] < self.dict[val][-1]:
                    self.dict[val].pop()
                else:
                    self.dict[val].pop(0)
                self.storage.pop()
                if not self.dict[val]:
                    self.dict[val] = -1
            # exchange then delete
            else:
                idx = self.dict[val].pop() # get the idx of item to be deleted
                if self.dict[last_num][-1] >= self.dict[last_num][0]:
                    self.dict[last_num].pop()
                    if self.dict[last_num]:
                        if self.dict[last_num][0] < idx:
                            self.dict[last_num].insert(0, idx)
                        else:
                            self.dict[last_num].insert(1, idx)
                    else:
                        self.dict[last_num].append(idx)
                else:
                    self.dict[last_num].pop(0)
                    if self.dict[last_num]:
                        if self.dict[last_num][0] < idx:
                            self.dict[last_num].insert(0, idx)
                        else:
                            self.dict[last_num].insert(1, idx)
                    else:
                        self.dict[last_num].append(idx)
                self.storage[idx] = last_num
                self.storage.pop()
                if not self.dict[val]:
                    self.dict[val] = -1
            return True
        return False
        
        

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        return random.choice(self.storage)
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()