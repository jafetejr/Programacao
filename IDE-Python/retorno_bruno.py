# RESOLUCAO DE PROBLEMA

retorno_bruno = 26
confirmacao_retorno = "S"

data_hoje = int(input("Informe a data de hoje: "))
while data_hoje < 1 or data_hoje > 31:
    print("Data inválida, informe um valor entre 1 e 31")
    data_hoje = int(input("Informe a data de hoje: "))  

if data_hoje >= retorno_bruno:
    print("Bruno já voltou?")
    print(confirmacao_retorno)
    confirmacao_retorno = str(input("Digite S para sim ou F para não: "))
    confirmacao_retorno = confirmacao_retorno.upper()

    while confirmacao_retorno != "S" and confirmacao_retorno != "F":
        print("Valor inválido, digite S para sim ou F para não")
        confirmacao_retorno = str(input("Digite S para sim ou F para não: "))
        confirmacao_retorno = confirmacao_retorno.upper()

    if confirmacao_retorno == "F":
        print("Bruno não voltou, socorrooooooooo")
    elif confirmacao_retorno == "S":
        print("Bruno é o melhor")
else:
    print("Chega logo dia 26!!!!")