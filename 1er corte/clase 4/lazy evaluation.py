# range
nums = range(1, 1_000_000)
print(nums)        # range(0, 1000000)
print(nums[0])     # 0
print(nums[999999])# 999999

# generators
def cuadrados():
    for n in range(1, 5):
        yield n * n

gen = cuadrados()
print(next(gen)) # 1
print(next(gen)) # 4
print(list(gen)) # [9, 16]


#generatos expression
# Lista por comprensión (evaluación estricta)
nums = [x*x for x in range(5)]
print(nums)  # [0, 1, 4, 9, 16]

# Generador (evaluación perezosa)
nums_lazy = (x*x for x in range(5))
print(nums_lazy)         # <generator object ...>
print(list(nums_lazy))   # [0, 1, 4, 9, 16]

#uso con map, filter, itertools
nums = [1, 2, 3, 4, 5]

# map devuelve un generador perezoso
dobles = map(lambda x: x*2, nums)

print(dobles)        # <map object ...>
print(list(dobles))  # [2, 4, 6, 8, 10]
