valor_compra = int(input())
    
while valor_compra < 0:
        print("Valor inválido. Digite um valor positivo.")
        valor_compra = int(input("Digite o valor da compra: "))

if valor_compra >= 200:
    print("Desconto de 25 reais aplicado!")
elif valor_compra >= 100 and valor_compra <= 199:
    print("Desconto de 10 reais aplicado!")
elif valor_compra >= 50 and valor_compra <= 99:
    print("Parabéns! Você ganhou um brinde!")
else:
    print("Obrigado por comprar conosco!")