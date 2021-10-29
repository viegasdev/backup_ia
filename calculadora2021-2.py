# Receber os números do utilizador
valor_a = input('Insira o primeiro número inteiro:\n')
valor_b = input('Insira o segundo número inteiro:\n')

# Transformar os valores inseridos em inteiros
valor_a_int = int(valor_a)
valor_b_int = int(valor_b)

# Receber a indicação da operação a executar
op = input('Insira o símbolo correspondente à operação a executar:\n')

# Fazer a operação com os números 

# Soma
if op == '+':
	soma = valor_a_int + valor_b_int
	print('O resultado da soma é', soma)
	
# Subtração
if op == '-':
	sub = valor_a_int - valor_b_int
	print('O resultado da subtração é', sub)
	
# Multiplicação
if op == '*':
	mult = valor_a_int * valor_b_int
	print('O resultado da multiplicação é', mult)
	
# Divisão
if op == '/':
	div = valor_a_int / valor_b_int
	print('O resultado da divisão é', div)
