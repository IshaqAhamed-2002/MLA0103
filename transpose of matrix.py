a=[[1,2],[3,4],[5,6]]
print("Given matrix : ")
for y in a:
    print(y)

x=[[0,0,0],[0,0,0]]
for i in range(len(a)):
    for j in range(len(a[0])):
        x[j][i]=a[i][j]

print("Transpose of matrix :")
for k in x:
    print(k)
