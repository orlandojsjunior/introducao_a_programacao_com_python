# Exercício 2.2 	Digite a seguinte expressão no interpretador: 10 / 3 x 10² + 1 - 10 x 4 / 2

# Tente resolver o mesmo cálculo, usando apenas lápis e papel. Observe como a prioridade das operações é importante.

Expressao = 10 % 3 * 10 ** 2 + 1 - 10 * 4 / 2

print(Expressao)

'''
Expressao: 
10 / 3 x 10² + 1 - 10 x 4 / 2

Seguindo a ordem de operações:
1.	Exponenciação: ( 10² = 100 )
2.	Multiplicação e divisão: 
	( 10 / 3 = 1 ) (resto da divisão de 10 por 3)
	( 1 x 100 = 100 ) (multiplicação do resultado da operação anterior por 100)
	( 10 x 4 = 40 ) (multiplicação)
	( 40 / 2 = 20 ) (divisão)
3.	Adição e subtração: 
	( 100 + 1 = 101 ) (adição)
	( 101 - 20 = 81 ) (subtração do resultado da divisão)
    
Resultado final da expressão é 81.0

'''