def mover_piedras(n, origen, destino, auxiliar):
    if n==1:
        print(f"Muevo la piedra de {origen} a {destino}")
        return
    
    #muevo n-1 piedras usando auxiliar
    mover_piedras(n-1, origen, auxiliar, destino)
    print(f"Muevo la piedra de {origen} a {destino}")
    mover_piedras(n-1, auxiliar, destino, origen)

def resolver_puzzle():
    num_piedras = 5 #si se le pone 74 como el ejercicio dice, explota
    print("Inicio el traslado de piedras")
    mover_piedras(num_piedras, 'A', 'C', 'B')
    print("Puzzle resuelto!")
