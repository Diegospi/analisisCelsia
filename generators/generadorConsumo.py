import random
def generarDatos():
    datos = []
    for i in range(5000):
        dato={}
        id=random.randint(1,10000)
        referencia=random.choice(["ACH01","ACH22","ACH43"])
        marca=random.choice(["Sony","Rico","Kalley","-"])
        capacidad=random.randint(100,2000)
        ciudad=random.choice(["Medellin","Bello","Itagui","Sabaneta","Niquia","sin","nan"])
        responsable=random.choice(["Mauro Yepes","Wilson Yepes","Santiago Yepes","Sonia Yepes","Tattiana Yepes"])

        dato=[id,referencia,marca,capacidad,ciudad,responsable]
        datos.append(dato)
    return datos

print(generarDatos())
