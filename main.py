'''from operacoes.soma import soma

a = float(input("Insira o valor de a: "))
b = float(input("Insira o valor de b: "))

resultado = soma(a, b)

print(f"A soma de {a} e {b} é: {resultado} ")'''
'''
def verificar(texto):

    if texto.startswith("Olá"):
        print("A sua frase começa com um 'Olá'.")
    else:
        print("A sua frase não começa com um 'Olá'.")

frase = input("Digite uma frase: ")
verificar(frase)'''


'''def criar_arquivo():

    texto = input("Insira um texto: ")

    with open('texto.txt', 'w')as arquivo:
        arquivo.write(texto)
    print("Arquivo criado com sucesso!")

criar_arquivo()
'''
'''
from operacoes.subtracao import*
from operacoes.multiplicar import*
from operacoes.verificar import*


a = float(input("Insira o valor de a: "))
b = float(input("Insira o valor de b: "))
c = float(input("Insira o valor de c: "))
d = float(input("Insira o valor de d: "))

numero = int(input("Insira um número para a verificar se ele é par: "))
if verirficar_par(numero):
    print(f"O número {numero} digitado é par!")
else:
    print(f"O número {numero} digitado é não par!")
    

total = multi(a, b)
resultado = sub(c, d)

print(f"A multiplicação de {a} e {b} é: {total} ")
print(f"A subtração de {c} e {d} é: {resultado} ")'''

'''
def somar_multiplos_de_tres(numeros):
    try:
        with open(numeros, 'r') as arquivo:
            soma = 0
            for linha in arquivo:
                try:
                    numero = int(linha.strip())
                    if numero % 3 == 0:
                        soma += numero
                except ValueError:
                    continue  
            return soma
    except FileNotFoundError:
        print(f"Erro: O arquivo '{numeros}' não foi encontrado.")
        return 0


arquivo_existente = 'numeros.txt'


resultado = somar_multiplos_de_tres(arquivo_existente)
print(f"A soma dos múltiplos de 3 é: {resultado}")'''


'''
with open('palavras.txt', 'r', encoding='utf-8') as arquivo:
    palavras = arquivo.read().split() 


palavras_filtradas = []
for palavra in palavras:
    if palavra.lower().startswith('b') and palavra.lower().endswith('o'):
        palavras_filtradas.append(palavra)

with open('palavras_filtradas.txt', 'w', encoding='utf-8') as arquivo:
    for palavra in palavras_filtradas:
        arquivo.write(palavra + '\n') 

print("As palavras foram filtradas e salvas em 'palavras_filtradas.txt'.")
'''

'''
with open('palavras.txt', 'r', encoding='utf-8' ) as arquivo:
    for linha in arquivo:
        if linha.strip().endswith('a'):
            print(linha.strip())'''


'''
with open('palavras.txt', 'r', encoding='utf-8' ) as arquivo:
    for linha in arquivo:
        if linha.strip().startswith('M'):
            print(linha.strip())

with open('palavras.txt', 'r', encoding='utf-8' ) as arquivo:
    for linha in arquivo:
        if linha.strip().endswith('A'):
            print(linha.strip())'''