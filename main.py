import random

def rezolvare (incercari):
    for persoane in range (2,366):
        if (probabilitate(persoane,incercari)>= 0.5):
            return persoane

for k in range (1,6):
    incercari= 10**k
    print(k,rezolvare(incercari))

def probabilitate(nr_persoane_in_camera, incercari):
    succes =0
    for incercare in range(incercari):
        if incercariReusite(nr_persoane_in_camera) ==True:
            succes +=1

    return  1.0 *succes /incercari

def incercariReusite(nr_persoane_in_camera):
    zile_atribuite= set()
    for persoana in range (nr_persoane_in_camera):
        ziua = random.randint(1, 365)
        if (ziua in zile_atribuite):
            return True
        zile_atribuite.add(ziua)
    return False




