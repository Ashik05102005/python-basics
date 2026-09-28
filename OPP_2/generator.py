def numbers ():
    yield 1
    yield 2
    yield 3

nums = numbers()
print(next(nums))
print(next(nums))
# print(next(nums))
print(next(nums))
