#restar 
def restar_polinomios(polinomio1, polinomio2):
    resultado = []
    
    polinomio2 = polinomio2[:]
    for coef1, exp1 in polinomio1:
        encontrado = False
        for i, (coef2, exp2) in enumerate(polinomio2):
            if exp1 == exp2:
                resultado.append((coef1 - coef2, exp1))
                polinomio2.pop(i)
                encontrado = True
                break
        if not encontrado:
            resultado.append((coef1, exp1))

    for coef2, exp2 in polinomio2:
        resultado.append((-coef2, exp2))
    
    resultado.sort(key=lambda x: x[1], reverse=True)
    
    return formatear_polinomio(resultado)

def formatear_polinomio(polinomio):
    if not polinomio:
        return "0"
    
    terminos = []
    for coef, exp in polinomio:
        if coef == 0:
            continue
        
        signo = " + " if coef > 0 else " - "
        coef_abs = abs(coef)
        
        if exp == 0:
            terminos.append(f"{signo}{coef_abs}")
        elif exp == 1:
            terminos.append(f"{signo}{coef_abs}x")
        else:
            terminos.append(f"{signo}{coef_abs}x^{exp}")
    
    polinomio_str = "".join(terminos)
    
    if polinomio_str.startswith(" + "):
        polinomio_str = polinomio_str[3:]
    elif polinomio_str.startswith(" - "):
        polinomio_str = "-" + polinomio_str[3:]
    
    return polinomio_str

#dividir  //////// a la hora de dividir únicamente es posible sacar el cociente 
def dividir_polinomios(p1, p2):  
    pol1 = {exp: coef for coef, exp in p1}
    pol2 = {exp: coef for coef, exp in p2}
    
    grado1 = max(pol1)
    grado2 = max(pol2)
    
    if grado1 < grado2:
        return "0"
    
    cociente = {}
    residuo = pol1.copy()
    
    while residuo and max(residuo) >= grado2:
        exp_residuo = max(residuo)
        coef_residuo = residuo[exp_residuo]
        
        exp_cociente = exp_residuo - grado2
        coef_cociente = coef_residuo / pol2[grado2]
        
        cociente[exp_cociente] = coef_cociente
        
        for exp, coef in pol2.items():
            exp_nuevo = exp_cociente + exp
            coef_nuevo = coef_cociente * coef
            if exp_nuevo in residuo:
                residuo[exp_nuevo] -= coef_nuevo
                if abs(residuo[exp_nuevo]) < 1e-10:  #
                    del residuo[exp_nuevo]
            else:
                residuo[exp_nuevo] = -coef_nuevo
    
    resultado = sorted(cociente.items(), key=lambda x: -x[0])
    
    def formatear_polinomio(polinomio):
        if not polinomio:
            return "0"
        partes = []
        for exp, coef in polinomio:
            if coef == 0:
                continue
            coef_str = f"{coef:.2f}" if coef % 1 != 0 else str(int(coef))
            if exp == 0:
                partes.append(f"{coef_str}")
            elif exp == 1:
                partes.append(f"{coef_str}x")
            else:
                partes.append(f"{coef_str}x^{exp}")
        return " + ".join(partes).replace("+ -", "- ")
    
    return formatear_polinomio(resultado)

#eliminar
def eliminar_termino(polinomio, coeficiente, exponente):
    return [t for t in polinomio if t != (coeficiente, exponente)]

#verificar
def existe_termino(polinomio, coeficiente, exponente):
    return (coeficiente, exponente) in polinomio

#hago esto para ejecutar todo desde el main
def polinomios():
    polinomio1 = [(5, 2), (2, 1), (1, 0)]  # 5x^2 + 2x + 1
    polinomio2 = [(1, 2), (4, 1), (4, 0)]  # x^2 + 4x + 4

    # Resta
    resultado_resta = restar_polinomios(polinomio1, polinomio2)
    print("Resultado de la resta:", resultado_resta)

    # División
    resultado_division = dividir_polinomios(polinomio1, polinomio2)
    print("Resultado de la división:", resultado_division)

    # Eliminar término (busca en ambos polinomios)
    try:
        coef_eliminar = float(input("Introduce el coeficiente del término a eliminar: "))
        exp_eliminar = int(input("Introduce el exponente del término a eliminar: "))
        
        en_polinomio1 = (coef_eliminar, exp_eliminar) in polinomio1
        en_polinomio2 = (coef_eliminar, exp_eliminar) in polinomio2
        
        if en_polinomio1 and en_polinomio2:
            opcion = input("El término está en ambos polinomios. ¿De cuál deseas eliminarlo? (1/2): ")
            if opcion == "1":
                polinomio1 = eliminar_termino(polinomio1, coef_eliminar, exp_eliminar)
            elif opcion == "2":
                polinomio2 = eliminar_termino(polinomio2, coef_eliminar, exp_eliminar)
            else:
                print("Opción no válida. No se ha eliminado ningún término.")
        elif en_polinomio1:
            polinomio1 = eliminar_termino(polinomio1, coef_eliminar, exp_eliminar)
        elif en_polinomio2:
            polinomio2 = eliminar_termino(polinomio2, coef_eliminar, exp_eliminar)
        else:
            print("El término no se encuentra en ninguno de los polinomios.")
        
        print("Polinomio 1 actualizado:", polinomio1)
        print("Polinomio 2 actualizado:", polinomio2)
    except ValueError:
        print("Error: Entrada inválida. Asegúrate de ingresar un número válido.")

    # Verificar término (busca en ambos polinomios)
    try:
        coef_verificar = float(input("Introduce el coeficiente del término a verificar: "))
        exp_verificar = int(input("Introduce el exponente del término a verificar: "))
        
        existe1 = existe_termino(polinomio1, coef_verificar, exp_verificar)
        print(f"¿Existe el término {coef_verificar}x^{exp_verificar} en el polinomio 1?", existe1)
        
        existe2 = existe_termino(polinomio2, coef_verificar, exp_verificar)
        print(f"¿Existe el término {coef_verificar}x^{exp_verificar} en el polinomio 2?", existe2)
        
    except ValueError:
        print("Error: Entrada inválida. Asegúrate de ingresar un número válido.")