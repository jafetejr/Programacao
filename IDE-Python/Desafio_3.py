# Lê a entrada do usuário (nome do cliente)
entrada = input()

# TODO: Remova espaços extras no início/fim e divida a string em palavras
palavras = entrada.strip().split()


# Dica: Use métodos de string para limpar e separar as palavras

# Capitalize cada palavra (primeira letra maiúscula, demais minúsculas)
palavras_formatadas = [palavra.capitalize() for palavra in palavras]

# Junte as palavras com um único espaço entre elas
nome_formatado = ' '.join(palavras_formatadas)

# Exiba o nome formatado
print(nome_formatado)