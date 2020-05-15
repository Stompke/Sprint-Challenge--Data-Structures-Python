import time
from bst_for_names import BSTNode

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)
# < --- MY CODE --->
names_1_bst = BSTNode(names_1[0])
names_2_bst = BSTNode(names_2[0])

for name_1 in names_1:
    if name_1 is not names_1[0]:
        names_1_bst.insert(name_1)

for name_2 in names_2:
    if name_2 is not names_2[0]:
        names_2_bst.insert(name_2)

for name_1 in names_1:
    if(names_2_bst.contains(name_1)):
        duplicates.append(name_1)



# print("NAMES 1")

# print("Root :", names_1_bst.value)
# print("Left :", names_1_bst.left.value)
# print("Right :", names_1_bst.right.value)
# print("Right > Left :", names_1_bst.right.left.value)
# print("Left > Right :", names_1_bst.left.right.value)

# print("NAMES 2")

# print("Root :", names_2_bst.value)
# print("Left :", names_2_bst.left.value)
# print("Right :", names_2_bst.right.value)
# print("Right > Left :", names_2_bst.right.left.value)
# print("Left > Right :", names_2_bst.left.right.value)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
