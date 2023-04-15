liste = [[1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]]
tümü = []
for i in liste:
    for z in i:
        tümü += [z]
print(tümü)


"""
liste = [[1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]]
tümü = [z for i in liste for z in i]
print(tümü)

liste üreteciyle daha kolay ama daha zor okunuyor
"""
