# Все объекты можно поделить на итерируемые и неитерируемые.
# for loop - итерационным протоколом.
# Итерационный протокол включает в себя два метода: iter(), next()


a = 4
b = "Hello world"
c = [1, 2, 3]

for element in c:
    print(element)

res = iter(c)  # iterator of obj, link to obj
try:
    print(next(res))
    print(next(res))
    print(next(res))
    print(next(res))
except StopIteration as err:
    print(err)
    print("End of loop")


# res = iter(a)
# print(res)
