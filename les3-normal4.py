def par(a, b, c, d):                                                # Функция определения параллелограмма
    def line(a,b):                                                  # Подфункция вычисления расстояния между точками
        ab = [0,0]
        ab[0] = abs(a[0] - b[0])
        ab[1] = abs(a[1] - b[1])                                    # Находит разницу в координатах и вычисляет расстояние
        r = (ab[0]**2+ab[1]**2)**0.5                                # с помощью теоремы Пифагора
        return r                                                    # Возвращает расстояние
    list = [line(a,b), line(a,c), line(a,d),                        # Создаем список расстояний между всеми точками
            line(b,c), line(b,d), line(c,d)]

    povtor = []
    nepovtor = []
    for n in list:
        if list.count(n) == 1:
            nepovtor.append(n)                                      # Создаем список неповторяющихся длин
        if list.count(n) > 1 and povtor.count(n) == 0:
            povtor.append(n)                                        # и повторяющихся

    # У параллелограмма 2 пары одинаковых сторон. Но они есть не только у параллелограмма, потому сперва отбрасываем
    # похожие варианты.
    # Это может быть квадрат (у квадрата 4 одинаковые стороны и 2 одинаковых перпендикуляра(они длиннее сторон))
    if list.count(min(povtor)) == 4 and list.count(max(povtor)) == 2:
        return "Точки являются вершинами параллелограмма, а если точнее, то КВАДРАТА"
    # Это может быть ромб, у него тоже 4 одинаковые стороны, как у квадрата, но квадрат мы уже отбросили)
    if list.count(max(povtor)) == 4:
        return "Точки являются вершинами параллелограмма, а если точнее, то РОМБА"

    # Также это может быть дельтоид, он отличается от параллелограмма пересечением диагоналей под прямым углом,
    # а значит к нему применима теорема Пифагора. Пытаемся высчитать длину стороны какой-либо пары с помощью теоремы
    # Пифагора, оперируя длиной другой пары одинаковых сторон и длинами перпендикуляров (они не повторяются)...

    nnn = (min(povtor)**2 - (min(nepovtor)/2)**2)**0.5              # отрезок от ближней вершины до пересечения диагоналей
    mmm = (((max(nepovtor)-nnn)**2 + (min(nepovtor)/2)**2))**0.5    # высчитываем длину длинной стороны фигуры
    nnn1 = (max(povtor)**2 - (max(nepovtor)/2)**2)**0.5             # отрезок от дальней вершины до пересечения диагоналей
    mmm1 = (((min(nepovtor)-nnn1)**2+(max(nepovtor)/2)**2))**0.5    # высчитываем длину короткой стороны фигуры

    # И если какая-либо из этих длин совпадает с какой-либо длиной уже высчитанной в начале, значит перпендикуляры
    # пересекаются под прямым углом и это уже не параллелограмм.
    if povtor.count(mmm) > 0 or povtor.count(mmm1) > 0:
        return "Точки НЕ являются вершинами параллелограмма, они являются вершинами ДЕЛЬТОИДА"

    # Имеющие парные стороны фигуры мы уже отбросили, остается ПАРАЛЛЕЛОГРАММ!
    if len(povtor) > 1:
        return "Точки ЯВЛЯЮТСЯ вершинами параллелограмма!"

    # В противном случае это уже не параллелограмм.
    return "Точки НЕ являются вершинами параллелограмма :((("

print(par([1,2],[5,1],[7,3],[3,4]))                 #параллелограмм
print(par([2,-3],[6,-4],[8,-2],[4,-1]))             #параллелограмм
print(par([-7,-2],[-5,-1],[-1,-2],[-5,-3]))         #дельтоид
print(par([1,2],[3,4],[5,1],[7,3]))                 #параллелограмм
print(par([1,1],[4,4],[1,4],[4,1]))                 #квадрат
print(par([0,-1],[-1,1],[0,3],[1,1]))               #ромб
print(par([0,-1],[-1,0],[0,3],[1,1]))               #не пойми что
print(par([1,-2],[4,0],[7,-2],[4,-3]))              #дельтоид

