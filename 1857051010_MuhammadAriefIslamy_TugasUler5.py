def isPerfect(x):
    faktor = []
    for i in range(1, x):
        if x % i == 0:
            temp = i
            faktor.append(temp)
    if x == sum(faktor):
        print("YES")
    else:
        print("NO")


K = int(input())
T = []
for i in range(K):
    T.append(input())

for i in range(K):
    isPerfect(int(T[i]))