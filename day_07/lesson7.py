# Sets

# A set is a collection of unordered and un-indexed distinct elements. In Python we use it to store uniqe items
# and it is possible to find the union, intersection, difference, symmetric difference, subset, super set and 
# disjoint set among sets.

# To create

st = set()
st1 = {'item1', 'item2', 'item3'}

# We can access sets with loops

# To add items to a set we use:

st1.add('item4')

# To add multiple items we use:

st1.update(['item5','item6','item7'])

# To remove items from a set we use remove:

st1.remove(['item6'])

# We can use pop to remove a random item:

st1.pop()

# If we want to know wich item was removed we can assign the value:

removed_item = st1.pop()