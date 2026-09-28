class Numbers  :
    def __init__(self,max):
        self.current = 1
        self.max = max

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.max :
            value = self.current
            self.current+=1
            return value
        else :
            return "maximumm........."

nums = Numbers(5)
print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))
