#ferramenta de Conversão Dolar x Real--
def converter(valor_dolar):
    taxa = 5.15
    valor_real = valor_dolar * taxa
    return valor_real
print("Conversor dolar x real")
preço = float(input("Digite o preço do produto em Dólar:"))
resultado = converter(preco)
print(f"O valor em reais é: {resultado}:.2f}")