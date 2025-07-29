

def generator(n=0, maximum=10):
    while True:
        yield n
        n += 1

        if n > maximum:
            return


gen = generator(maximum=20)
for n in gen:
    print(n)


# Yield From

def gen1():
    yield 1
    yield 2
    yield 3


def gen2():
    yield from gen1()
    yield 4
    yield 5
    yield 6


g = gen2()
for numero in g:
    print(numero)
