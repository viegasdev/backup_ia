# Importar o módulo tkinter
import tkinter

# Definir variáveis iniciais
conta, numero1_str, numero1_float, operacao_a, operacao_b = '', '', 0, '', ''

# Definir funções a utilizar
def escrever(str):      # Função que introduz um algarismo na entry
    conta = entry.get() # Atribui à variável tudo o que está na entry
    conta = conta + str # Atribui à variável o que está na entry adicionando o dado novo introduzido
    entry.delete(0, 'end') # Apaga o que estava na entry
    entry.insert(0, conta) # Coloca na entry a expressão já com os novos dados

def zero(): # Função que o botão do número vai executar e que escreve o número na entry
    escrever('0') # Executa a função "escrever" com o atributo "0"

def um():
    escrever('1')

def dois():
    escrever('2')
    
def tres():
    escrever('3')
    
def quatro():
    escrever('4')

def cinco():
    escrever('5')
    
def seis():
    escrever('6')

def sete():
    escrever('7')
    
def oito():
    escrever('8')
    
def nove():
    escrever('9')
	
def somar():
	operacao('+')
	
def subtrair():
	operacao('-')
	
def multiplicar():
	operacao('*')

def dividir():
	operacao('/')
    
def clear():
	entry.delete(0, 'end') # Elimina toda a informação presente na Entry
    
def igual(): # Função que lê a conta e mostra o resultado desta na Entry
    global resultado # Define a variável "resultado" como uma variável global
    calcular_a() # Executa a função "calcular_a"
    entry.delete(0, 'end') # Elimina a informação presente na Entry
    entry.insert(0, resultado) # Coloca na Entry o resultado da conta
	
def operacao(operacao_b): # Função que transforma o que está na Entry em float e insere a operação desejada
    global numero1_str, numero1_float, operacao_a, operacao_c # Define como globais as variáveis
    operacao_a = operacao_b # Atribui o símbolo da operação (em string) à variável operacao_a
    numero1_str = entry.get() # Atribui à variável numero1_str os dados da Entry
    numero1_float = float(numero1_str) # Transforma o valor armazenado em numero1_str em float armazenando-o em numero1_float
    escrever(operacao_b) # Apresenta na Entry o símbolo da operação pretendida
    numero1_str = entry.get() # Atribui à variável numero1_str o que está na Entry
	
def calcular_a(): # Função que calcula o resultado da conta
	global numero1_str, numero1_float, operacao_a, numero_2b, resultado # Define como globais as variáveis
	conta = entry.get() # Atribui à variável "conta" o que está na Entry
	numero_2a = conta.replace(numero1_str, '') # Substitui o que está na Entry pelo valor de numero1_str e um espaço em frente
	numero_2b = float(numero_2a) # Atribui à variável numero_2b o valor (em float) de numero_2a
	if operacao_a == '+': 
		resultado = str(numero1_float + numero_2b) # Analisa a operação que se pretende fazer e fá-la

	elif operacao_a == '-':
		resultado = str(numero1_float - numero_2b)
    
	elif operacao_a == '*':
		resultado = str(numero1_float * numero_2b)
    
	elif operacao_a ==  '/':
		resultado = str(numero1_float / numero_2b)
	
	else:
		resultado = 'Erro' # Caso o símbolo de operação não seja um dos definidos, retorna um erro

# Criar janela e configurá-la
window = tkinter.Tk() # Cria a janela
window.title('Calc.') # Atribui um título à janela
window.geometry('205x180') # Atribui o tamanho à janela
window.resizable(0, 0) # Faz com que o tamanho da janela seja fixo


# Criar entry para apresentação da expressão e conta
entry = tkinter.Entry(window, font = 'Arial') # Define a fonte do que está escrito na Entry como Arial
entry.pack()
entry.place(width = 205, height = 20) # Define a posição da Entry na janela

# Criar botões

botao_zero = tkinter.Button(window, height = 2, width = 6, text = '0', command = zero) # Cria o botão com a devida função
botao_zero.pack()

botao_um = tkinter.Button(window, height = 2, width = 6, text = '1', command = um)
botao_um.pack()

botao_dois = tkinter.Button(window, height = 2, width = 6, text = '2', command = dois)
botao_dois.pack()

botao_tres = tkinter.Button(window, height = 2, width = 6, text = '3', command = tres)
botao_tres.pack()

botao_quatro = tkinter.Button(window, height = 2, width = 6, text = '4', command = quatro)
botao_quatro.pack()

botao_cinco = tkinter.Button(window, height = 2, width = 6, text = '5', command = cinco)
botao_cinco.pack()

botao_seis = tkinter.Button(window, height = 2, width = 6, text = '6', command = seis)
botao_seis.pack()

botao_sete = tkinter.Button(window, height = 2, width = 6, text = '7', command = sete)
botao_sete.pack()

botao_oito = tkinter.Button(window, height = 2, width = 6, text = '8', command = oito)
botao_oito.pack()

botao_nove = tkinter.Button(window, height = 2, width = 6, text = '9', command = nove)
botao_nove.pack()

botao_clear = tkinter.Button(window, height = 2, width = 6, text = 'C', command = clear)
botao_clear.pack()

botao_igual = tkinter.Button(window, height = 2, width = 6, text = '=', command = igual)
botao_igual.pack()

botao_mais = tkinter.Button(window, height = 2, width = 6, text = '+', command = somar)
botao_mais.pack()

botao_menos = tkinter.Button(window, height = 2, width = 6, text = '-', command = subtrair)
botao_menos.pack()

botao_multiplicar = tkinter.Button(window, height = 2, width = 6, text = '×', command = multiplicar)
botao_multiplicar.pack() 

botao_dividir = tkinter.Button(window, height = 2, width = 6, text = '÷', command = dividir)
botao_dividir.pack()

# Dispor os botões
botao_um.place(x = 0, y = 20) # Define a posição do botão na janela
botao_dois.place(x = 51, y = 20)
botao_tres.place(x = 102, y = 20)
botao_quatro.place(x = 0, y = 60)
botao_cinco.place(x = 51, y = 60)
botao_seis.place(x = 102, y = 60)
botao_sete.place(x = 0, y = 100)
botao_oito.place(x = 51, y = 100)
botao_nove.place(x = 102, y = 100)
botao_zero.place(x = 0, y = 140)

botao_clear.place(x = 51, y = 140)
botao_igual.place(x = 102, y = 140)
botao_mais.place(x = 153, y = 20)
botao_menos.place(x = 153, y = 60)
botao_multiplicar.place(x = 153, y = 100)
botao_dividir.place(x = 153, y = 140)

# Mainloop da interface gráfica (mantém a janela aberta enquanto o programa está a ser executado)
window.mainloop()