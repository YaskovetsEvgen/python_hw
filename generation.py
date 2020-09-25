""" Написать генератор, который при каджом обращении к нему генерирует
элемент последовательности 1, 2, 3, 4, 5, 6... 
но ! если генерируемый элемент делится на 3 без остатка - возвращает 
вместо него "Василий" """
def gen_func():
    for i in (1, 2, 3, 4, 5, 6, 7, 8):
        if i % 3 == 0 :
            yield "Василий"
        else :
            yield i 
       
s = gen_func()

print(next(s))
print(next(s))
print(next(s))
print(next(s))
print(next(s))
print(next(s))
print(next(s))
print(next(s))