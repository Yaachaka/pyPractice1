"""
bhch07exrc03.py: Start with the list [8,9,10]. Do the following:
(a) Set the second entry (index 1) to 17
(b) Add 4, 5, and 6 to the end of the list
(c) Remove the first entry from the list
(d) Sort the list
(e) Double the list
(f) Insert 25 at index 3
The final list should equal [4,5,6,25,10,17,4,5,6,10,17]
"""
print('*'*80)

list = [8, 9, 10]
print('list:', list)
list.insert(1, 17)
print('(a) Insertion at index 1:', list)
list = list + [4, 5, 6]
print('(b) Appending elements:', list)
list = list[1:]
print('(c) First entry of the list removed:', list)
list.sort()
print('(d) List sorted:', list)
list = list * 2
print('(e) list doubled:', list)
list.insert(3, 25)
print('(f) Insert 25 at index 3:', list)

print('*'*80)
"""PROGRAM OUTPUT
********************************************************************************
list: [8, 9, 10]
(a) Insertion at index 1: [8, 17, 9, 10]
(b) Appending elements: [8, 17, 9, 10, 4, 5, 6]
(c) First entry of the list removed: [17, 9, 10, 4, 5, 6]
(d) List sorted: [4, 5, 6, 9, 10, 17]
(e) list doubled: [4, 5, 6, 9, 10, 17, 4, 5, 6, 9, 10, 17]
(f) Insert 25 at index 3: [4, 5, 6, 25, 9, 10, 17, 4, 5, 6, 9, 10, 17]
********************************************************************************
"""