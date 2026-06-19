# Tuples

# Collection of different data types wich is ordered and unchangable(immutable). Tpl (). Once a tuple is created
# we cannot change its values. Unlike lists, tuple has few methods.:

# to create: 

tuple1 = tuple('item1', 'item2', 'item3')

# to count: 

print(tuple1.count())

# to find the index of a specified item in a tuple

print(tuple1.index(1)) # or 

print(tuple1[1])


# to join two or more tuples and create a new tuple

tuple2 = tuple('item4', 'item5', 'item6')

joinedtuple = tuple1 + tuple2

# we can change tuples to list

lst = list(joinedtuple)

# its not possible to delete items from tuples, but we can delete the entire tuple using del 'tuple name'
