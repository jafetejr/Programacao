
print ("Hello World!")
print (10 + 20)

# Para definir um dado com valor constante, colocar o nome em maiúsculo
#   Utilizar Underline no lugar do espaço ^^

nome = "Jafete"
idade = "34"

print(nome, idade)

nome, idade = "Jafete Junior", 34
print (nome, idade)

# CONVERSÃO DE TIPOS

preco = 100
print(preco)

print(preco / 2)
print(preco // 2)

preco = float(preco)
print(preco)

print(str(preco))

texto = f"idade {idade} preco {preco}"
print (texto)

print(type(preco))
print(type(texto))


# FUNÇÕES DE ENTRADA E SAÍDA

nome = input("Informe o seu nome: ")
sobrenome = input("Informe sou sobrenome: ")
idade = int(input("informe a sua idade: "))

print(nome, sobrenome, end=" \n")
print(idade)

# OPERADORES ARITIMETICOS
# Considera a mesma lógica da matemática comum

print(1 + 1)
print(12 /3)
print(12 // 2)
print(10 % 3) # resto da visisao
print(2 ** 3) # exponenciacao


# OPERADORES DE COMPARAÇÃO

saldo = 450
saque = 200

print(saldo == saque)
print(saldo != saque)
print(saldo >= saque)
print(saldo > saque)
print(saldo <= saque)

resultado = input(saldo == saque)
print((resultado))

# OPERADORES DE ATRIBUICAO

saldo = 200
saldo +=100

print(saldo)

# OPERADORES LOGICOS
#utiliza a regra de precedencia da matemática, ou seja, 
# primeiro resolve os parenteses, depois as multiplicações e divisões,
#  depois as adições e subtrações e por fim os operadores lógicos

# AND = todas as expressões precisam ser verdadeiras para o resultado ser verdadeiro
# OR = apenas uma expressão precisa ser verdadeira para o resultado ser verdadeiro

print(saldo > 100 and saldo < 500)
print(saldo > 100 or saldo < 500)
print(not saldo > 100)


# OPERADORES DE IDENTIDADE
# is = verifica se os objetos são o mesmo
# is not = verifica se os objetos são diferentes
a = [1, 2, 3]
b = a
print(a is b) # True
c = [1, 2, 3]
print(a is c) # False
print(a is not c) # True

# OPERADORES DE ASSOCIAÇÃO
# in = verifica se um valor está presente em uma sequência
# not in = verifica se um valor não está presente em uma sequência
# 
# posso utilizar para verificar uma parte de uma string, 
# ou um elemento de uma lista, ou um caractere de uma tupla, etc

frutas = ["maçã", "banana", "laranja"]
print("maçã" in frutas) # True
print("uva" in frutas) # False
print("uva" not in frutas) # True


print("Fim do programa")

# IDENTAÇÃO
# A indentação é a forma como o código é organizado visualmente,   
#  utilizando espaços ou tabulações para indicar blocos de código.
# Em Python, a indentação é obrigatória e é utilizada para definir blocos de código,
#  como os blocos de uma função, de um loop, de um if, etc

def sacar(valor):

    saldo = 1000

    if saldo > valor:
        print("Saque realizado com sucesso!")
    else:
        print("Valor inválido para saque.")

sacar(200)


# ESTRUTURAS CONDICIONAIS
# if = se
# elif = se não, se
# else = senão

status = "Sucesso" if saldo > 0 else "Falha"
print(f"{status} ao realizar o saque.")