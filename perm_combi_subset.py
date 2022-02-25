from itertools import permutations,combinations

ls=[1,2,3]
print("permutation...............................................")
X=permutations(ls)
for i in X:
    print(i)

print("combination...............................................")
Y=combinations(ls,2)
for i in Y:
    print(i)

print("subset.............................................")
for i in range(len(ls)+1):
    for j in range(i):
        print(ls[j:i])
print(".............................................")