from timeit import Timer

# =========================================================================
# Testing a list created by range.
def test1(n):
    s = 0
    for i in range(n):
        s += i
    return s

def test2(n):
    return sum(range(n))

# Timing test1() function
t1 = Timer("test1(10000)", "from __main__ import test1")
print(f"test1(): {t1.timeit(number=1000)} milliseconds")

# Timing test2() function
t2 = Timer("test2(10000)", "from __main__ import test2")
print(f"test2(): {t2.timeit(number=1000)} milliseconds")

# Output:
# test1(): 0.16868586899363436 milliseconds
# test2(): 0.06680456700269133 milliseconds


# ===============================================================
# Testing list creation versions of 1000 elements

def test1():
    l = []
    for i in range(1000):
        l = l + [i]

def test2():
    l = []
    for i in range(1000):
        l.append(i)

def test3():
    l = [i for i in range(1000)]

def test4():
    l = list(range(1000))

t1 = Timer("test1()", "from __main__ import test1")
print(f"concatenation: {t1.timeit(number=1000):15.3f} milliseconds")
t2 = Timer("test2()", "from __main__ import test2")
print(f"appending: {t2.timeit(number=1000):19.3f} milliseconds")
t3 = Timer("test3()", "from __main__ import test3")
print(f"list comprehension: {t3.timeit(number=1000):10.3f} milliseconds")
t4 = Timer("test4()", "from __main__ import test4")
print(f"list range: {t4.timeit(number=1000):18.3f} milliseconds")
print(type(range(1000)))
l=[0,2,3,4,5,6,7,8,9]
l[1:5] = [2,3,4]
print(l)

# Output:
# concatenation:            0.59 milliseconds
# appending:                0.02 milliseconds
# list comprehension:       0.01 milliseconds
# list range:               0.01 milliseconds


# ===================================
import timeit
import random

print(f"{'n':10s}{'list':>10s}{'dict':>10s}")
for i in range(10_000, 1_000_001, 20_000):
    t = timeit.Timer(f"random.randrange({i}) in x",
    "from __main__ import random, x")
    x = list(range(i))
    lst_time = t.timeit(number=1000)
    x = {j: None for j in range(i)}
    dict_time = t.timeit(number=1000)
    print(f"{i:<10,}{lst_time:>10.3f}{dict_time:>10.3f}")