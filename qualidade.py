#Multiplas funçoes -- exercicio controle de qualidade--
def cabecalho():
    print("\n" + "=" *30)
    print("SISTEMA DE QUALIDADE")
def verificador_status (peso):
    if peso >= 50 and peso <=100:
        return "Aprovada"
    else:
        return "Reprovado"
cabecalho()
peso_item = float(input("Digite o peso do item em gramas:"))
status = verificador_status(peco_item)
print(f"Resultado da inspeção:{status}")
print("=" *30)