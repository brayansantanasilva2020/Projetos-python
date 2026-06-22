def calcular_frete(peso):
    if peso <= 20:
        custo = peso * 10
        print("Carga Leve")
    else:
        valor = peso * 15 + 20
        print("Carga pesada")

    return custo

peso_carga = float(input("Digite o peso da carga em kg:"))

valor_final = calcular_frete(peso_carga)

print(f"O valor final do frete é: R$(valor_final:.2f)")

#Brayan De Santana Da Silva