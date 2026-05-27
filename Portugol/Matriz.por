programa
{
	
	funcao inicio()
	{
		cadeia cliente[3][3] = {{" "," "," "},{" "," "," "},{" "," "," "}
		}
		inteiro linha = 0
		inteiro coluna = 0

		
		
		
		faca{
			escreva("Digite o nome do cliente: ")
			leia (cliente[linha][coluna])
			coluna++

			escreva("Digite a cidade: ")
			leia (cliente[linha][coluna])
			coluna++

			escreva("Digite o telefone: ")
			leia (cliente[linha][coluna])
			coluna = 0
			linha++
		}enquanto (linha<3)

		linha = 0
		coluna = 0

		faca{
			escreva ("nome: " + cliente[linha][coluna] + "\n")
			coluna ++
			escreva ("nome: " + cliente[linha][coluna] + "\n")
			coluna ++
			escreva ("telefone: " + cliente[linha][coluna] + "\n")
			coluna = 0
			linha++
			escreva ("\n")
		}enquanto (linha<3)

		
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 738; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */