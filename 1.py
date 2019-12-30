#!/usr/bin/env python
# coding=utf-8
for i in xrange(1, 100):
    print i,

list_a = range(1, 100)
print list_a

list_b = range(1, 5)
list_c = range(6, 10)

list_b.append(6)
list_c.append(7)

list_b.insert(1, [1, 2, 3])

list_b.extend(list_c)

del list_b[4]
list_b.pop(1)


print list_b
print list_c

list_d = range(1, 10, 2)
print list_d

