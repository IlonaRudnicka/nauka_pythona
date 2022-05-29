# importujemy modul i nadajemy mu alias
from mytoolkit import matematyczny as mat
from mytoolkit import pomocniczy as pom #j.w. tylko dla drugiego modulu

# wywolanie funkcji/metod z mytoolkit/matematyczny (alias 'mat')
print(mat.dodaj(4,14))
print(mat.odejmij(10,5))

# wywolanie funkcji/metody z mytoolkit/pomocniczy (alias 'pom')
pom.czesc()
