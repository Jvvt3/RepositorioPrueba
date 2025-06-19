turistas = {"001": ["John Doe", "Estados Unidos", "12-01-2024"],
"002": ["Emily Smith", "Estados Unidos", "23-03-2024"],
"012": ["Julian Martinez", "Argentina", "19-09-2023"],
"014": ["Agustin Morales", "Argentina", "28-03-2024"],
"005": ["Carlos Garcia", "Mexico", "10-05-2024"],
"006": ["Maria Lopez", "Mexico", "08-12-2023"],
"007": ["Joao Silva", "Brasil", "20-06-2024"],
"003": ["Michael Brown", "Estados Unidos", "05-07-2023"],
"004": ["Jessica Davis", "Estados Unidos", "15-11-2024"],
"008": ["Ana Santos", "Brasil", "03-10-2023"],
"010": ["Martin Fernandez", "Argentina", "13-02-2023"],
"011": ["Sofia Gomez", "Argentina", "07-04-2024"],
}

def menu():
    print("-"*60)
    print("turistas por pais")
    print("turistas por mes")
    print("Deportar turista")
    print("Salir")
    print("-"*60)

    opcion=input("seleccione su opción(1-4): ")
    return opcion


def turistas_por_pais(pais):
    for elemento in turistas.values():
        if elemento[1].upper()==str(pais).upper():
            print(f"Nombre: {elemento[0]}")

turistas_por_pais("Brasil")

def turistas_por_mes(mes,pais):
    contador_turista=0
    for Datoturista in turistas.values():
        fecha=Datoturista[2]
        mes_fecha=fecha[3:5]
        
        if int(mes_fecha)==int(mes) and Datoturista[1].upper==pais.upper():
            contador_turista+=1
            print(f"{contador_turista}")
        

turistas_por_mes()