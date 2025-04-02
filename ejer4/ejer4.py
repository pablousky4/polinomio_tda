#restar 
def restar_polinomios(polinomio1, polinomio2):
    resultado = []
    
    polinomio2 = polinomio2[:]
    for coef1, exp1 in polinomio1:
        encontrado = False
        for i, (coef2, exp2) in enumerate(polinomio2):
            if exp1 == exp2:
                resultado.append((coef1 - coef2, exp1))
                polinomio2.pop(i)  # Marcar como procesado
                encontrado = True
                break
        if not encontrado:
            resultado.append((coef1, exp1))

    polinomio2 = [term for term in polinomio2 if term is not None]

    for coef2, exp2 in polinomio2:
        resultado.append((-coef2, exp2))
    
    resultado.sort(key=lambda x: x[1], reverse=True)
    
    return resultado

#dividir
def dividir_polinomios(polinomio1, polinomio2):
    cociente = []
    polinomio1 = sorted(polinomio1, key=lambda x: x[1], reverse=True)
    divisor = sorted(polinomio2, key=lambda x: x[1], reverse=True)
    
    while polinomio1 and polinomio1[0][1] >= polinomio2[0][1]:
        coef1, exp1 = polinomio1[0]
        coef2, exp2 = divisor[0]
        
        coef_cociente = coef1 / coef2
        exp_cociente = exp1 - exp2
        
        cociente.append((coef_cociente, exp_cociente))
        
        subtraccion = [(coef_cociente * coef, exp_cociente + exp) for coef, exp in divisor]
        polinomio1 = restar_polinomios(polinomio1, subtraccion)

        if not polinomio1 or polinomio1[0][1] < polinomio2[0][1]:
            pass
    
    return cociente

#eliminar
def eliminar_termino(polinomio, coeficiente, exponente):
    return [t for t in polinomio if t != (coeficiente, exponente)]

#verificar
def existe_termino(polinomio, coeficiente, exponente):
    return (coeficiente, exponente) in polinomio

#hago esto para ejecutar todo desde el main
def polinomios():
    polinomio1 = [(3, 2), (2, 1), (1, 0)]  # 3x^2 + 2x + 1
    polinomio2 = [(1, 2), (-4, 1), (4, 0)]  # x^2 - 4x + 4

    # Resta
    resultado_resta = restar_polinomios(polinomio1, polinomio2)
    print("p1:", polinomio1, "-p2:", polinomio2)
    print("Resultado de la resta:", resultado_resta)

    # División
    #resultado_division = dividir_polinomios(polinomio1, polinomio2)
    #print("Resultado de la división:", resultado_division)

    # Eliminar término
    try:
        coef_eliminar = float(input("Introduce el coeficiente del término a eliminar: "))
        exp_eliminar = int(input("Introduce el exponente del término a eliminar: "))
        polinomio_sin_termo = eliminar_termino(polinomio1, coef_eliminar, exp_eliminar)
        print(f"Polinomio sin el término {coef_eliminar}x^{exp_eliminar}:", polinomio_sin_termo)
    except ValueError:
        print("Error: Entrada inválida. Asegúrate de ingresar un número válido.")

    # Verificar término
    try:
        coef_verificar = float(input("Introduce el coeficiente del término a verificar: "))
        exp_verificar = int(input("Introduce el exponente del término a verificar: "))
        existe = existe_termino(polinomio1, coef_verificar, exp_verificar)
        print(f"¿Existe el término {coef_verificar}x^{exp_verificar} en el polinomio 1?", existe)
        existe1 = existe_termino(polinomio1, coef_verificar, exp_verificar)
        print(f"¿Existe el término {coef_verificar}x^{exp_verificar} en el polinomio 2?", existe1)
    except ValueError:
        print("Error: Entrada inválida. Asegúrate de ingresar un número válido.")