class NaveEspacial:
    def __init__(self, nombre, longitud, tripulantes, pasajeros):
        self.nombre = nombre
        self.longitud = longitud
        self.tripulantes = tripulantes
        self.pasajeros = pasajeros

    def __repr__(self):
        return f"Nave: {self.nombre}, Longitud: {self.longitud}m, Tripulantes: {self.tripulantes}, Pasajeros: {self.pasajeros}"

def naves():
    naves = [
        NaveEspacial("Mercedes E63", 5, 4, 3),
        NaveEspacial("Cometa Veloz", 200, 5, 50),
        NaveEspacial("Titán del Cosmos", 300, 6, 100),
        NaveEspacial("Estrella Fugaz", 250, 7, 60),
        NaveEspacial("GX-200", 150, 4, 80),
        NaveEspacial("GX-300", 180, 5, 120),
        NaveEspacial("Nebulosa Rápida", 220, 6, 45),
        NaveEspacial("Halcon Estelar", 350, 8, 200),
        NaveEspacial("Aguja Galáctica", 280, 6, 150),
        NaveEspacial("Explorer-X", 210, 4, 30),
        NaveEspacial("BMW M4", 5, 4, 3)
    ]

    naves_ordenadas = sorted(naves, key=lambda x: (x.nombre, -x.longitud))
    print("Naves ordenadas por nombre ascendente y longitud descendente:")
    for nave in naves_ordenadas:
        print(nave)

    print("\nInformación de la nave 'Cometa Veloz' y 'Titán del Cosmos':")
    for nave in naves:
        if nave.nombre in ["Cometa Veloz", "Titán del Cosmos"]:
            print(nave)

    naves_mayores_pasajeros = sorted(naves, key=lambda x: x.pasajeros, reverse=True)[:5]
    print("\nLas cinco naves con mayor cantidad de pasajeros:")
    for nave in naves_mayores_pasajeros:
        print(nave)

    nave_mayor_tripulacion = max(naves, key=lambda x: x.tripulantes)
    print("\nLa nave que requiere la mayor cantidad de tripulación:")
    print(nave_mayor_tripulacion)

    print("\nNaves cuyo nombre comienza con 'GX':")
    for nave in naves:
        if nave.nombre.startswith("GX"):
            print(nave)
    
    print("\nNaves que pueden llevar seis o más pasajeros:")
    for nave in naves:
        if nave.pasajeros >= 6:
            print(nave)


    #Mostrar info
    nave_mas_pequena = min(naves, key=lambda x: x.longitud)
    nave_mas_grande = max(naves, key=lambda x: x.longitud)
    print("\nNave más pequeña y más grande:")
    print(f"Nave más pequeña: {nave_mas_pequena}")
    print(f"Nave más grande: {nave_mas_grande}")