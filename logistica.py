def calcular_frete(peso):
    if peso <= 20:
        custo = peso * 10.00
    else:
        custo = peso * 15.00

    return custo

peso_carga = float(input("Digite o peso da carga em kg:"))

valor_final = calcular_frete(peso_carga)

print(f"O valor final do frete é: R$ (valor_final:.2f)")