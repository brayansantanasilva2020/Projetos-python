# Quiz com 3 questões de múltipla escolha

print("=== QUIZ DE TECNOLOGIA ===")

pontos = 0

# Pergunta 1
print("\n1) Quem criou o Python?")
print("a) Bill Gates")
print("b) Guido van Rossum")
print("c) Elon Musk")

resposta = input("Digite a alternativa correta: ")

if resposta == "b":
    print("Correto! ✅")
    pontos += 1
else:
    print("Errado! ❌")

# Pergunta 2
print("\n2) Qual destas é uma linguagem de programação?")
print("a) HTML")
print("b) Windows")
print("c) Python")

resposta = input("Digite a alternativa correta: ")

if resposta == "c":
    print("Correto! ✅")
    pontos += 1
else:
    print("Errado! ❌")

# Pergunta 3
print("\n3) O que significa CPU?")
print("a) Unidade Central de Processamento")
print("b) Controle de Programa Universal")
print("c) Central Python Unit")

resposta = input("Digite a alternativa correta: ")

if resposta == "a":
    print("Correto! ✅")
    pontos += 1
else:
    print("Errado! ❌")

# Resultado final
print("\n=== RESULTADO FINAL ===")
print("Você acertou", pontos, "de 3 questões!")

#Brayan De Santana Da Silva 2F