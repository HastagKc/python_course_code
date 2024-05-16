#set --it is collection data item(data structure) which is mutable,unorder,donot allow duplicate value
# a={"sujan",12,2.2}
a={5,4,6,3,2,1,3,3,3,99,77}

# a={3,1,4,6}
# print(a[0])
# print(type(a))
# print(a)

# a.add(2)
# a.update([6,88,44])

# a.clear()
# del a
# a.pop()
# a.remove(9)
# a.discard(9)

# a={1,2,3,4,5}
# b={2,4,6,8}

# a.update(b)
# c=a.union(b)
# c=a.intersection(b)
# c=b.difference(a)
# c=a.isdisjoint(b)
# c=a.issuperset(b)
# c=b.issubset(a)
# c=a.symmetric_difference(b)
# print(c)

# print(a.difference_update(b))
# a.difference_update(b)
# print(a)

a=frozenset({1,2,3,4})
print(a)
print(type(a))

b=a.difference({1,2,5,6})
print(b)
