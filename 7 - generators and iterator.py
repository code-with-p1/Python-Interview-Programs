def sqr(n):
    for i in range(1, n+1):
        yield i*i
a = sqr(5)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))

print('***************')

itr_list = iter(['A', 'B', 'C', 'D'])
print(next(itr_list))
print(next(itr_list))
print(next(itr_list))
print(next(itr_list))