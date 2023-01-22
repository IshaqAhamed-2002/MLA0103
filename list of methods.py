nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
length = len(nested_list)
print("Length:", length)
concatenation = nested_list + [[10, 11, 12]]
print("Concatenation:", concatenation)
print("Membership:", 3 in [1, 2, 3])
print("Iterations")
for sublist in nested_list:
    for element in sublist:
        print(element,"\t")
index = nested_list[1][2]
print("Indexing:", index)
slice = nested_list[1:]
print("Slicing:", slice)
