def HeightQueue(a):
    a.sort(key=lambda (h, k): (-h, k))
    z = []
    for i in a:
        z.insert(i[1], i)
    print(z)

HeightQueue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]])
HeightQueue([[12,0],[6,3],[3,4],[9,2], [11,1],[1,5]])
HeightQueue([ [2,4], [5,1], [3,3], [1,5], [4,2], [6,0]])