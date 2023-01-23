from random import shuffle
class Sort:
    
    def __init__(self, N):
        self._list = [x for x in range(N)]
        shuffle(self._list)
        
    def first(self):
        return self._list[0]
    
    def second(self):
        return self._list[1]
    
    def swap_top_two(self):
        self._list[0], self._list[1] = self._list[1], self._list[0]
        
    def move_first_to_bottom(self):
        first = self._list.pop(0)
        self._list.append(first)
            
    def size(self):
        return len(self._list)
        
    def sort(self):
        # Rules
        # You may not access the list directly
        # You may only call the other methods in the class
        # first, second, swap_top_two, move_first_to_bottom, size
        # Indicate the time complexity of your algorithm
        for i in range(self.size()):
            for _ in range(self.size() - i - 1):
                if self.first() <= self.second():
                    self.move_first_to_bottom()
                else:
                    self.swap_top_two()
                    self.move_first_to_bottom()
            for _ in range(i + 1):
                self.move_first_to_bottom()
        pass
    # time complexity = O(N^2)
    # auxiliary memory = O(1)

    def is_sorted(self):
        for i in range(self.size()-1):
            if self._list[i] > self._list[i+1]:
                return False
        return True
    
    def __repr__(self):
        return str(self._list)
        
c = Sort(20)
print("BEFORE:", c)       
print() 
 
c.sort()
print("AFTER:", c)       

print(c.is_sorted())  
